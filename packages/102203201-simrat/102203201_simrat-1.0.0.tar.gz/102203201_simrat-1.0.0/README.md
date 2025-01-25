# TOPSIS-Package Simrat(102203201)

Overview
TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision-making (MCDM) technique. This Python package helps you evaluate alternatives based on multiple criteria by calculating the TOPSIS score and ranking them accordingly.

With this package, you can:

1. Input your dataset in CSV format.
2. Specify weights for each criterion.
3. Define whether each criterion is beneficial (+) or non-beneficial (-).
4. Obtain a ranked CSV file as output with TOPSIS scores.

# Installation

Install the package using
` pip install 102203201-simrat`

# Input Parameters

1. Input CSV File: Path to your dataset in CSV format.
   The dataset must have at least three columns:
   The first column should contain the names of the alternatives.
   The subsequent columns should contain numeric values for criteria.
2. Weights: Comma-separated numeric values representing the weight of each criterion.
3. Impacts: Comma-separated values (+ or -) indicating whether each criterion is beneficial (+) or non-beneficial (-).
4. Output CSV File Name: Desired file name for the output CSV containing TOPSIS scores and rankings.

## License

Copyright (c) 2024 Simrat Kaur

This package is licensed under the MIT License.
