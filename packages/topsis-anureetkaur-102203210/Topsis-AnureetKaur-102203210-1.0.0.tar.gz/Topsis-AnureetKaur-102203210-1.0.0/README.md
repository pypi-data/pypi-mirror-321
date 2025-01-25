# TOPSIS Implementation in Python

This repository contains a Python implementation of the **Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)**, a multi-criteria decision-making (MCDM) method. TOPSIS is used to rank and evaluate alternatives based on multiple criteria, considering both their closeness to an ideal solution and their distance from a nadir (worst-case) solution.

## Features
- Accepts input data from a CSV file for analysis.
- Normalizes numerical data using vector normalization.
- Applies user-defined weights and impacts (`+` for benefit criteria, `-` for cost criteria) to compute the weighted normalized decision matrix.
- Calculates ideal and anti-ideal solutions and their respective distances for each alternative.
- Computes the TOPSIS score and assigns ranks to alternatives.
- Outputs results including TOPSIS scores and ranks in a CSV file.

## Installation
Clone the repository and install the required Python libraries:
```bash
pip install pandas numpy scipy

