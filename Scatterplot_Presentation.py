#code for scatter plot + some ideas/codes we can use to tweak it at the bottom
#the csv file I used is uploaded in the files in the correct formatting
#here is the youtube tutorial I followed: https://www.youtube.com/watch?v=zZZ_RCwp49g&t=860s
  #I think this guy's youtube account will be a really good resource 

import pandas as pd
from matplotlib import pyplot as plt


plt.style.use('seaborn')

data = pd.read_csv('hdi_pop_growth_2019.csv')
x = data['HDI_2019']
y = data['Population_Growth_Rate']
 
plt.scatter(x, y, s = 100, color = 'blue', edgecolor = 'black', linewidth = 1, alpha = 0.75)

plt.title('Population Growth against HDI by Country in 2019')
plt.xlabel('HDI')
plt.ylabel('Population Growth Rate (%)')

plt.tight_layout()

plt.show()


#to change the shade of colour of different points add a number from 1 to 10 for every point in turn - we can do this to separate out the countries by continent
  #e.g. colors = [1, 10, 9, 8...]
  #there must be a faster way to do this rather than point by point but this is a start
#below are the codes to introduce a colour scale at the side of the graph 
  #cbar = plt.colorbar() 
  #cbar.set_label('Geographical Placement of Countries')

#can do same here by size
#sizes = [numbers here point by point, doesn't have to be 0,10 - not sure what range is]

