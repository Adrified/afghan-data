import matplotlib.pyplot as plt
import seaborn as sns

def function(years):
  return 26.62012987012987 * years - 52969.05714285715 # btw this equation was generated using a random number from a 90% confidence t-interval for slope
# note for cayden/anybody who sees this pls take this equation with a grain of salt it was developed via a scikitlearn t-test and idk its reliability

Year = np.arange(2024, 2030)
App = [function(year) for year in Year]

sns.regplot(x = Year, y = App, color = 'crimson')

plt.xlabel("Year", fontsize = 12, color = 'grey')
plt.ylabel("Applications", fontsize = 12, color = 'grey')
plt.grid(color = 'darkgreen', linewidth = 0.3)
plt.title("Predicted Number of Afghan Asylum Applications", fontweight = 'bold', fontsize = 14)

plt.show()
