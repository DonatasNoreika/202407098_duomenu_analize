import pandas as pd

orai = {
    'data': ['7/1/2019', '7/2/2019', '7/3/2019', '7/4/2019', '7/5/2019'],
    'temperatura': [32, 35, 28, 24, 22],
    'vejas': [6, 7, 2, 4, 5],
    'oras': ['Lietus', 'Saulėta', 'Saulėta', 'Saulėta', 'Debesuota']
}

df = pd.DataFrame(data=orai)
# print(df)


# print(df.describe())
print(df.info())