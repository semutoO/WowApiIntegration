import pytest
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

@pytest.fixture
def mock_credentials():
    from WowApiIntegration.Dto.WowApiCredentialModel import WowApiCredentialModel
    return WowApiCredentialModel("test_client_id", "test_client_secret")
