# dataReporter

This project automates routine preprocessing tasks in data analysis

Aim:
To generate a report of data exploration and quality

objectives:
1) Report number of unique values per column
2) Report percentage of Missing values per column
3) Report outliers



Usage: 
1) Download DataReporter.py

import DataReporter
report = Report(df)  
# for jupyter notebooks include " %run -i DataReporter.py"
report.eda()
report.missing()