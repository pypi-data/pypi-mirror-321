Multi-Criteria Decision Making with TOPSIS

Overview
This repository contains a Python-based implementation of the TOPSIS decision-making methodology (Technique for Order of Preference by Similarity to Ideal Solution). The tool helps evaluate and rank different options based on multiple decision criteria while considering their relative significance.

System Requirements
- Python 3.x environment
- Required packages:
  pandas
  numpy

To set up the dependencies:
pip install pandas numpy

File Structure
- Main script: 102203557.py
- Required input: CSV format decision matrix
- Generated output: CSV file with rankings

Input Data Requirements
Your input CSV file should be structured as follows:
- Column 1: Alternative identifiers
- Columns 2+: Numerical values for each criterion

Sample input format (input.csv):
Alternative,Metric1,Metric2,Metric3,Metric4
Option1,20,300,50,0.5
Option2,25,250,60,0.7

Running the Program
Execute the script using the following syntax:
python 102203557.py input_file weights impacts output_file

Parameters:
- input_file: Path to your input CSV
- weights: Criterion weights (comma-separated)
- impacts: Criterion types (+ for maximization, - for minimization)
- output_file: Desired location for results

Example:
python 102203557.py input.csv "1,1,1,1" "+,-,+,+" results.csv

Results Format
The output CSV includes:
- All original input data
- TOPSIS score column
- Final ranking column

Sample output structure:
Alternative,Metric1,Metric2,Metric3,Metric4,TOPSIS_Score,Rank
Option1,20,300,50,0.5,0.78,2
Option2,25,250,60,0.7,0.85,1

Error Management
The program includes validation for:
1. File existence and accessibility
2. Data format requirements
3. Input parameter consistency
4. Valid impact indicators

Common error messages:
- "Unable to locate specified input file"
- "Input data must contain 3+ columns"
- "Weight/impact count must match criterion count"
- "Impact values limited to '+' or '-'"
