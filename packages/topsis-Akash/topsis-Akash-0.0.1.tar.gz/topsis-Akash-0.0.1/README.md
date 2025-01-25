# TOPSIS Akash Package

## Overview

The **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method is a multi-criteria decision-making tool. This Python package allows you to implement the TOPSIS method for ranking and selecting alternatives based on multiple criteria.

## How to Use

Run the program through command line as:
Usages: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>
Example: python 101556.py 101556-data.csv “1,1,1,2” “+,+,-,+” 101556-result.csv


## Features

- Input data validation
- Weighted normalization of the decision matrix
- Calculation of ideal best and worst solutions
- Ranking alternatives based on their similarity to the ideal solution
- Supports command-line execution

---

## Installation

Install the package using `pip`:

```bash
pip install topsis-akash
