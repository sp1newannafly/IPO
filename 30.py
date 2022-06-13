import numpy as np
import pandas as pd
s = pd.Series(['one', 'two', 'three', 'four', 'five'])
s = pd.Series(str(i) for i in s)
ans2 = np.asarray([len(i) for i in s])
print(ans2)