import numpy as np
import pandas as pd
s = pd.Series(np.random.randint(low=1,high=10,size=[100]), pd.date_range('2022-01-01', periods=100, freq='W-SAT'))
print(s)