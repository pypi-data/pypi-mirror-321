# Topsis-Devit-102217044

## Description

This project is a Python implementation of the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method, which is widely used for decision-making problems. TOPSIS helps to evaluate and rank alternatives based on multiple criteria, determining how close each alternative is to the ideal solution.

## Features

- Takes input data as a CSV file.
- Accepts weights for each criterion.
- Allows specification of impacts for each criterion (positive or negative).
- Computes the TOPSIS score and ranks the alternatives.
- Outputs the results into a CSV file with ranks and scores.

## Installation

You can install this package using `pip`:

```bash
pip install topsis-devit-102217044

#Once installed, you can use the TOPSIS method as follows:

from topsis import topsis

# Example data
input_file = 'data.csv'
weights = '1,1,2,2'  # Comma-separated weights for each criterion
impacts = '+,+,-,+,+'   # Comma-separated impacts for each criterion ('+' for benefit, '-' for cost)
result_file = 'result.csv'

topsis(input_file, weights, impacts, result_file)

## Requirements
pip install pandas numpy

###For creating python package
 pip install build
 python -m build

 ##To upload in pypi site
 pip install twine
 twine upload dist/* 
 #enter the token accesing from pypi site after login and authenticator from authenticator app the you can add token for specific project
## Validation
python>=3.6



