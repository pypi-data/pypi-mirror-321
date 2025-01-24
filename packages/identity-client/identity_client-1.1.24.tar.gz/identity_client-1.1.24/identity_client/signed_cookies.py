from django.conf import settings
from django.http import HttpResponseRedirect

from datetime import datetime
import time
import logging
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner
from urllib.parse import urlparse

from identity_client.helpers import get_assets_v2_domain


# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Heavily inspired on a couple of existing solutions in stackoverflow and AWS documentation.
# Adapted for good measure, to serve our needs.

def rsa_signer(message):
    logger.info("Signing the policy using the private key.")
    return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())


def generate_signed_cookies(resource=None, expire_minutes=60, assets_domain=None):
    """
    @resource   path to s3 object inside bucket(or a wildcard path,e.g. '/blah/*' or  '*')
    @expire_minutes     how many minutes before we expire these access credentials (within cookie)
    return tuple of domain used in resource URL & dict of name=>value cookies
    """
    logger.info("Entering generate_signed_cookies().")
    if not resource:
        resource = '*'

    dist = SignedCookiedCloudfrontDistribution(assets_domain)
    logger.info(
        f"Generating signed cookies for resource: {resource}, "
        f"expire_minutes: {expire_minutes}, assets_domain: {assets_domain}."
    )
    return dist.create_signed_cookies(resource, expire_minutes=expire_minutes)


class SignedCookiedCloudfrontDistribution():

    def __init__(self,cname):
        logger.info(f"Initializing SignedCookiedCloudfrontDistribution with cname={cname}.")
        self.domain = cname

    def get_http_resource_url(self,resource=None,secure=False):
        """
        @resource   optional path and/or filename to the resource 
                   (e.g. /mydir/somefile.txt);
                    defaults to wildcard if unset '*'
        @secure     whether to use https or http protocol for Cloudfront URL - update  
                    to match your distribution settings 
        return constructed URL
        """
        logger.info(f"Constructing HTTP resource URL for resource={resource}, secure={secure}.")
        if not resource:
            resource = '*'
            logger.info("Resource not provided. Using default: '*'.")
        protocol = "http" if not secure else "https"
        http_resource = '%s://%s/%s' % (protocol,self.domain,resource)
        logger.info(f"Constructed http_resource: {http_resource}.")
        return http_resource

    def create_signed_cookies(self,resource,expire_minutes=60):
        """
        generate the Cloudfront download distirbution signed cookies
        @resource   path to the file, path, or wildcard pattern to generate policy for
        @expire_minutes  number of minutes until expiration
        return      tuple with domain used within policy (so it matches 
                    cookie domain), and dict of cloudfront cookies you
                    should set in request header
        """
        logger.info(f"Entering create_signed_cookies() for resource: {resource}, expire_minutes: {expire_minutes}")
        http_resource = self.get_http_resource_url(resource, secure=True)    #per-file access #NOTE secure should match security settings of cloudfront distribution

        cloudfront_signer = CloudFrontSigner(settings.CLOUDFRONT_SIGNED_COOKIES_KEY_PAIR_ID, rsa_signer)
        expires = SignedCookiedCloudfrontDistribution.get_expires(expire_minutes)
        logger.info(f"Generated expiration time: {expires}.")
        policy = cloudfront_signer.build_policy(http_resource,datetime.fromtimestamp(expires))
        logger.info(f"Raw policy: {policy}")
        encoded_policy = cloudfront_signer._url_b64encode(policy.encode('utf-8')).decode('utf-8')

        #assemble the 3 Cloudfront cookies
        signature = rsa_signer(policy.encode('utf-8'))
        encoded_signature = cloudfront_signer._url_b64encode(signature).decode('utf-8')
        cookies = {
            "CloudFront-Policy": encoded_policy,
            "CloudFront-Signature": encoded_signature,
            "CloudFront-Key-Pair-Id": settings.CLOUDFRONT_SIGNED_COOKIES_KEY_PAIR_ID,
        }
        logger.info(f"Generated cookies: {cookies}.")
        return cookies

    @staticmethod
    def get_expires(minutes):
        logger.info(f"Calculating expiration time with minutes={minutes}.")
        unixTime = time.time() + (minutes * 60)
        expires = int(unixTime)  #if not converted to int causes Malformed Policy error and has 2 decimals in value
        logger.info(f"Calculated expiration timestamp: {expires}.")
        return expires


