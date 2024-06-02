"""
This is an example script to train your model given the (cleaned) input dataset.

This script will not be run on the holdout data, 
but the resulting model model.joblib will be applied to the holdout data.

It is important to document your training steps here, including seed, 
number of folds, model, et cetera
"""

from sklearn.ensemble import HistGradientBoostingClassifier
import pandas as pd
import random
import joblib
from xgboost import XGBClassifier

def train_save_model(cleaned_df, outcome_df):
    """
    Trains a model using the cleaned dataframe and saves the model to a file.

    Parameters:
    cleaned_df (pd.DataFrame): The cleaned data from clean_df function to be used for training the model.
    outcome_df (pd.DataFrame): The data with the outcome variable (e.g., from PreFer_train_outcome.csv or PreFer_fake_outcome.csv).
    """
    
    ## This script contains a bare minimum working example
    random.seed(1) # not useful here because logistic regression deterministic
    
    # Combine cleaned_df and outcome_df
    model_df = pd.merge(cleaned_df, outcome_df, on="nomem_encr")

    # Filter cases for whom the outcome is not available
    model_df = model_df[~model_df['new_child'].isna()]  

    X = model_df.drop(columns=["nomem_encr", "new_child", "outcome_available"])
    y = model_df["new_child"]

    params = {'learning_rate': 0.02091617422015919,
          'n_estimators': 843,
          'max_depth': 7,
          'min_child_weight': 3,
          'subsample': 0.6576877866257521,
          'colsample_bytree': 0.8670126466945359,
          'gamma': 0.5386742083894775,
          'lambda': 0.12559455867301336,
          'scale_pos_weight': 4.5}

    clf = XGBClassifier(**params, enable_categorical=True, n_jobs=-1)
    clf.fit(X, y)

    # Save the model
    joblib.dump(clf, "model.joblib")

