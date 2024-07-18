
import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('sqlite:///countries.db')

df = pd.read_csv("countries.csv")

df.to_sql("countries_table", con=engine)

print(df)
