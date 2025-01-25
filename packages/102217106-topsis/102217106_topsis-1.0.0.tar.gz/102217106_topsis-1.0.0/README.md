
# TOPSIS Package



## Overview

The TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method is a widely used multi-criteria decision analysis (MCDA) technique designed to evaluate and rank alternatives based on multiple criteria. This Python package offers a straightforward implementation of the TOPSIS method.

## Features

- User-friendly functionality to perform the TOPSIS method on decision matrices.
- Allows customization of weights for each criterion.
- Supports both beneficial and non-beneficial criteria (impacts).
- Provides preference scores and rankings for alternatives.

    Parameters:
        data (list of lists): The decision matrix (alternatives x criteria).
        weights (list): Weights assigned to each criterion.
        impacts (list): Use '+' for beneficial criteria and '-' for non-beneficial criteria.

    Returns:
        list: Preference scores for each alternative.
        list: Ranks of each alternative.

## Installation

You can install the *Topsis Package* using pip from PyPI.

### From PyPI:

Install the package using pip:
```bash
pip install 102217106_topsis
```
