import bcrypt
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
