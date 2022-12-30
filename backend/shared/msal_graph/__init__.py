import msal
import requests

from django.core.cache import cache

from shared.env_util import getenv


class MsalGraph:
    def __init__(self):
        self.scopes = ['https://graph.microsoft.com/.default']
        self.cache = msal.SerializableTokenCache()
        self.app = msal.ConfidentialClientApplication(
            client_id=getenv('ADFS_CLIENT_ID'),
            client_credential=getenv('ADFS_SECRET'),
            authority=f"https://login.microsoftonline.com/{getenv('ADFS_TENANT_ID')}",
            token_cache=self.cache,
        )

    # @staticmethod
    # def _build_cache():
    #     msal_cache = msal.SerializableTokenCache()
    #     if cache.get("token_cache"):
    #         msal_cache.deserialize(cache["token_cache"])
    #     return msal_cache
    #
    # def _update_cache(self):
    #     if self.cache.has_state_changed:
    #         cache["token_cache"] = self.cache.serialize()

    def _get_token_from_cache(self):
        accounts = self.app.get_accounts()
        if accounts:  # So all account(s) belong to the current signed-in user
            result = self.app.acquire_token_silent(self.scopes, account=accounts[0])
            return result

    def login(self, username: str, password: str):
        return self.app.acquire_token_by_username_password(username, password, self.scopes)

    def graph_get(self, resource: str, **kwargs):
        headers = kwargs.pop('headers', {})
        token = self._get_token_from_cache()
        headers['Authorization'] = {'Authorization': f"Bearer {token['access_token']}"}
        url = f"https://graph.microsoft.com{resource}"
        return requests.get(url, headers=headers, **kwargs).json()

    def graph_post(self, resource: str, **kwargs):
        headers = kwargs.pop('headers', {})
        token = self._get_token_from_cache()
        headers['Authorization'] = {'Authorization': f"Bearer {token['access_token']}"}
        url = f"https://graph.microsoft.com{resource}"
        return requests.post(url, headers=headers, **kwargs).json()
