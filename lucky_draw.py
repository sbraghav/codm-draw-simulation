# problem statement : Monte Carlo Simulation to estimate odds in COD Mobile Draws
import random
import csv
import copy
import numpy

READ_MODE = 'r'
odds = "Odds"
iterations = 10000

draw_cost = [10, 30, 50, 120, 200, 320, 520, 800, 1100, 1400]
costArray = []
turnArray = []

#helper functions

def getDrawDict(fileLocation):
    with open(fileLocation, mode=READ_MODE) as csv_file:
        items_array = []
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            items_array.append(row)
    return items_array


def random_draw(items_array):
    rand_number = random.random()
    sum = 0
    for item in items_array:
        sum = sum + float(item[odds])
        if(sum > rand_number):
            return item


def redistributeOdds(items_array, chosen_odd):
    for item in items_array:
        item[odds] = float(item[odds])/(1 - float(chosen_odd))
    return

#monte carlo simulation

parsed_items_array = getDrawDict("Primeveal_redux.csv")

for x in range(iterations):
    items_array = copy.deepcopy(parsed_items_array)
    cost = 0
    turn = 0
    while(len(items_array) > 0):
        chosen_item = random_draw(items_array)
        cost = cost + draw_cost[turn]
        turn = turn + 1
        if(chosen_item["Rarity"] == "Legendary" and chosen_item["Type"] == "Weapon"):
            costArray.append(cost)
            turnArray.append(turn)
            break
        chosen_odd = chosen_item[odds]
        items_array.remove(chosen_item)
        redistributeOdds(items_array, chosen_odd)
print(numpy.mean(costArray))
print(numpy.histogram(turnArray, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
