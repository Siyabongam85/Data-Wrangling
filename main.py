#We first need to import our libraries we will be using .

import pandas as pd
import numpy as np

# We then need to load our dataset using pandas read_csv file .
Our_Dataset=pd.read_csv('College_Majors')

#We will display the first 5 rows in our dataset using .head method.
print(Our_Dataset)
Our_Dataset.describe().T
