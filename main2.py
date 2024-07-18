
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///countries.db')

df = pd.read_sql("countries_table", engine)
print(df)
