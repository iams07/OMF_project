from Model import Model
import pandas as pd
data = pd.read_csv('17MA20038.csv')

model = Model()
allocations = model.get_allocations(data)
print(allocations)
