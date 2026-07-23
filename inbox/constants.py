import os

TOKEN_URL = os.getenv("XYLEME_TOKEN_URL", "https://gevernova.xyleme.com")
SYNDICATE_URL = os.getenv("XYLEME_SYNDICATE_URL",
                          "https://core-gevernova.bravais.com")
ANALYTICS_DOMAIN = os.getenv("XYLEME_ANALYTICS_DOMAIN", "gevernova")

XYLEME_CLIENT_ID = "***REMOVED***"
XYLEME_CLIENT_SECRET = "***REMOVED***"

CLIENT_ID = XYLEME_CLIENT_ID
CLIENT_SECRET = XYLEME_CLIENT_SECRET

OAUTH_URLS = [
    f"{TOKEN_URL}/api/v1/oauth2/token",
    f"{SYNDICATE_URL}/api/v1/oauth2/token",
]

REQUEST_VERIFY_SSL = os.getenv("XYLEME_VERIFY_SSL", "false").strip().lower() in {
    "1", "true", "yes"}
