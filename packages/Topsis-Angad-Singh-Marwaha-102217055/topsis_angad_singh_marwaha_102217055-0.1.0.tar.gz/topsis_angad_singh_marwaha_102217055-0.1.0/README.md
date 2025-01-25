
TOPSIS Implementation in Python

Overview
This Python script implements TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution), a multi-criteria decision-making method to rank alternatives based on criteria weights and impacts.

Requirements
- Python 3.x
- Libraries: Install via  
  pip install pandas numpy

Files
1. `102217055.py`: Main Python script.  
2. Input File: CSV containing alternatives and criteria.  
3. Output File: CSV with calculated scores and ranks.

Input Format
- First Column: Alternative names (e.g., A, B, C).  
- Other Columns: Numerical criteria values.  

Example (data.csv):
Alternatives,Criterion1,Criterion2,Criterion3
A,20,300,50
B,25,250,60
C,30,200,70

Usage
Run the script with:
python 102217055.py <InputFile> <Weights> <Impacts> <ResultFile>

Arguments:
1. <InputFile>: Path to input CSV.  
2. <Weights>: Comma-separated weights (e.g., 1,1,1).  
3. <Impacts>: Comma-separated impacts (+ for beneficial, - for non-beneficial).  
4. <ResultFile>: Path to save output CSV.

Example:
python 102217055.py data.csv "1,1,1" "+,+,-" result.csv

Output Format
The output CSV includes the input data with:  
- Topsis Score: Calculated score for each alternative.  
- Rank: Based on TOPSIS score.

Example (result.csv):
Alternatives,Criterion1,Criterion2,Criterion3,Topsis Score,Rank
A,20,300,50,0.78,2
B,25,250,60,0.85,1
C,30,200,70,0.63,3

Error Handling
1. File Errors: Ensure the input file exists and is correctly formatted.  
2. Mismatch in Weights/Impacts: Ensure their count matches the criteria columns.  
3. Invalid Impacts: Use only + or -.

Method Overview
1. Normalize: Scale values for comparability.  
2. Weighting: Apply weights to normalized values.  
3. Ideal Values: Determine best and worst values for criteria.  
4. Distance Calculation: Measure distances from ideal best/worst.  
5. Score & Rank: Compute scores and rank alternatives.

This script simplifies multi-criteria decision-making. Reach out for support if needed!
