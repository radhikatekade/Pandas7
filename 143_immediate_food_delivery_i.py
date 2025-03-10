# Only keep rows where the order_date matches the customer_preference_date. Take the sum of
# number of immidiate count. Return the percentage of immediate count versus total number of
# deliveries.

import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate_order = delivery['order_date'] == delivery['customer_pref_delivery_date']
    immediateCount = immediate_order.sum()
    return pd.DataFrame([round(immediateCount/len(delivery) * 100, 2)], \
        columns = ['immediate_percentage'])