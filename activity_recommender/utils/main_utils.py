
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