if getattr(settings, 'CLOUDFRONT_SIGNED_COOKIES', False):
    #dist = SignedCookiedCloudfrontDistribution(settings.CLOUDFRONT_SIGNED_COOKIES_CNAME)
    logger.info("Loading private key for CloudFront signing.")
    private_key = serialization.load_pem_private_key(
        settings.CLOUDFRONT_SIGNED_COOKIES_PRIVATE_KEY.encode('utf-8'),
        password=None,
        backend=default_backend()
    )


def add_signed_cookies(request, response, assets_domain, domain=settings.CLOUDFRONT_SIGNED_COOKIES_DOMAIN):
    # Generate signed cookies and add them to the response.
    # The idea is to generate the cookies at each request and have them relatively short lived.
    logger.info(f"Entering add_signed_cookies() with assets_domain={assets_domain}, domain={domain}.")
    try:
        if getattr(settings, 'CLOUDFRONT_SIGNED_COOKIES', False):
            # Remove existing cookies
            logger.info("Removing existing cookies to avoid duplication.")
            response.delete_cookie("CloudFront-Key-Pair-Id", domain=domain, path="/")
            response.delete_cookie("CloudFront-Policy", domain=domain, path="/")
            response.delete_cookie("CloudFront-Signature", domain=domain, path="/")

            # Generate new cookies
            logger.info("Generating new signed cookies.")
            cookies = generate_signed_cookies(
                resource=settings.CLOUDFRONT_SIGNED_COOKIES_RESOURCE,
                assets_domain=assets_domain
            )

            # Set new cookies
            for key, value in cookies.items():
                response.set_cookie(key, value, domain=domain, path="/")
                logger.info(f"Set cookie: {key} for domain: {domain}")

            # Redirect to ensure cookies are applied
            redirect_url = request.build_absolute_uri()
            logger.info(f"Redirecting to {redirect_url} after setting cookies.")
            return HttpResponseRedirect(redirect_url)
        else:
            logger.warning("CloudFront signed cookies are not enabled in settings.")
    except Exception as ex:
        logger.error(f"An error occurred while adding signed cookies. {ex}", exc_info=ex)
    return response


def get_domain_from_header(host_header):
    logger.info(f"Entering get_domain_from_header() with host_header={host_header}.")
    if "hub3d.pvh.com" in host_header:
        return ".hub3d.pvh.com"
    parsed_header = urlparse(host_header).netloc or urlparse(host_header).path
    domain = '.'.join(parsed_header.split('.')[-2:])
    logger.info(f"Extracted domain from header: {domain}.")
    return '.' + domain


class SignedCookiesMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        logger.info("SignedCookiesMiddleware initialized.")

    def __call__(self, request):
        logger.info("Entering SignedCookiesMiddleware.")
        response = self.get_response(request)

        if not getattr(request, 'user', None):
            logger.warning("User object is not available in the request.")
        elif not request.user.is_authenticated:
            logger.warning("User is not authenticated. Skipping signed cookies setup.")
        else:
            try:
                logger.info(f"Authenticated user detected: {request.user}. Adding signed cookies.")
                if 'HTTP_HOST' in request.META:
                    logger.info("HTTP_HOST found in request.META.")
                    assets_domain = get_assets_v2_domain(request)
                    host = request.META['HTTP_HOST']
                    domain = get_domain_from_header(host)
                    logger.info(f"Assets domain: {assets_domain}, Domain: {domain}")
                    add_signed_cookies(request, response, assets_domain, domain)
                else:
                    assets_domain = 'assets-v2.hub3d.pvh.com'
                    domain = assets_domain
                    logger.info(f"Default Assets domain: {assets_domain}, Default Domain: {domain}")
                add_signed_cookies(request, response, assets_domain, domain)
            except Exception as e:
                logger.error(f"Failed to set signed cookies: {e}", exc_info=True)

        return response
