#reads the information
import pandas

data = pandas.read_csv('forestfires.csv')

#Load and describe data: 
#MISSING VALUE TREATMENT
#print(data.isna().sum().sum())


#Create a new column
data["burntarea"] = " "


#Fill the column with data
x = (data.area == 0).empty

data["burntarea"] = ["yes" if i > x else "no" for i in data.area]


##PreProcessing

## Encode Data
data.month.replace(('jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'),(1,2,3,4,5,6,7,8,9,10,11,12), inplace=True)
data.day.replace(('mon','tue','wed','thu','fri','sat','sun'),(1,2,3,4,5,6,7), inplace=True)

data= data.drop(['area'],axis=1)

#save to the file 
data.to_csv("forestfires.csv", index=False)