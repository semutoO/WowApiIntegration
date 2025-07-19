import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from WowApiIntegration.AppServices.WowApiInvoker import WowApiInvoker

class TestWowApiInvoker:
    def test_get_api_url(self, mock_credentials):
        invoker = WowApiInvoker(region="us", creds=mock_credentials)
        assert invoker.GetApiUrl() == "https://us.api.blizzard.com"

    def test_init_defaults(self):
        from WowApiIntegration.Dto.WowApiCredentialModel import WowApiCredentialModel
        creds = WowApiCredentialModel("test", "secret")
        invoker = WowApiInvoker(creds=creds)
        assert invoker.region == "us"
        assert invoker.apiUrl == "api.blizzard.com"
