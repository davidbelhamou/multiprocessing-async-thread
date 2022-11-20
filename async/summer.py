import numpy as np
import pandas as pd
# store names
stores = ["store_a", "store_b", "store_c", "store_d", "store_e"]

# number of daily sales
number_of_sales_per_store = 6
df = pd.DataFrame(columns=["store_name", "sales"], dtype=np.int8)
for store in stores:
    d = pd.DataFrame(
        dict(
            store_name=[store for _ in range(number_of_sales_per_store)],
            sales=[
                np.random.randint(10, 10000) for _ in range(number_of_sales_per_store)
            ],
        )
    )
    df = df.append(d)

df