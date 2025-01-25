# TOPSIS Implementation

This Python script implements the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)**, a multi-criteria decision-making method. It evaluates and ranks alternatives based on multiple criteria, considering weights and impacts.

## Requirements

Before running the script, ensure you have Python installed along with the following libraries:
- `pandas`
- `numpy`

To install the required libraries, run:
```bash
pip install pandas numpy
 
Usage
The script is executed from the command line and requires the following inputs:
python topsis.py <InputFile> <Weights> <Impacts> <ResultFile>


Arguments:
InputFile: Path to the CSV file containing the dataset.

The first column should have the names/identifiers of alternatives.
The subsequent columns should contain numeric values representing the criteria.
Weights: Comma-separated weights for each criterion (e.g., 1,2,3).

Impacts: Comma-separated impacts for each criterion (+ for beneficial and - for non-beneficial). Example: +, -, +.

ResultFile: Path to save the output CSV file containing the TOPSIS scores and ranks.

Example
Input Data
Alternative,Criteria1,Criteria2,Criteria3
A1,250,16,12
A2,200,20,8
A3,300,12,16
A4,275,15,11
 
Command:
python topsis.py example.csv 0.5,0.3,0.2 +,+,- result.csv

Output Data (result.csv):
Alternative,Criteria1,Criteria2,Criteria3,Topsis Score,Rank
A1,250,16,12,0.7742,1
A2,200,20,8,0.4268,4
A3,300,12,16,0.6423,2
A4,275,15,11,0.5797,3

Steps in the Script
Data Loading:

Reads the input file and validates that it has at least three columns.
Validation:

Checks if the number of weights and impacts match the number of criteria.
Ensures impacts are either + or -.
Normalization:

Normalizes the criteria values using vector normalization.
Weighted Matrix Calculation:

Multiplies normalized values by their respective weights.
Ideal Values:

Determines the ideal best and worst values based on the impacts.
Score Calculation:

Computes TOPSIS scores using distances to the ideal best and worst values.
Ranking:

Assigns ranks based on the scores (higher scores are better).
Output:

Saves the results (scores and ranks) to the specified output file.
Error Handling


File Not Found:
If the input file does not exist, the script exits with an error message.

Validation Errors:
If the weights/impacts do not match the number of criteria, or if impacts are invalid, appropriate error messages are displayed.

General Errors:
Any other unexpected errors during execution are caught and displayed.

Notes
The first column of the input file is treated as the identifier for alternatives.
Ensure all criteria columns contain numeric values.
Weights must be positive real numbers, and impacts must be + or -.

License
This script is open-source and can be used, modified, and distributed freely.