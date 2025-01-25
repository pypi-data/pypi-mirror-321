"""
Topsis Package
--------------
A Python package for implementing the Topsis decision-making method.
"""

# Version of the Topsis package
__version__ = "0.1"

# Import the main functions for easier access
from .topsis import normalize_matrix, weighted_matrix, ideal_solution, negative_ideal_solution, topsis_score, rank, main
