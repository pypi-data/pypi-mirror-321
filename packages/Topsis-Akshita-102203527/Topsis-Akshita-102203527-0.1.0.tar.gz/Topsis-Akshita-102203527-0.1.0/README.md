TOPSIS Implementation in Python

Introduction

This Python script implements the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method for multi-criteria decision-making. It evaluates alternatives based on multiple criteria, considering their relative importance and impact.

Prerequisites
Python 3.x

Libraries:
pandas
numpy

Install the required libraries using the following command:
pip install pandas numpy

Files
102203527.py: The main Python script containing the TOPSIS implementation.
Input File: A CSV file containing the decision matrix.
Output File: A CSV file where the results will be saved.

Input File Format
The input file must be a CSV file with the following format:
First column: Names or identifiers of alternatives (e.g., A, B, C).
Remaining columns: Criteria values (numerical).

Example Input File (data.csv):

Command-Line Usage
The script requires four command-line arguments:
python 102203527.py <InputFile> <Weights> <Impacts> <ResultFile>

Arguments:
<InputFile>: Path to the input CSV file (e.g., data.csv).
<Weights>: Comma-separated weights for each criterion (e.g., 1,1,1,1).
<Impacts>: Comma-separated impacts for each criterion (+ for beneficial, - for non-beneficial).
<ResultFile>: Path to the output CSV file (e.g., result.csv).

Example Command:
python 102203527.py data.csv "1,1,1,1" "+,-,+,+" result.csv

Output File Format
The output file will be a CSV file containing the input data with two additional columns:
Topsis Score: The calculated score for each alternative.
Rank: The rank of each alternative based on the TOPSIS score.

Example Output File
Alternatives,Criterion1,Criterion2,Criterion3,Criterion4,Topsis Score,Rank
A,20,300,50,0.5,0.78,2
B,25,250,60,0.7,0.85,1
C,30,200,70,0.4,0.63,3

Error Handling

Common Errors:
Invalid Input File:
Ensure the file exists and follows the correct format.
Error: File '<InputFile>' not found.

Insufficient Columns:
Ensure the file contains at least three columns (one for alternatives and two for criteria).
Error: Input file must contain at least three columns.
Mismatch in Weights or Impacts:
Ensure the number of weights and impacts matches the number of criteria columns.

Error: Number of weights and impacts must match the number of criteria columns.
Invalid Impacts:
Ensure impacts are either + or -.
Error: Impacts must be '+' or '-'.

Explanation of the TOPSIS Method

Input Normalization:
Normalize the decision matrix using:

Weight Assignment:
Multiply each normalized value by its respective weight.

Determine Ideal Best and Worst Values:
For beneficial criteria (+), the ideal best is the maximum value, and the ideal worst is the minimum value.
For non-beneficial criteria (-), the ideal best is the minimum value, and the ideal worst is the maximum value.

Calculate Distances:
Compute the Euclidean distance from the ideal best and worst values.

Calculate TOPSIS Score:
Compute the relative closeness to the ideal solution:

Ranking:
Rank the alternatives based on their scores in descending order.

