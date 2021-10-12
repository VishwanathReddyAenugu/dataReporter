import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns

class Report:
    def __init__(self,df):
        self.df = df
        

    def eda(self):
        numericalColumns = self.df.select_dtypes(include = ["int64","float64","datetime64[ns]"]).columns 
        print(" Size of the data set is",self.df.shape,"\n")
        for column in self.df.columns:
            if(self.df[column].unique().shape[0] == 1 ):
                print("\ncolumn: ",column ) 
                print(column, " has zero variance")
            elif(self.df[column].unique().shape[0] > 1 and self.df[column].unique().shape[0] < 100):
                print("\ncolumn: ",column )
                #print("Unique values : ",self.df[column].unique().shape[0]) 
                print(f"Number of Unique values: {self.df[column].unique().shape[0]}")
                if column in numericalColumns:
                    print(f"min = {self.df[column].min()}, max = {self.df[column].max()}, range = {self.df[column].max() - self.df[column].min()}")
                print("List\n",self.df[column].unique())
            else:
                print("\ncolumn: ",column )
                print(f"Number of Unique values: {self.df[column].unique().shape[0]}")
                if column in numericalColumns:
                    print(f"min = {self.df[column].min()}, max = {self.df[column].max()}, range = {self.df[column].max() - self.df[column].min()}")

    def univarDist(self):
        columns = self.df.columns
        sns.set(style="whitegrid")
        for column in columns: 
            #if(self.df[column].unique().shape[0] < 150): # selecting columns with low variance
            sns.displot(df, x=column, color='darkturquoise',height = 5,aspect = 3)
            plt.xlabel(column, labelpad=10, fontsize=20, weight = 'bold')
            plt.ylabel("Count", labelpad=10, fontsize=20, weight = 'bold')
            plt.xticks(fontsize=15,weight = 'bold')
            plt.yticks(fontsize=15, weight = 'bold')

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


    def groupByPlot(self, group, measure):
        sns.set_theme(style="whitegrid", palette="rocket")

        Total = self.df.groupby([group])[measure].sum().sort_values(ascending = False)
        mean = self.df.groupby([group])[measure].mean().sort_values(ascending = False)

        DataFrameTotal = pd.DataFrame({group:Total.index, measure:Total.values})
        DataFrameMean = pd.DataFrame({group:mean.index, measure:mean.values})

        fig, ax = plt.subplots(nrows = 1,ncols = 2, figsize = (15,8), sharey = False)
       
        sns.barplot(ax = ax[0], x = DataFrameTotal[group], y = DataFrameTotal[measure])
        sns.barplot(ax = ax[1], x = DataFrameMean[group], y = DataFrameMean[measure])
        fig.suptitle(f"grouped {measure} by {group} ",  weight='bold').set_fontsize('18')
        
        ax[0].set_title(f"Total {measure} by {group}")
        ax[1].set_title(f"Mean {measure} by {group}")


        