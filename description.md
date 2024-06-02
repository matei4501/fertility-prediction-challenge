# Description of submission
After testing several approaches (random effects reggresion, deep learning, machine learning algorithms for time-series data) the best performing one was XGBoost. This could be due to several factors:
    Firstly, when using XGBoost we can keep all features, even ones with a high percentage of missing data, because of XGBoost's ability to handle missing values by learning branch directions for missing values. Therefore, we do not lose any information. As a side, various imputation methods were tried (interpolation + ffill +bfill, knn, multiple imputation), but that only degraded the results.
    Secondly, drawbacks of other methods. The regression methods we tried could not capture non-linear relationships. There were not enough observations for a deep learning approach to be able to shine.

Due to the lack of preprocessing required for an XGBoost model we kept preprocessing simple. We only kept observations where the outcome was known and we only kept columns that were either numeric or categorical.

There are several advantages to our final result. The model is fast and can take advantage of categorical features, it requires minimal preprocessing, and it is interpretable due to the access to feature importances.