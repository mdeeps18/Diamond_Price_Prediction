'''import os
path="notebooks/EDA.ipynb"

dir,file=os.path.split(path)
os.makedirs(dir, exist_ok=True)

with open(path,'w') as f:
    pass'''

from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

custdataobj=CustomData(0.34,62.0,54.0,4.47,4.5,2.78,"Ideal","G","VVS1")
data=custdataobj.get_data_as_dataframe()

print(data)