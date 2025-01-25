# TOPSIS

This script calculates the **TOPSIS** (Technique for Order Preference by Similarity to Ideal Solution) score and ranks alternatives based on the provided decision matrix, weights, and impacts. It uses the weights and impacts to determine the ideal best and worst values, then calculates the distance of each alternative from these values to derive the final score and ranking.

## Installation

There are no external dependencies, but you need to have **Python** and **pandas** installed to run the script.

```pip install 102203836_topsis```

## How to use it?
### Step 1: Prepare the Data
The input data should be a CSV file containing the following columns:

The first column should contain the fund names.
The remaining columns should contain the criteria values for each alternative (row).
Example CSV format:

Fund Name,P1,P2,P3,P4,P5
M1,0.67,0.45,6.3,38.2,11.41
M2,0.81,0.66,6,42.4,12.47
M3,0.68,0.46,3,60.2,16.09

### Step 2: Run the Script
To run the script, use the following command in the terminal:

python <your-script-name>.py <input-file> <weights> <impacts> <output-file>
Example:
python topsis.py data.csv "1,1,1,2,1" "+,+,-,+,-" results.csv
Where:
<your-script-name>.py is the name of the script file (e.g., topsis.py).
<input-file> is your input CSV file (e.g., data.csv).
<weights> is a comma-separated string of weights for each criterion (e.g., "1,1,1,2,1").
<impacts> is a comma-separated string of impacts for each criterion (e.g., "+,+,-,+,-").
<output-file> is the file where the results will be saved (e.g., results.csv).

### Step 3: Output
The output will be a CSV file with the calculated TOPSIS scores and ranks for each alternative.
...