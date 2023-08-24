import unittest
from unittest.mock import Mock, patch
import json
import requests
from api_integration import get_location_info


class TestGetLocationInfo(unittest.TestCase):
    @patch("requests.get")
    def test_successful_response(self, mock_get):
        expected_address = "123 Main St, City, Country"

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response_data = {
            "resourceSets": [{
                "resources": [{
                    "address": {
                        "formattedAddress": expected_address
                    }
                }]
            }]
        }
        mock_response.json.return_value = mock_response_data
        mock_get.return_value = mock_response

        location = get_location_info("123 Main St")
        self.assertEqual(location, expected_address)

    @patch("requests.get")
    def test_location_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response_data = {
            "resourceSets": []
        }
        mock_response.json.return_value = mock_response_data
        mock_get.return_value = mock_response

        location = get_location_info("Nonexistent Location")
        self.assertEqual(location, "Location not found")


if __name__ == "__main__":
    unittest.main()

