# Maintain 3 series, low, avg, and high. Finally create a dataframe for the count associated
# with the 3 series and return.

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    lowCount = (accounts['income'] < 20000).sum()
    avgCount = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    highCount = (accounts['income'] > 50000).sum()

    return pd.DataFrame([['Low Salary', lowCount], ['Average Salary', avgCount], \
        ['High Salary', highCount]], columns= ['category', 'accounts_count'])