import requests

api_key = 'z44aAu03gKIdAq8/LJpKKA==4X3UsxPNyJ9qAmNT'

# Get Food Calories From API
def get_calories(food_item, amount):
    query = amount + " " + food_item

    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': api_key}).json()

    calories = str(response[0]['calories'])

    return calories


# Get More Food Information From API
def get_more_info(food_item, amount):
    query = amount + " " + food_item

    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': api_key}).json()

    return response[0]
