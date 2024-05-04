import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns

# we want to predict the count of new refugees in 2024 using the number of refugees from female and male
# ideally, run a multivariate scatterplot ()

xFemale = np.array([0, 5, 5, 61, 0, 0])
xMale = np.array([0, 10, 0, 164, 0, 5])

ages = ["<4", "5-11", "12-17", "18-59", "60+", "-1*"] # for reference

scatterData = {

    "Asylum Applications": np.array([225 + 218, 225 + 274, 239 + 141, 138 + 52, 48 + 24, 27 + 18, 26 + 40, 22 + 69, 22 + 57, 31 + 70, 43 + 113, 63 + 159, 44 + 160, 32 + 174, 24 + 273, 40 + 298, 48 + 263, 65 + 112, 25 + 39 + 97, 36 + 33 + 72, 29 + 15 + 96, 26 + 42 + 465]),
    "Year": np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]),

}

df = pd.DataFrame(scatterData)

# maybe determine association between current Afghan refugee count and future predicted counts
# or association between count and gender ??
# if both increase, this means people are likely moving in the families since many males and females same time. all the more rsn to help pople
# or many correlation between female and age or male and age

years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
apps = np.array([225 + 218, 225 + 274, 239 + 141, 138 + 52, 48 + 24, 27 + 18, 26 + 40, 22 + 69, 22 + 57, 31 + 70, 43 + 113, 63 + 159, 44 + 160, 32 + 174, 24 + 273, 40 + 298, 48 + 263, 65 + 112, 25 + 39 + 97, 36 + 33 + 72, 29 + 15 + 96, 26 + 42 + 465])

colors = ["crimson", "darkgreen", "black"]
sns.scatterplot(data = df, x = 'Year', y = 'Asylum Applications', color = "crimson")
plt.grid(color = 'darkgreen', linestyle = '-', linewidth = '0.3')
plt.xlabel("Year", fontsize = 12, color = 'grey')
plt.ylabel("Asylum Applications", fontsize = 12, color = 'grey')
plt.title("Number of Asylum Applications of Afghan Refugees per Year", fontweight = 'bold', fontsize = 14)

plt.show()
