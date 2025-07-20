# problem statement : Monte Carlo Simulation to estimate odds in COD Mobile Draws
import random
import csv
import copy
import numpy
from tabulate import tabulate

READ_MODE = 'r'
odds = "Odds"
iterations = 10000

draw_cost = [10, 30, 50, 120, 200, 320, 520, 800, 1100, 1400]
costArray = []
turnArray = []

def getDrawDict(fileLocation):
    with open(fileLocation, mode=READ_MODE) as csv_file:
        return [row for row in csv.DictReader(csv_file)]

def random_draw(items_array):
    rand_number = random.random()
    sum_odds = 0
    for item in items_array:
        sum_odds += float(item[odds])
        if sum_odds > rand_number:
            return item

def redistributeOdds(items_array, chosen_odd):
    for item in items_array:
        item[odds] = float(item[odds]) / (1 - float(chosen_odd))

parsed_items_array = getDrawDict("Primeveal_redux.csv")

for _ in range(iterations):
    items_array = copy.deepcopy(parsed_items_array)
    cost = 0
    turn = 0
    while items_array:
        chosen_item = random_draw(items_array)
        cost += draw_cost[turn]
        turn += 1
        if chosen_item["Rarity"] == "Legendary" and chosen_item["Type"] == "Weapon":
            costArray.append(cost)
            turnArray.append(turn)
            break
        chosen_odd = chosen_item[odds]
        items_array.remove(chosen_item)
        redistributeOdds(items_array, chosen_odd)

# Print summary statistics for turns
print("Cost statistics:")
summary = [
    ["Min", min(costArray)],
    ["Max", max(costArray)],
    ["Mean", round(numpy.mean(costArray), 2)],
    ["Median", numpy.median(costArray)],
]
print(tabulate(summary, headers=["Statistic", "Value"], tablefmt="grid"))

# If you want to see a frequency table for turns:
from collections import Counter
turn_counts = Counter(turnArray)
freq_table = [[turn, count] for turn, count in sorted(turn_counts.items())]
print("\nTurn Frequency Table:")
print(tabulate(freq_table, headers=["Turns", "Frequency"], tablefmt="grid"))