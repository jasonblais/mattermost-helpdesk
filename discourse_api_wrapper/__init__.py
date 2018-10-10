import os
import requests
from .discourse import Discourse

DISCOURSE_API_KEY = os.environ.get('DISCOURSE_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

if DISCOURSE_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://meta.discourse.org/t/discourse-api-documentation/22706 "
        "for information on how to retrieve an API token from Discourse."
    )

session = requests.Session()
session.params = {}
session.params['api_key'] = DISCOURSE_API_KEY
