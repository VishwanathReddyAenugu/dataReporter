import matplotlib
from matplotlib import pyplot as plt

class Report:
    def __init__(self,df):
        self.df = df

    def eda(self):
        print(" Size of the data set",self.df.shape,"\n\n","Number of Unique values per column \n")
        for column in self.df.columns:
            if(self.df[column].unique().shape[0] ==1 ):
                print("column " ,column, " has zero variance")
            elif(self.df[column].unique().shape[0] > 1 and self.df[column].unique().shape[0] < 100):
                print(column," : ",self.df[column].unique().shape[0])
                print()
                print(self.df[column].unique())
            else:
                print(f"Number of Unique values in {column} : {self.df[column].unique().shape[0]}")
                #print(f"column {column} , has high variance, Range ={}")

    def missing(self):
        rows = self.df.shape[0]
        series = self.df.isnull().sum()*(100/rows)
        plt.figure(figsize=(20,8)) 
        matplotlib.pyplot.grid(axis = 'y', linestyle='-.') 
        matplotlib.pyplot.title('Percentage of missing values by column', fontsize=25, weight = 'bold') 
        matplotlib.pyplot.xlabel('Feature', color='#AF5050', labelpad=10, fontsize=20, weight = 'bold') 
        matplotlib.pyplot.ylabel('Percentage', color='#af5050', labelpad=10, fontsize=20, weight = 'bold')
        matplotlib.pyplot.xticks(fontsize=18, rotation=90,weight = 'bold')
        matplotlib.pyplot.yticks(fontsize=18, weight = 'bold')        
        series.plot.bar()