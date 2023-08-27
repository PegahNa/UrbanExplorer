import unittest
from activity_recommender.activities.search import Filter


class TestFilter(unittest.TestCase):
    # It'll run its code before every single test
    def setUp(self):
        # It'll mock the data from all the cities in the JSON file
        self.madrid_data = [
    {
      "activity": "Plaza Mayor",
      "price": 0,
      "rating": 4.6,
      "wheelchair_accessible_entrance": False,
      "hearing_accessibility": False,
      "visual_accessibility": False,
      "opening_hours": {
        "everyday": "24hs",
        "specific_times": []
      }
    },
    {
      "activity": "El Retiro Park",
      "price": 0,
      "rating": 4.8,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": False,
      "visual_accessibility": False,
      "opening_hours": {
        "everyday": "24hs",
        "specific_times": []
      }
    },
    {
      "activity": "Museo nacional del Prado",
      "price": 15,
      "rating": 4.7,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": True,
      "visual_accessibility": True,
      "opening_hours": {
        "everyday": "",
        "specific_times": [
          { "day": "Monday", "open": "10:00", "close": "20:00" },
          { "day": "Tuesday", "open": "10:00", "close": "20:00" },
          { "day": "Wednesday", "open": "10:00", "close": "20:00" },
          { "day": "Thursday", "open": "10:00", "close": "20:00" },
          { "day": "Friday", "open": "10:00", "close": "20:00" },
          { "day": "Saturday", "open": "10:00", "close": "20:00" },
          { "day": "Sunday", "open": "10:00", "close": "19:00" }
        ]
      }
    },
    {
      "activity": "Royal Palace of Madrid",
      "price": 12,
      "rating": 4.6,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": True,
      "visual_accessibility": True,
      "opening_hours": {
        "everyday": "",
        "specific_times": [
          { "day": "Monday", "open": "10:00", "close": "19:00" },
          { "day": "Tuesday", "open": "10:00", "close": "19:00" },
          { "day": "Wednesday", "open": "10:00", "close": "19:00" },
          { "day": "Thursday", "open": "10:00", "close": "19:00" },
          { "day": "Friday", "open": "10:00", "close": "19:00" },
          { "day": "Saturday", "open": "10:00", "close": "19:00" },
          { "day": "Sunday", "open": "10:00", "close": "16:00" }
        ]
      }
    },
    {
      "activity": "Santiago Bernabeu Stadium",
      "price": 15,
      "rating": 4.6,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": False,
      "visual_accessibility": False,
      "opening_hours": {
        "everyday": "",
        "specific_times": [
          { "day": "Monday", "open": "09:30", "close": "19:00" },
          { "day": "Tuesday", "open": "09:30", "close": "19:00" },
          { "day": "Wednesday", "open": "09:30", "close": "19:00" },
          { "day": "Thursday", "open": "09:30", "close": "19:00" },
          { "day": "Friday", "open": "09:30", "close": "19:00" },
          { "day": "Saturday", "open": "09:30", "close": "19:00" },
          { "day": "Sunday", "open": "10:00", "close": "18:30" }
        ]
      }
    },
    {
      "activity": "Mercado de San Miguel",
      "price": 0,
      "rating": 4.4,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": False,
      "visual_accessibility": False,
      "opening_hours": {
        "everyday": "",
        "specific_times": [
          { "day": "Monday", "open": "10:00", "close": "23:00" },
          { "day": "Tuesday", "open": "10:00", "close": "23:00" },
          { "day": "Wednesday", "open": "10:00", "close": "23:00" },
          { "day": "Thursday", "open": "10:00", "close": "23:00" },
          { "day": "Friday", "open": "10:00", "close": "23:59:59.9999999" },
          { "day": "Saturday", "open": "10:00", "close": "23:59:59.9999999" },
          { "day": "Sunday", "open": "10:00", "close": "23:00" }
        ]
      }
    },
    {
      "activity": "Puerta de Alcala",
      "price": 0,
      "rating": 4.7,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": False,
      "visual_accessibility": False,
      "opening_hours": {
        "everyday": "24hs",
        "specific_times": []
      }
    }
  ]
        self.paris_data = [
            {
              "activity": "Eiffel Tower",
              "price": 16,
              "rating": 4.7,
              "wheelchair_accessible_entrance": True,
              "hearing_accessibility": True,
              "visual_accessibility": True,
              "opening_hours": {
                "everyday" : "",
                "specific_times" : [
                {"day": "Monday", "open": "09:00", "close": "23:00"},
                {"day": "Tuesday", "open": "09:00", "close": "23:00"},
                {"day": "Wednesday", "open": "09:00", "close": "23:00"},
                {"day": "Thursday", "open": "09:00", "close": "23:00"},
                {"day": "Friday", "open": "09:00", "close": "23:00"},
                {"day": "Saturday", "open": "09:00", "close": "23:00"},
                {"day": "Sunday", "open": "09:00", "close": "23:00"}
              ]}
            },
            {
              "activity": "Louvre Museum",
              "price": 15,
              "rating": 4.8,
              "wheelchair_accessible_entrance": True,
              "hearing_accessibility": True,
              "visual_accessibility": True,
              "opening_hours": {
                "everyday" : "",
                "specific_times" : [
                {"day": "Monday", "open": "09:00", "close": "18:00"},
                {"day": "Tuesday", "open": "09:00", "close": "21:45"},
                {"day": "Wednesday", "open": "09:00", "close": "21:45"},
                {"day": "Thursday", "open": "09:00", "close": "18:00"},
                {"day": "Friday", "open": "09:00", "close": "21:45"},
                {"day": "Saturday", "open": "09:00", "close": "18:00"},
                {"day": "Sunday", "open": "09:00", "close": "18:00"}
              ]}
            },
            {
              "activity": "Notre-Dame Cathedral",
              "price": 0,
              "rating": 4.6,
              "wheelchair_accessible_entrance": True,
              "hearing_accessibility": False,
              "visual_accessibility": False,
              "opening_hours": {
                "everyday" : "",
                "specific_times" : [
                {"day": "Monday", "open": "08:00", "close": "18:45"},
                {"day": "Tuesday", "open": "08:00", "close": "18:45"},
                {"day": "Wednesday", "open": "08:00", "close": "18:45"},
                {"day": "Thursday", "open": "08:00", "close": "18:45"},
                {"day": "Friday", "open": "08:00", "close": "18:45"},
                {"day": "Saturday", "open": "08:00", "close": "18:45"},
                {"day": "Sunday", "open": "08:00", "close": "18:45"}
              ]}
            },
            {
              "activity": "Mondaytmartre",
              "price": 0,
              "rating": 4.5,
              "wheelchair_accessible_entrance": False,
              "hearing_accessibility": False,
              "visual_accessibility": False,
              "opening_hours": {
                "everyday" : "24hs",
                "specific_times" : []}
            },
            {
              "activity": "Seine River Cruise",
              "price": 12,
              "rating": 4.7,
              "wheelchair_accessible_entrance": True,
              "hearing_accessibility": True,
              "visual_accessibility": True,
              "opening_hours": {
                "everyday" : "",
                "specific_times" : [
                {"day": "Monday", "open": "09:00", "close": "23:00"},
                {"day": "Tuesday", "open": "09:00", "close": "23:00"},
                {"day": "Wednesday", "open": "09:00", "close": "23:00"},
                {"day": "Thursday", "open": "09:00", "close": "23:00"},
                {"day": "Friday", "open": "09:00", "close": "23:00"},
                {"day": "Saturday", "open": "09:00", "close": "23:00"},
                {"day": "Sunday", "open": "09:00", "close": "23:00"}
              ]}
            },
            {
              "activity": "Versailles Palace",
              "price": 20,
              "rating": 4.6,
              "wheelchair_accessible_entrance": True,
              "hearing_accessibility": True,
              "visual_accessibility": True,
              "opening_hours": {
                "everyday" : "",
                "specific_times" : [
                {"day": "Monday", "open": "09:00", "close": "18:30"},
                {"day": "Tuesday", "open": "09:00", "close": "18:30"},
                {"day": "Wednesday", "open": "09:00", "close": "18:30"},
                {"day": "Thursday", "open": "09:00", "close": "18:30"},
                {"day": "Friday", "open": "09:00", "close": "18:30"},
                {"day": "Saturday", "open": "09:00", "close": "18:30"},
                {"day": "Sunday", "open": "09:00", "close": "18:30"}
              ]}
            },
            {
              "activity": "Centre Pompidou",
              "price": 14,
              "rating": 4.5,
              "wheelchair_accessible_entrance": True,
              "hearing_accessibility": True,
              "visual_accessibility": True,
              "opening_hours": {
                "everyday" : "",
                "specific_times" : [
                {"day": "Monday", "open": "11:00", "close": "21:00"},
                {"day": "Tuesday", "open": "11:00", "close": "21:00"},
                {"day": "Wednesday", "open": "11:00", "close": "21:00"},
                {"day": "Thursday", "open": "11:00", "close": "21:00"},
                {"day": "Friday", "open": "11:00", "close": "21:00"},
                {"day": "Saturday", "open": "11:00", "close": "21:00"},
                {"day": "Sunday", "open": "11:00", "close": "21:00"}
              ]}
            }
          ]
        self.new_york_data = [
    {
      "activity": "Central Park",
      "price": 0,
      "rating": 4.8,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": False,
      "visual_accessibility": False,
      "opening_hours": {
        "everyday": "24hs",
        "specific_times": []
      }
    },
    {
      "activity": "Times Square",
      "price": 0,
      "rating": 4.7,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": False,
      "visual_accessibility": False,
      "opening_hours": {
        "everyday": "24hs",
        "specific_times": []
      }
    },
    {
      "activity": "The Metropolitan Museum of Art",
      "price": 25,
      "rating": 4.9,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": True,
      "visual_accessibility": True,
      "opening_hours": {
        "everyday": "",
        "specific_times": [
          { "day": "Monday", "open": "10:00", "close": "17:30" },
          { "day": "Tuesday", "open": "10:00", "close": "17:30" },
          { "day": "Wednesday", "open": "10:00", "close": "17:30" },
          { "day": "Thursday", "open": "10:00", "close": "17:30" },
          { "day": "Friday", "open": "10:00", "close": "21:00" },
          { "day": "Saturday", "open": "10:00", "close": "21:00" },
          { "day": "Sunday", "open": "10:00", "close": "17:30" }
        ]
      }
    },
    {
      "activity": "Statue of Liberty",
      "price": 20,
      "rating": 4.6,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": True,
      "visual_accessibility": True,
      "opening_hours": {
        "everyday": "",
        "specific_times": [
          { "day": "Monday", "open": "08:30", "close": "16:30" },
          { "day": "Tuesday", "open": "08:30", "close": "16:30" },
          { "day": "Wednesday", "open": "08:30", "close": "16:30" },
          { "day": "Thursday", "open": "08:30", "close": "16:30" },
          { "day": "Friday", "open": "08:30", "close": "16:30" },
          { "day": "Saturday", "open": "08:30", "close": "16:30" },
          { "day": "Sunday", "open": "08:30", "close": "16:30" }
        ]
      }
    },
    {
      "activity": "Empire State Building",
      "price": 38,
      "rating": 4.5,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": True,
      "visual_accessibility": True,
      "opening_hours": {
        "everyday": "",
        "specific_times": [
          { "day": "Monday", "open": "10:00", "close": "23:00" },
          { "day": "Tuesday", "open": "10:00", "close": "23:00" },
          { "day": "Wednesday", "open": "10:00", "close": "23:00" },
          { "day": "Thursday", "open": "10:00", "close": "23:00" },
          { "day": "Friday", "open": "10:00", "close": "23:00" },
          { "day": "Saturday", "open": "10:00", "close": "23:00" },
          { "day": "Sunday", "open": "10:00", "close": "23:00" }
        ]
      }
    },
    {
      "activity": "Brooklyn Bridge",
      "price": 0,
      "rating": 4.7,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": True,
      "visual_accessibility": True,
      "opening_hours": {
        "everyday": "24hs",
        "specific_times": []
      }
    },
    {
      "activity": "Central Park Zoo",
      "price": 14,
      "rating": 4.4,
      "wheelchair_accessible_entrance": True,
      "hearing_accessibility": True,
      "visual_accessibility": True,
      "opening_hours": {
        "everyday": "",
        "specific_times": [
          { "day": "Monday", "open": "10:00", "close": "17:00" },
          { "day": "Tuesday", "open": "10:00", "close": "17:00" },
          { "day": "Wednesday", "open": "10:00", "close": "17:00" },
          { "day": "Thursday", "open": "10:00", "close": "17:00" },
          { "day": "Friday", "open": "10:00", "close": "17:00" },
          { "day": "Saturday", "open": "10:00", "close": "17:00" },
          { "day": "Sunday", "open": "10:00", "close": "17:00" }
        ]
      }
    }
  ]


    # VALID CASES
    def test_filter_by_price_medium(self):
        city_filter = Filter(self.madrid_data, "madrid")
        target_price = "medium"

        result = city_filter.filter_by_price(target_price)
        expected_result = [{'activity': 'Museo nacional del Prado', 'price': 15, 'rating': 4.7, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '10:00', 'close': '20:00'}, {'day': 'Tuesday', 'open': '10:00', 'close': '20:00'}, {'day': 'Wednesday', 'open': '10:00', 'close': '20:00'}, {'day': 'Thursday', 'open': '10:00', 'close': '20:00'}, {'day': 'Friday', 'open': '10:00', 'close': '20:00'}, {'day': 'Saturday', 'open': '10:00', 'close': '20:00'}, {'day': 'Sunday', 'open': '10:00', 'close': '19:00'}]}}, {'activity': 'Royal Palace of Madrid', 'price': 12, 'rating': 4.6, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '10:00', 'close': '19:00'}, {'day': 'Tuesday', 'open': '10:00', 'close': '19:00'}, {'day': 'Wednesday', 'open': '10:00', 'close': '19:00'}, {'day': 'Thursday', 'open': '10:00', 'close': '19:00'}, {'day': 'Friday', 'open': '10:00', 'close': '19:00'}, {'day': 'Saturday', 'open': '10:00', 'close': '19:00'}, {'day': 'Sunday', 'open': '10:00', 'close': '16:00'}]}}, {'activity': 'Santiago Bernabeu Stadium', 'price': 15, 'rating': 4.6, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': False, 'visual_accessibility': False, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '09:30', 'close': '19:00'}, {'day': 'Tuesday', 'open': '09:30', 'close': '19:00'}, {'day': 'Wednesday', 'open': '09:30', 'close': '19:00'}, {'day': 'Thursday', 'open': '09:30', 'close': '19:00'}, {'day': 'Friday', 'open': '09:30', 'close': '19:00'}, {'day': 'Saturday', 'open': '09:30', 'close': '19:00'}, {'day': 'Sunday', 'open': '10:00', 'close': '18:30'}]}}]

        # Check whether the result is right
        self.assertEqual(result, expected_result)

    def test_filter_by_price_free(self):
        city_filter = Filter(self.madrid_data, "madrid")
        target_price = "free"

        result = city_filter.filter_by_price(target_price)
        expected_result = [{'activity': 'Plaza Mayor', 'price': 0, 'rating': 4.6, 'wheelchair_accessible_entrance': False, 'hearing_accessibility': False, 'visual_accessibility': False, 'opening_hours': {'everyday': '24hs', 'specific_times': []}}, {'activity': 'El Retiro Park', 'price': 0, 'rating': 4.8, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': False, 'visual_accessibility': False, 'opening_hours': {'everyday': '24hs', 'specific_times': []}}, {'activity': 'Mercado de San Miguel', 'price': 0, 'rating': 4.4, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': False, 'visual_accessibility': False, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '10:00', 'close': '23:00'}, {'day': 'Tuesday', 'open': '10:00', 'close': '23:00'}, {'day': 'Wednesday', 'open': '10:00', 'close': '23:00'}, {'day': 'Thursday', 'open': '10:00', 'close': '23:00'}, {'day': 'Friday', 'open': '10:00', 'close': '23:59:59.9999999'}, {'day': 'Saturday', 'open': '10:00', 'close': '23:59:59.9999999'}, {'day': 'Sunday', 'open': '10:00', 'close': '23:00'}]}}, {'activity': 'Puerta de Alcala', 'price': 0, 'rating': 4.7, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': False, 'visual_accessibility': False, 'opening_hours': {'everyday': '24hs', 'specific_times': []}}]

        # Check whether the result is right
        self.assertEqual(result, expected_result)

    def test_filter_by_rating_4_star(self):
        city_filter = Filter(self.paris_data, "paris")

        result = city_filter.filter_by_rating(4)
        expected_result = [{'activity': 'Eiffel Tower', 'price': 16, 'rating': 4.7, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '09:00', 'close': '23:00'}, {'day': 'Tuesday', 'open': '09:00', 'close': '23:00'}, {'day': 'Wednesday', 'open': '09:00', 'close': '23:00'}, {'day': 'Thursday', 'open': '09:00', 'close': '23:00'}, {'day': 'Friday', 'open': '09:00', 'close': '23:00'}, {'day': 'Saturday', 'open': '09:00', 'close': '23:00'}, {'day': 'Sunday', 'open': '09:00', 'close': '23:00'}]}}, {'activity': 'Louvre Museum', 'price': 15, 'rating': 4.8, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '09:00', 'close': '18:00'}, {'day': 'Tuesday', 'open': '09:00', 'close': '21:45'}, {'day': 'Wednesday', 'open': '09:00', 'close': '21:45'}, {'day': 'Thursday', 'open': '09:00', 'close': '18:00'}, {'day': 'Friday', 'open': '09:00', 'close': '21:45'}, {'day': 'Saturday', 'open': '09:00', 'close': '18:00'}, {'day': 'Sunday', 'open': '09:00', 'close': '18:00'}]}}, {'activity': 'Notre-Dame Cathedral', 'price': 0, 'rating': 4.6, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': False, 'visual_accessibility': False, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '08:00', 'close': '18:45'}, {'day': 'Tuesday', 'open': '08:00', 'close': '18:45'}, {'day': 'Wednesday', 'open': '08:00', 'close': '18:45'}, {'day': 'Thursday', 'open': '08:00', 'close': '18:45'}, {'day': 'Friday', 'open': '08:00', 'close': '18:45'}, {'day': 'Saturday', 'open': '08:00', 'close': '18:45'}, {'day': 'Sunday', 'open': '08:00', 'close': '18:45'}]}}, {'activity': 'Mondaytmartre', 'price': 0, 'rating': 4.5, 'wheelchair_accessible_entrance': False, 'hearing_accessibility': False, 'visual_accessibility': False, 'opening_hours': {'everyday': '24hs', 'specific_times': []}}, {'activity': 'Seine River Cruise', 'price': 12, 'rating': 4.7, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '09:00', 'close': '23:00'}, {'day': 'Tuesday', 'open': '09:00', 'close': '23:00'}, {'day': 'Wednesday', 'open': '09:00', 'close': '23:00'}, {'day': 'Thursday', 'open': '09:00', 'close': '23:00'}, {'day': 'Friday', 'open': '09:00', 'close': '23:00'}, {'day': 'Saturday', 'open': '09:00', 'close': '23:00'}, {'day': 'Sunday', 'open': '09:00', 'close': '23:00'}]}}, {'activity': 'Versailles Palace', 'price': 20, 'rating': 4.6, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '09:00', 'close': '18:30'}, {'day': 'Tuesday', 'open': '09:00', 'close': '18:30'}, {'day': 'Wednesday', 'open': '09:00', 'close': '18:30'}, {'day': 'Thursday', 'open': '09:00', 'close': '18:30'}, {'day': 'Friday', 'open': '09:00', 'close': '18:30'}, {'day': 'Saturday', 'open': '09:00', 'close': '18:30'}, {'day': 'Sunday', 'open': '09:00', 'close': '18:30'}]}}, {'activity': 'Centre Pompidou', 'price': 14, 'rating': 4.5, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '11:00', 'close': '21:00'}, {'day': 'Tuesday', 'open': '11:00', 'close': '21:00'}, {'day': 'Wednesday', 'open': '11:00', 'close': '21:00'}, {'day': 'Thursday', 'open': '11:00', 'close': '21:00'}, {'day': 'Friday', 'open': '11:00', 'close': '21:00'}, {'day': 'Saturday', 'open': '11:00', 'close': '21:00'}, {'day': 'Sunday', 'open': '11:00', 'close': '21:00'}]}}]

        # Check whether the result is right
        self.assertEqual(result, expected_result)

    def test_filter_by_hearing_accessibility(self):
        city_filter = Filter(self.new_york_data, "new york")

        result = city_filter.filter_by_hearing_accessibility()
        expected_result = [{'activity': 'The Metropolitan Museum of Art', 'price': 25, 'rating': 4.9, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '10:00', 'close': '17:30'}, {'day': 'Tuesday', 'open': '10:00', 'close': '17:30'}, {'day': 'Wednesday', 'open': '10:00', 'close': '17:30'}, {'day': 'Thursday', 'open': '10:00', 'close': '17:30'}, {'day': 'Friday', 'open': '10:00', 'close': '21:00'}, {'day': 'Saturday', 'open': '10:00', 'close': '21:00'}, {'day': 'Sunday', 'open': '10:00', 'close': '17:30'}]}}, {'activity': 'Statue of Liberty', 'price': 20, 'rating': 4.6, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '08:30', 'close': '16:30'}, {'day': 'Tuesday', 'open': '08:30', 'close': '16:30'}, {'day': 'Wednesday', 'open': '08:30', 'close': '16:30'}, {'day': 'Thursday', 'open': '08:30', 'close': '16:30'}, {'day': 'Friday', 'open': '08:30', 'close': '16:30'}, {'day': 'Saturday', 'open': '08:30', 'close': '16:30'}, {'day': 'Sunday', 'open': '08:30', 'close': '16:30'}]}}, {'activity': 'Empire State Building', 'price': 38, 'rating': 4.5, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '10:00', 'close': '23:00'}, {'day': 'Tuesday', 'open': '10:00', 'close': '23:00'}, {'day': 'Wednesday', 'open': '10:00', 'close': '23:00'}, {'day': 'Thursday', 'open': '10:00', 'close': '23:00'}, {'day': 'Friday', 'open': '10:00', 'close': '23:00'}, {'day': 'Saturday', 'open': '10:00', 'close': '23:00'}, {'day': 'Sunday', 'open': '10:00', 'close': '23:00'}]}}, {'activity': 'Brooklyn Bridge', 'price': 0, 'rating': 4.7, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '24hs', 'specific_times': []}}, {'activity': 'Central Park Zoo', 'price': 14, 'rating': 4.4, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '10:00', 'close': '17:00'}, {'day': 'Tuesday', 'open': '10:00', 'close': '17:00'}, {'day': 'Wednesday', 'open': '10:00', 'close': '17:00'}, {'day': 'Thursday', 'open': '10:00', 'close': '17:00'}, {'day': 'Friday', 'open': '10:00', 'close': '17:00'}, {'day': 'Saturday', 'open': '10:00', 'close': '17:00'}, {'day': 'Sunday', 'open': '10:00', 'close': '17:00'}]}}]

        self.assertEqual(result, expected_result)

    def test_filter_by_future_opening_hours(self):
        city_filter = Filter(self.new_york_data, "new york")

        result = city_filter.filter_by_future_opening_hours("12/05/2023", "23:15")
        expected_result = [{'activity': 'Central Park', 'price': 0, 'rating': 4.8, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': False, 'visual_accessibility': False, 'opening_hours': {'everyday': '24hs', 'specific_times': []}}, {'activity': 'Times Square', 'price': 0, 'rating': 4.7, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': False, 'visual_accessibility': False, 'opening_hours': {'everyday': '24hs', 'specific_times': []}}, {'activity': 'Brooklyn Bridge', 'price': 0, 'rating': 4.7, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '24hs', 'specific_times': []}}]

        self.assertEqual(result, expected_result)

    def filter_by_hearing_accessibility(self):
        city_filter = Filter(self.new_york_data, "new york")

        result = city_filter.filter_by_hearing_accessibility()

        expected_result = [{'activity': 'The Metropolitan Museum of Art', 'price': 25, 'rating': 4.9, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '10:00', 'close': '17:30'}, {'day': 'Tuesday', 'open': '10:00', 'close': '17:30'}, {'day': 'Wednesday', 'open': '10:00', 'close': '17:30'}, {'day': 'Thursday', 'open': '10:00', 'close': '17:30'}, {'day': 'Friday', 'open': '10:00', 'close': '21:00'}, {'day': 'Saturday', 'open': '10:00', 'close': '21:00'}, {'day': 'Sunday', 'open': '10:00', 'close': '17:30'}]}}, {'activity': 'Statue of Liberty', 'price': 20, 'rating': 4.6, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '08:30', 'close': '16:30'}, {'day': 'Tuesday', 'open': '08:30', 'close': '16:30'}, {'day': 'Wednesday', 'open': '08:30', 'close': '16:30'}, {'day': 'Thursday', 'open': '08:30', 'close': '16:30'}, {'day': 'Friday', 'open': '08:30', 'close': '16:30'}, {'day': 'Saturday', 'open': '08:30', 'close': '16:30'}, {'day': 'Sunday', 'open': '08:30', 'close': '16:30'}]}}, {'activity': 'Empire State Building', 'price': 38, 'rating': 4.5, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '10:00', 'close': '23:00'}, {'day': 'Tuesday', 'open': '10:00', 'close': '23:00'}, {'day': 'Wednesday', 'open': '10:00', 'close': '23:00'}, {'day': 'Thursday', 'open': '10:00', 'close': '23:00'}, {'day': 'Friday', 'open': '10:00', 'close': '23:00'}, {'day': 'Saturday', 'open': '10:00', 'close': '23:00'}, {'day': 'Sunday', 'open': '10:00', 'close': '23:00'}]}}, {'activity': 'Brooklyn Bridge', 'price': 0, 'rating': 4.7, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '24hs', 'specific_times': []}}, {'activity': 'Central Park Zoo', 'price': 14, 'rating': 4.4, 'wheelchair_accessible_entrance': True, 'hearing_accessibility': True, 'visual_accessibility': True, 'opening_hours': {'everyday': '', 'specific_times': [{'day': 'Monday', 'open': '10:00', 'close': '17:00'}, {'day': 'Tuesday', 'open': '10:00', 'close': '17:00'}, {'day': 'Wednesday', 'open': '10:00', 'close': '17:00'}, {'day': 'Thursday', 'open': '10:00', 'close': '17:00'}, {'day': 'Friday', 'open': '10:00', 'close': '17:00'}, {'day': 'Saturday', 'open': '10:00', 'close': '17:00'}, {'day': 'Sunday', 'open': '10:00', 'close': '17:00'}]}}]

        self.assertEqual(result, expected_result)


    # EDGE CASES
    def test_filter_by_price_cheap(self):
        city_filter = Filter(self.madrid_data, "madrid")
        target_price = "cheap"

        result = city_filter.filter_by_price(target_price)
        expected_result = []

        # Check whether the result is right
        self.assertEqual(result, expected_result)

    def test_filter_by_price_expensive(self):
        city_filter = Filter(self.madrid_data, "madrid")
        target_price = "expensive"

        result = city_filter.filter_by_price(target_price)
        expected_result = []
        # Check whether the result is right
        self.assertEqual(result, expected_result)

    def test_filter_by_rating_1_stars(self):
        city_filter = Filter(self.paris_data, "paris")

        result = city_filter.filter_by_rating(1)
        expected_result = []
        # Check whether the result is right
        self.assertEqual(result, expected_result)

    # INVALID CASES
    # Not functioning properly. It doesn't recognise the error raised
    def test_filter_by_rating_6_stars(self):
        city_filter = Filter(self.paris_data, "paris")
        result = city_filter.filter_by_rating(6)
        self.assertEqual(result, "The rating requested is not in the range of 1-5 stars")
        # with self.assertRaises(RatingHigherThan5Stars):
        #     city_filter.filter_by_rating(6)
    def test_filter_by_price_really_cheap(self):
        city_filter = Filter(self.new_york_data, "new york")
        result = city_filter.filter_by_price("really cheap")
        self.assertEqual(result, "The price requested is not possible. It can only be free, cheap, medium or expensive ")
        # with self.assertRaises(PriceNotInOptions):
        #     city_filter.filter_by_price("really cheap")





if __name__ == '__main__':
    unittest.main()
