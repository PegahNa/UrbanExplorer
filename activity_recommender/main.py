import json
from activities.search import Filter
import inspect
# *** import login


class main:
    # Get data from JSON file
    def __init__(self):
        # *** Change to relative path. It doesn't work for me, don't know why, but I have to use absolute paths for it to work
        with open('C:/Users/Fabiana/Downloads/CFG degree/Group-1-activity-recommender/data/locations.json') as json_file:
            self.data = json.load(json_file)

    # *** Here should come the login process

    """
    Filters data for each city
    
    :param city_name: The name of the city that you want to filter (your holiday destination)
    :param filter_chosen: The method that user chooses to filter those activities (e.g. by price, rating, opening hours, etc)
    :param *args: Arguments to be passed (if necessary) to the filter methods
    """
    def recommend_activities(self, city_name, filter_chosen, *args):
        # Getting the data from a specific city (e.g. Madrid)
        city_data = self.data.get(city_name.lower())

        # *** This should be an error to be caught
        if city_data is None:
            return "City not found"

        # Creating an instance of Filter class using the data from a specific city
        city_filter = Filter(city_data)

        # Get the name of the method you want to apply.
        # You retrieve the method filter_chosen from the object city_filter
        filter_method = getattr(city_filter, filter_chosen)

        # Where the filtered activities, after the method has been applied, will be stored
        filtered_results = []

        # Count how many parameters the method needs
        args_count = len(inspect.signature(filter_method).parameters)

        # If the method needs no arguments, append the activities to filtered_results
        if args_count == 0:
            filtered_results.append(filter_method())
        # If the number of arguments needed is the same as the arguments passed, append those results
        elif args_count == len(args):
            filtered_results.append(filter_method(*args))
        else:
            # *** This should be an error to be caught
            return "Incorrect number of filters"

        return filtered_results


if __name__ == "__main__":
    recommender = main()

    # city_name, filter_chosen and parameter are the parameter that we'll pass to recommender.recommend_activities
    # Here they're specified. But for it to work properly in the program, they need to be inputted by user.
    # city_name is already obtained by input as an example of how it should work
    # *** change filter_chosen and parameter to inputs
    city_name = input("What city do you want to go to? \n").lower()
    filter_chosen = "filter_by_future_opening_hours"
    parameter = ["12/05/2023", "23:50"]

    # This calls the method recommend_activities from main, so it can return the activities recommended
    recommendations = recommender.recommend_activities(city_name, filter_chosen, *parameter)

    # Print all the activities that have been filtered
    for result in recommendations:
        print(result)
