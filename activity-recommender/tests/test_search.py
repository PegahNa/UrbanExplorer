import json
import unittest
from ..activities.search import Filter, RatingHigherThan5Stars



class TestFilter(unittest.TestCase):
    # It'll run its code before every single test
    def setUp(self):
        # It'll mock the data from all the cities in the JSON file
        self.madrid_data = [
            {
                "activity": "Plaza Mayor",
                "price": 0,
                "rating": 4.6,
                "wheelchair_accessible_entrance": True,
                "hearing_accessibility": False,
                "visual_accessibility": False,
                "opening_hours": "24hs",
                "current_opening_hours": "open_now"
            },
            {
                "activity": "El Retiro Park",
                "price": 0,
                "rating": 4.8,
                "wheelchair_accessible_entrance": True,
                "hearing_accessibility": False,
                "visual_accessibility": False,
                "opening_hours": "24hs",
                "current_opening_hours": "open_now"
            },
            {
                "activity": "Museo nacional del Prado",
                "price": 15,
                "rating": 4.7,
                "wheelchair_accessible_entrance": True,
                "hearing_accessibility": True,
                "visual_accessibility": True,
                "opening_hours": "mon-sat 10:00-20:00, sun 10:00-19:00",
                "current_opening_hours": "open_now"
            },
            {
                "activity": "Royal Palace of Madrid",
                "price": 12,
                "rating": 4.6,
                "wheelchair_accessible_entrance": True,
                "hearing_accessibility": True,
                "visual_accessibility": True,
                "opening_hours": "mon-sat 10:00-19:00, sun 10:00-16:00",
                "current_opening_hours": "open_now"
            },
            {
                "activity": "Santiago Bernabeu Stadium",
                "price": 15,
                "rating": 4.6,
                "wheelchair_accessible_entrance": True,
                "hearing_accessibility": False,
                "visual_accessibility": False,
                "opening_hours": "mon-sat 9:30-19:00, sun 10:00-18:30",
                "current_opening_hours": "open_now"
            },
            {
                "activity": "Mercado de San Miguel",
                "price": 0,
                "rating": 4.4,
                "wheelchair_accessible_entrance": True,
                "hearing_accessibility": False,
                "visual_accessibility": False,
                "opening_hours": "sun-thu 10:00-00:00, fri-sat 10:00-01:00",
                "current_opening_hours": "open_now"
            },
            {
                "activity": "Puerta de Alcala",
                "price": 0,
                "rating": 4.7,
                "wheelchair_accessible_entrance": True,
                "hearing_accessibility": False,
                "visual_accessibility": False,
                "opening_hours": "24hs",
                "current_opening_hours": "open_now"
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
              "opening_hours": "daily 9:00-00:45",
              "current_opening_hours": "open_now"
            },
            {
              "activity": "Louvre Museum",
              "price": 15,
              "rating": 4.8,
              "wheelchair_accessible_entrance": True,
              "hearing_accessibility": True,
              "visual_accessibility": True,
              "opening_hours": "mon, thu, sat, sun 9:00-18:00, wed, fri 9:00-21:45",
              "current_opening_hours": "open_now"
            },
            {
              "activity": "Notre-Dame Cathedral",
              "price": 0,
              "rating": 4.6,
              "wheelchair_accessible_entrance": True,
              "hearing_accessibility": False,
              "visual_accessibility": False,
              "opening_hours": "daily 8:00-18:45",
              "current_opening_hours": "open_now"
            },
            {
              "activity": "Montmartre",
              "price": 0,
              "rating": 4.5,
              "wheelchair_accessible_entrance": False,
              "hearing_accessibility": False,
              "visual_accessibility": False,
              "opening_hours": "24hs",
              "current_opening_hours": "open_now"
            },
            {
              "activity": "Seine River Cruise",
              "price": 12,
              "rating": 4.7,
              "wheelchair_accessible_entrance": True,
              "hearing_accessibility": True,
              "visual_accessibility": True,
              "opening_hours": "daily 9:00-23:00",
              "current_opening_hours": "open_now"
            },
            {
              "activity": "Versailles Palace",
              "price": 20,
              "rating": 4.6,
              "wheelchair_accessible_entrance": True,
              "hearing_accessibility": True,
              "visual_accessibility": True,
              "opening_hours": "tue-sun 9:00-18:30",
              "current_opening_hours": "open_now"
            },
            {
              "activity": "Centre Pompidou",
              "price": 14,
              "rating": 4.5,
              "wheelchair_accessible_entrance": True,
              "hearing_accessibility": True,
              "visual_accessibility": True,
              "opening_hours": "wed-mon 11:00-21:00",
              "current_opening_hours": "open_now"
            }]


    # VALID CASES
    def test_filter_by_price_medium(self):
        city_filter = Filter(self.madrid_data)
        target_price = range(10,20)

        result = city_filter.filter_by_price(target_price)
        expected_result = [
    {
        "activity": "Museo nacional del Prado",
        "price": 15,
        "rating": 4.7,
        "wheelchair_accessible_entrance": True,
        "hearing_accessibility": True,
        "visual_accessibility": True,
        "opening_hours": "mon-sat 10:00-20:00, sun 10:00-19:00",
        "current_opening_hours": "open_now"
    },
    {
        "activity": "Royal Palace of Madrid",
        "price": 12,
        "rating": 4.6,
        "wheelchair_accessible_entrance": True,
        "hearing_accessibility": True,
        "visual_accessibility": True,
        "opening_hours": "mon-sat 10:00-19:00, sun 10:00-16:00",
        "current_opening_hours": "open_now"
    },
    {
        "activity": "Santiago Bernabeu Stadium",
        "price": 15,
        "rating": 4.6,
        "wheelchair_accessible_entrance": True,
        "hearing_accessibility": False,
        "visual_accessibility": False,
        "opening_hours": "mon-sat 9:30-19:00, sun 10:00-18:30",
        "current_opening_hours": "open_now"
    }
]
        # Check whether the result is right
        self.assertEqual(result, json.dumps(expected_result, indent=4))

    def test_filter_by_price_free(self):
        city_filter = Filter(self.madrid_data)
        target_price = [0]

        result = city_filter.filter_by_price(target_price)
        expected_result = [{
        "activity": "Plaza Mayor",
        "price": 0,
        "rating": 4.6,
        "wheelchair_accessible_entrance": True,
        "hearing_accessibility": False,
        "visual_accessibility": False,
        "opening_hours": "24hs",
        "current_opening_hours": "open_now"
    },
    {
        "activity": "El Retiro Park",
        "price": 0,
        "rating": 4.8,
        "wheelchair_accessible_entrance": True,
        "hearing_accessibility": False,
        "visual_accessibility": False,
        "opening_hours": "24hs",
        "current_opening_hours": "open_now"
    },
    {
        "activity": "Mercado de San Miguel",
        "price": 0,
        "rating": 4.4,
        "wheelchair_accessible_entrance": True,
        "hearing_accessibility": False,
        "visual_accessibility": False,
        "opening_hours": "sun-thu 10:00-00:00, fri-sat 10:00-01:00",
        "current_opening_hours": "open_now"
    },
    {
        "activity": "Puerta de Alcala",
        "price": 0,
        "rating": 4.7,
        "wheelchair_accessible_entrance": True,
        "hearing_accessibility": False,
        "visual_accessibility": False,
        "opening_hours": "24hs",
        "current_opening_hours": "open_now"
    }]
        # Check whether the result is right
        self.assertEqual(result, json.dumps(expected_result, indent=4))

    def test_filter_by_rating_4_star(self):
        city_filter = Filter(self.paris_data)
        target_rating = [4.0 + (x * 0.1)
             for x in range(0, 10)]

        result = city_filter.filter_by_rating(target_rating)
        expected_result = [{
            "activity": "Eiffel Tower",
            "price": 16,
            "rating": 4.7,
            "wheelchair_accessible_entrance": True,
            "hearing_accessibility": True,
            "visual_accessibility": True,
            "opening_hours": "daily 9:00-00:45",
            "current_opening_hours": "open_now"
        },
        {
            "activity": "Louvre Museum",
            "price": 15,
            "rating": 4.8,
            "wheelchair_accessible_entrance": True,
            "hearing_accessibility": True,
            "visual_accessibility": True,
            "opening_hours": "mon, thu, sat, sun 9:00-18:00, wed, fri 9:00-21:45",
            "current_opening_hours": "open_now"
        },
        {
            "activity": "Notre-Dame Cathedral",
            "price": 0,
            "rating": 4.6,
            "wheelchair_accessible_entrance": True,
            "hearing_accessibility": False,
            "visual_accessibility": False,
            "opening_hours": "daily 8:00-18:45",
            "current_opening_hours": "open_now"
        },
        {
            "activity": "Montmartre",
            "price": 0,
            "rating": 4.5,
            "wheelchair_accessible_entrance": False,
            "hearing_accessibility": False,
            "visual_accessibility": False,
            "opening_hours": "24hs",
            "current_opening_hours": "open_now"
        },
        {
            "activity": "Seine River Cruise",
            "price": 12,
            "rating": 4.7,
            "wheelchair_accessible_entrance": True,
            "hearing_accessibility": True,
            "visual_accessibility": True,
            "opening_hours": "daily 9:00-23:00",
            "current_opening_hours": "open_now"
        },
        {
            "activity": "Versailles Palace",
            "price": 20,
            "rating": 4.6,
            "wheelchair_accessible_entrance": True,
            "hearing_accessibility": True,
            "visual_accessibility": True,
            "opening_hours": "tue-sun 9:00-18:30",
            "current_opening_hours": "open_now"
        },
        {
            "activity": "Centre Pompidou",
            "price": 14,
            "rating": 4.5,
            "wheelchair_accessible_entrance": True,
            "hearing_accessibility": True,
            "visual_accessibility": True,
            "opening_hours": "wed-mon 11:00-21:00",
            "current_opening_hours": "open_now"
        }
    ]

        # Check whether the result is right
        self.assertEqual(result, json.dumps(expected_result, indent=4))

    # EDGE CASES
    def test_filter_by_price_cheap(self):
        city_filter = Filter(self.madrid_data)
        target_price = range(1, 10)

        result = city_filter.filter_by_price(target_price)
        expected_result = []

        # Check whether the result is right
        self.assertEqual(result, json.dumps(expected_result, indent=4))

    def test_filter_by_price_expensive(self):
        city_filter = Filter(self.madrid_data)
        target_price = range(20, 100)

        result = city_filter.filter_by_price(target_price)
        expected_result = []
        # Check whether the result is right
        self.assertEqual(result, json.dumps(expected_result, indent=4))

    def test_filter_by_rating_1_stars(self):
        city_filter = Filter(self.paris_data)
        target_rating = [1.0 + (x * 0.1)
             for x in range(0, 10)]

        result = city_filter.filter_by_price(target_rating)
        expected_result = []
        # Check whether the result is right
        self.assertEqual(result, json.dumps(expected_result, indent=4))

    # INVALID CASES
    # Not functioning properly. It doesn't recognise the error raised
    def test_filter_by_rating_6_stars(self):
        city_filter = Filter(self.paris_data)
        with self.assertRaises(RatingHigherThan5Stars):
            city_filter.filter_by_rating([6.0])



if __name__ == '__main__':
    unittest.main()
