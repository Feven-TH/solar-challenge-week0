import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12,6)

# ------------------------------
# Data Summary & Missing Values
# ------------------------------
def summarize_df(df):
    """
    Prints summary statistics and missing value information.
    Lists columns with >5% missing values.
    """
    print("=== Data Info ===")
    print(df.info())
    print("\n=== Summary Statistics ===")
    print(df.describe())
    
    print("\n=== Missing Values ===")
    missing = df.isna().sum()
    print(missing)
    
    high_missing = missing[missing/len(df) > 0.05]
    if len(high_missing) > 0:
        print("\nColumns with >5% missing values:")
        print(high_missing)
    else:
        print("\nNo columns with >5% missing values.")


# ------------------------------
# Z-score Outlier Detection
# ------------------------------
def flag_outliers_zscore(df, cols, threshold=3):
    """
    Returns a DataFrame with True/False for outliers based on Z-score
    """
    outliers = pd.DataFrame(False, index=df.index, columns=cols)
    for col in cols:
        if col in df.columns:
            z_scores = (df[col] - df[col].mean())/df[col].std()
            outliers[col] = z_scores.abs() > threshold
    return outliers


# ------------------------------
# Fill Missing Values
# ------------------------------
def fill_missing(df, cols, method='median'):
    """
    Fill missing values with median or mean
    """
    for col in cols:
        if col in df.columns:
            if method == 'median':
                df[col] = df[col].fillna(df[col].median())
            elif method == 'mean':
                df[col] = df[col].fillna(df[col].mean())
    return df


# ------------------------------
# Plotting Helpers
# ------------------------------
def line_plot(df, x, y, title=None):
    plt.figure()
    sns.lineplot(data=df, x=x, y=y)
    if title: plt.title(title)
    plt.show()


def scatter_plot(df, x, y, hue=None, size=None, title=None):
    plt.figure()
    sns.scatterplot(data=df, x=x, y=y, hue=hue, size=size)
    if title: plt.title(title)
    plt.show()


def heatmap_corr(df, cols):
    plt.figure()
    sns.heatmap(df[cols].corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()


def histogram(df, col, bins=30):
    plt.figure()
    sns.histplot(df[col], bins=bins, kde=True)
    plt.title(f"Histogram of {col}")
    plt.show()
