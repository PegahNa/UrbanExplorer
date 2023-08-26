import unittest
from unittest.mock import patch
from api_integration import get_location_info

class TestGetLocationInfo(unittest.TestCase):
    @patch("requests.get")
    def test_get_location_info_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "resourceSets": [
                {
                    "resources": [
                        {
                            "point": {
                                "coordinates": [123.456, 789.012]
                            },
                            "address": {
                                "formattedAddress": "Sample Address"
                            }
                        }
                    ]
                }
            ]
        }

        location, latitude, longitude = get_location_info("Sample Query")

        self.assertEqual(location, "Sample Address")
        self.assertEqual(latitude, 123.456)
        self.assertEqual(longitude, 789.012)

    @patch("requests.get")
    def test_get_location_info_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        location, latitude, longitude = get_location_info("Nonexistent Location")

        self.assertEqual(location, "Location not found")
        self.assertIsNone(latitude)
        self.assertIsNone(longitude)

if __name__ == "__main__":
    unittest.main()

