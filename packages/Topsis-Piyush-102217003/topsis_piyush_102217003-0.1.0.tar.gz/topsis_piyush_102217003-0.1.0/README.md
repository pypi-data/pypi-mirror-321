# Topsis-Piyush-102217003

[![PyPI version](https://badge.fury.io/py/102217003_piyush_garg.svg)](https://pypi.org/project/102217003_piyush_garg/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A Python package for implementing the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)**, a multi-criteria decision-making method.

---

## Installation

Install the package from PyPI:

```bash
pip install Topsis-Piyush-102217003
```
## Usage

### Input
The package expects a CSV file with the following structure:

The first row contains column headers.
The first column contains alternative names.
The subsequent columns contain numerical values for different criteria.
Output
The result will include the following:

Topsis Score: A score for each alternative.
Rank: Ranking of the alternatives based on the score.

### Explanation of Parameters:
"data.csv": Input CSV file path.
"1,1,1": Weights for each criterion.
"+,+,-": Impact of each criterion (+ for beneficial, - for non-beneficial).
"result.csv": Output CSV file path.

### Features
Handles both beneficial and non-beneficial criteria.
Scalable to multiple alternatives and criteria.
Provides normalized scores for accurate decision-making.

### Dependencies
Ensure you have the following Python libraries installed (they will be auto-installed via pip):

numpy
pandas

### Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Submit a pull request.

### Acknowledgments
Inspired by the Topsis method for decision-making.
Developed by Piyush Garg.