""" Imported Restaurant: Using your latest Restaurant class, store it in a module.
 Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working properly."""

import resturant

ed_spring = resturant.Restaurant('Ed Spring', 'Ice Cream')
ed_spring.describe_restaurant()
ed_spring.open_restaurant()
