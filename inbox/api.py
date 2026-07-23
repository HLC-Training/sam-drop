import logging
import requests
import urllib3
from requests.exceptions import ProxyError, Timeout, ConnectionError

from xyleme_common.constants import CLIENT_ID, CLIENT_SECRET, OAUTH_URLS, REQUEST_VERIFY_SSL


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger("XylemeApp.API")


def get_access_token():
    """Get OAuth2 token from the first working auth endpoint.

    Raises:
        Exception: If authentication fails with diagnostic details about the failure.
    """
    if not CLIENT_ID or not CLIENT_SECRET:
        raise Exception(
            "Missing XYLEME_CLIENT_ID or XYLEME_CLIENT_SECRET environment variable"
        )

    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }

    errors = []

    for url in OAUTH_URLS:
        try:
            logger.debug(f"Attempting authentication with: {url}")
            response = requests.post(
                url,
                data=payload,
                verify=REQUEST_VERIFY_SSL,
                timeout=10
            )

            if response.status_code == 200:
                logger.debug(f"Authentication successful with {url}")
                return response.json()["access_token"]
            else:
                error_msg = f"HTTP {response.status_code} from {url}"
                try:
                    error_detail = response.json()
                    error_msg += f": {error_detail.get('error_description', error_detail)}"
                except Exception:
                    error_msg += f": {response.text[:200]}"
                logger.warning(error_msg)
                errors.append(error_msg)

        except ProxyError as e:
            error_msg = (
                f"ProxyError from {url}: {str(e)}. "
                "Check HTTPS_PROXY/HTTP_PROXY environment variables, or set NO_PROXY "
                "for core-gevernova.bravais.com and gevernova.xyleme.com if direct access is required."
            )
            logger.warning(error_msg)
            errors.append(error_msg)

        except Timeout as e:
            error_msg = (
                f"Timeout connecting to {url} (10s). "
                "The server may be unreachable or network is slow. "
                "Check firewall, proxy, and network connectivity."
            )
            logger.warning(error_msg)
            errors.append(error_msg)

        except ConnectionError as e:
            error_msg = (
                f"Connection failed to {url}: {str(e)}. "
                "Check network connectivity, firewall rules, and proxy settings."
            )
            logger.warning(error_msg)
            errors.append(error_msg)

        except Exception as e:
            error_msg = f"Unexpected error with {url}: {type(e).__name__}: {str(e)}"
            logger.warning(error_msg)
            errors.append(error_msg)

    # All URLs failed - provide comprehensive error message
    diagnostic = (
        f"Could not authenticate. Tried {len(OAUTH_URLS)} endpoint(s). "
        f"SSL verification: {REQUEST_VERIFY_SSL}. "
        f"Details:\n" + "\n".join([f"  - {err}" for err in errors])
    )
    logger.error(diagnostic)
    raise Exception(diagnostic)


def fetch_paginated(url, headers, limit=1000, params=None, skip_param="skip", limit_param="max"):
    """Fetch a list endpoint that supports limit/offset style paging."""
    query_params = dict(params or {})
    all_data = []
    current_offset = 0

    while True:
        query_params[limit_param] = limit
        query_params[skip_param] = current_offset

        try:
            response = requests.get(
                url,
                headers=headers,
                params=query_params,
                verify=REQUEST_VERIFY_SSL,
                timeout=60,
            )
        except ProxyError as e:
            raise RuntimeError(
                "Proxy tunnel failed while calling Xyleme API. "
                "Check HTTPS_PROXY/HTTP_PROXY settings, or set NO_PROXY for core-gevernova.bravais.com if direct access is required. "
                f"Endpoint: {url}"
            ) from e
        response.raise_for_status()

        result = response.json()
        batch = result.get("value") if isinstance(result, dict) else result

        if not batch or not isinstance(batch, list):
            break

        all_data.extend(batch)

        if len(batch) < limit:
            break

        current_offset += limit

    return all_data
