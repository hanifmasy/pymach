from pandas import read_csv
from pandas import set_option
path = "/home/hanif/pymach/data/melb_data.csv"
names = ['Rooms','Price','Distance','Postcode','Bedroom2','Bathroom','Car','Landsize','BuildingArea','YearBuilt','Lattitude','Longtitude','Propertycount']
data = read_csv(path,usecols=names)
# print(data.head(10))
# print(data.shape)
# print(data.dtypes)

# set_option('display.width',100)
# set_option('precision',2)

# print(data.shape)
# print(data.describe())

corrs = data.corr(method='pearson')
print(corrs)

# print(data.skew())
