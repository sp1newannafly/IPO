import pandas as pd
import numpy as np
a = pd.Series([2, 4, 6, 8])
b = pd.Series([1, 3, 5, 7])
rez = np.linalg.norm(a-b)
print(rez)