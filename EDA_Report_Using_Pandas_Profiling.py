# Import necessary libraries
import pandas as pd
from pandas_profiling import ProfileReport

# Load data into a pandas dataframe
data = pd.read_csv('path/to/your/data.csv')

# Generate EDA report
profile = ProfileReport(data, title='Pandas Profiling Report', explorative=True)

# Save report as an HTML file
profile.to_file('output.html')