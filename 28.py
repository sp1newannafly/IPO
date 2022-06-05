import numpy as np
import pandas as pd
n = 10
s1 = pd.Series(np.random.choice(['dog', 'cat', 'horse', 'bird'], n))
s2 = pd.Series(np.linspace(1,n,n))
ans = s2.groupby(s1).mean()
print(ans)