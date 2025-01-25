
# TOPSIS Package



## Overview

The *TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)* method is a multi-criteria decision analysis (MCDA) technique used to evaluate and rank alternatives based on multiple criteria. This Python package provides a simple implementation of the TOPSIS method.

## Features

- Easy to use function to perform the TOPSIS method on decision matrices.
- Accepts customizable weights for each criterion.
- Supports both beneficial and non-beneficial criteria (impacts).
- Returns preference scores and ranks for the alternatives.

    Parameters:
        data (list of lists): Decision matrix (alternatives x criteria).
        weights (list): List of weights for each criterion.
        impacts (list): '+' for beneficial, '-' for non-beneficial criteria.

    Returns:
        list: Preference scores for each alternative.
        list: Ranks of each alternative.

## Installation

You can install the *Topsis Package* using pip from PyPI.

### From PyPI:

Install the package using pip:
```bash
pip install 102217109_topsis
```
