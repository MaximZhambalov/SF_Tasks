import pandas as pd
# print(pd.__name__)

def create_medications (names, counts):
    Series_medications = pd.Series (data=counts, index=names)
    return Series_medications

def get_percent (medications, name): 
    return 100 * (medications.loc[name] / sum(medications))

names=['chlorhexidine', 'cyntomycin', 'afobazol']
counts=[15, 18, 7]
medications = create_medications(names, counts)


print(get_percent(medications, "chlorhexidine")) #37.5