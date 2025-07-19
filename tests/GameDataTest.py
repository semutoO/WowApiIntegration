import pytest
from unittest.mock import Mock, patch
from WowApiIntegration.Controllers.WowGameDataController import WowGameDataController
from WowApiIntegration.Dto.GameDataDto.WowApiAchievementRequest import WowApiAchievementRequest

class TestWowGameDataController:
    def test_get_achievement_index(self, mock_credentials):
        controller = WowGameDataController(mock_credentials)
        request = WowApiAchievementRequest()
        
        with patch.object(controller, 'ApiInvoker') as mock_invoker:
            mock_invoker.return_value = {"success": True}
            result = controller.GetAchievementIndex(request)
            
            assert request.endpoint == "/data/wow/achievement/index"
            mock_invoker.assert_called_once_with(request)
            assert result == {"success": True}

    def test_get_achievement(self, mock_credentials):
        controller = WowGameDataController(mock_credentials)
        request = WowApiAchievementRequest()
        request.achievementId = 123
        
        with patch.object(controller, 'ApiInvoker') as mock_invoker:
            mock_invoker.return_value = {"success": True}
            result = controller.GetAchievement(request)
            
            assert request.endpoint == "/data/wow/achievement/123"
            mock_invoker.assert_called_once_with(request)
