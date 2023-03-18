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

    # for item in response[0]:
    #     extra_info = {
    #         "fat_total_g": item[0],
    #         "fat_saturated_g": item[1],
    #         "protein_g": item[2],
    #         "sodium_mg": item[3],
    #         "potassium_mg": item[4],
    #         "cholesterol_mg": item[5],
    #         "carbohydrates_total_g": item[6],
    #         "fiber_g": item[7],
    #         "sugar_g": item[8]
    #     }

    return response[0]
