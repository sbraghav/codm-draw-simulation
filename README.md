# COD Mobile Lucky Draw : Monte Carlo Simulation

The python code reads odds of the various items in the lucky draw from the CSV file. It continues to play the draw the action till the intended item (Legendary Weapon) is received.

The although the items are different for each draw, the odds continue to be the same across the draws. We try to simulate the draw 10,000 times and determine how much percentage of players (out of 10,000) receive the draw in each of the turns.

The results of the simulation can be used as a aid for decision making. A snapshot of the simulation is obtained as



![image](https://user-images.githubusercontent.com/22560048/116670671-a2318700-a9bd-11eb-8fba-ce5add8afa13.png)

## How to Run

1. **Install Python**: Make sure Python 3.x is installed on your system.
2. **Install required packages**: Run `pip install -r requirements.txt` in your project directory.
3. **Run the simulation**: Execute `python lucky_draw.py` from the command line in the project folder.
4. **Customize draw settings**: To change the cost or probability of each item, edit the values in `Primeveal_redux.csv`. The simulation will use the updated values on the next run.


