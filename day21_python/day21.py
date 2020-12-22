import sys
import re


if __name__ == '__main__':
    input_content = sys.stdin.read()
    foods = [[(f[0].split(' '), f[1].split(', ')) for f in re.findall(r'(.+?) \(contains (.+?)\)', line)][0] for line in input_content.split('\n')]
    ingredients_all = [item for sublist in foods for item in sublist[0]]
    ingredients = list(set(ingredients_all))
    allergens = list(set([item for sublist in foods for item in sublist[1]]))

    allergens_food = {}

    for i in range(len(allergens)):
        for allergen in allergens:

            integredients_intersect = [item for item in ingredients if item not in allergens_food.values()]
            for food in foods:
                food_ingredients, food_allergens = food
                if allergen in food_allergens:
                    integredients_intersect = list(set(integredients_intersect) & set(food_ingredients))

            if len(integredients_intersect) == 1:
                allergens_food[allergen] = integredients_intersect[0]

    print(len([item for item in ingredients_all if item not in allergens_food.values()]))