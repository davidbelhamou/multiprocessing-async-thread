import numpy as np
import pandas as pd
import json
# store names
stores = name = ["david", "dima", "elad", "nir", "ron", "roy"]

# number of daily sales
number_of_sales_per_store = 6
df = pd.DataFrame(columns=["id", "name"], dtype=np.int8)
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

json_data = df.to_json()
# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)