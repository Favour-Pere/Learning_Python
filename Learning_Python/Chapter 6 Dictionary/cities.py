""". Cities: Make a dictionary called cities. Use the names of three cities as 
keys in your dictionary. Create a dictionary of information about each city and 
include the country that the city is in, its approximate population, and one fact 
about that city. The keys for each city’s dictionary should be something like 
country, population, and fact. Print the name of each city and all of the information you have stored about it.
"""

cities = {
    'london': {
        'country': 'united kingdom',
        'population': '8.982 million',
        'fact': 'The London Underground is the oldest underground railway network in the world.'
    },
    'paris': {
        'country': 'france',
        'population': '2.141 million',
        'fact': 'The Eiffel Tower was originally intended for Barcelona, Spain.'
    },
    'new york': {
        'country': 'united states',
        'population': '8.623 million',
        'fact': 'The New York Public Library has over 50 million books.'
    },
    'australia': {
        'country': 'australia',
        'population': '25.36 million',
        'fact': 'Australia is the only continent without an active volcano.'
    }
}

for city, city_info in cities.items():
    print("\nCity: " + city.title())
    print("\tCountry: " + city_info['country'].title())
    print("\tPopulation: " + city_info['population'])
    print("\tFact: " + city_info['fact'])
