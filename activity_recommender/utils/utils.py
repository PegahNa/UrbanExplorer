
# Functions used in search.py

# Function that returns a range of ratings
def get_range_of_ratings(target_rating):
    if target_rating == 0:
        return [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    if target_rating == 1:
        return [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
    if target_rating == 2:
        return [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9]
    if target_rating == 3:
        return [3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9]
    if target_rating == 4:
        return [4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9]
    if target_rating == 5:
        return [5]

# Function that returns a range of prices
def get_range_of_prices(target_price):
    if target_price == "cheap":
        return range(1, 10)
    elif target_price == "medium":
        return range(10, 20)
    elif target_price == "expensive":
        return range(20, 100)
    elif target_price == "free":
        return [0]

def euro_or_dollars(city):
    if city == "new york":
        return "$"
    elif city == "madrid" or city == "paris":
        return "€"


# Functions used in main.py

def print_filters_used(filters_applied):
    filters = []
    for filter in filters_applied:
        if "filter_by_price()" in filter:
            filters.append(f"Price --> {filter['filter_by_price()']}")
        if "filter_by_rating()" in filter:
            filters.append(f"Rating --> {filter['filter_by_rating()']}")
        if "filter_by_wheelchair_accessible_entrance()" in filter:
            filters.append("Wheelchair accessible entrance")
        if "filter_by_hearing_accessibility()" in filter:
            filters.append("Hearing accessibility")
        if "filter_by_visual_accessibility()" in filter:
            filters.append("Visual accessibility")
        if "filter_by_current_opening_hours()" in filter:
            filters.append("Current opening hours")
        if "filter_by_future_opening_hours()" in filter:
            filters.append(f"Future opening hours --> {filter['filter_by_future_opening_hours()']}")
    return filters


def get_filter_from_numbers(number_chosen):
    methods = []
    for number in number_chosen:
        if number == "1":
            methods.append("search_by_price")
        if number == "2":
            methods.append("search_by_rating")
        if number == "3":
            methods.append("search_by_accessibility")
        if number == "4":
            methods.append("search_by_opening_hours")
    return methods


#print(get_filter_from_numbers(["1", "2", "3"]))