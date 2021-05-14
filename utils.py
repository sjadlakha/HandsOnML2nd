# Creating a Custom Transformer
"""
- implement three functions
    1. fit() returns self
    2. transform()
    3. fit_transform() : No need to do if you inherit BaseEstimator
    TransformerMixin gives you extra methods for get_params() and set_params()
"""

from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

rooms_ix, bedrooms_ix, population_ix, household_ix = 3,4,5,6

class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room = True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self


    def transform(self, X, y= None):
        rooms_per_household = X[:, rooms_ix]/X[:, household_ix]
        population_per_household = X[:, population_ix]/X[:, household_ix]

        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix]/ X[:, rooms_ix]

            return np.c_[X, rooms_per_household, population_per_household, bedrooms_per_room]

        else:
            return np.c_[X, rooms_per_household, population_per_household]
# np.c_ : Translates slice objects to concatenation along the second axis.

# Display cross_valid_score helper function

def display_scores(scores):
    print("scores: ", scores)
    print("scores mean: ", scores.mean())
    print("standard deviation: ", scores.std())