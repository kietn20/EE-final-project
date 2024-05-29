import numpy as np
import matplotlib.pyplot as plt

######  Example 1.11 ##########
# load text file
fname = 'Sales_01_20.csv'  # comma separated values
# data1 = np.loadtxt(fname, delimiter=',', skiprows=1)  # skip first row
data1 = np.loadtxt('Sales_01_20.csv', delimiter=',', dtype=int, skiprows=1)

years = data1[:, 0]
sale_amount = data1[:, 1]

start_year = 2001
end_year = 2020

years_range = np.arange(start_year, end_year + 1)
mean_values = [np.mean(sale_amount[years == year]) for year in years_range]
std_values = [np.std(sale_amount[years == year]) for year in years_range]

print('------------ Mean Price ------------')
for i, mean in enumerate(mean_values):
    print(f'Year: {2001 + i} | Mean_Price: {mean}')

print('------------ STD ------------')
for i, mean in enumerate(mean_values):
    print(f'Year: {2001 + i} | STD: {mean}')

# print (data1)
# Create a figure containing a single axes
fig, ax = plt.subplots(1, 3, figsize=(15, 8))
ax[0].bar(years_range, mean_values, color='purple', alpha=0.6)
ax[0].set_title("Yearly Mean Prices (2001-2020)")
ax[0].set_xlabel('List Year')
ax[0].set_ylabel('Mean Sale_Amount')
ax[0].set_xticks(years_range)
ax[0].set_xticklabels([str(int(year)) for year in years_range], rotation=45)

ax[1].bar(years_range, std_values, color='orange', alpha=0.6)
ax[1].set_title("Yearly Standard Deviation of Prices (2001-2020)")
ax[1].set_xlabel('List Year')
ax[1].set_ylabel('Standard Deviation')
ax[1].set_xticks(years_range)
ax[1].set_xticklabels([str(int(year)) for year in years_range], rotation=45)

range_start, range_end = 200000, 300000
probability_values = []
for year in years_range:
    houses_sold = sale_amount[years == year]
    inclusive_range = np.sum((houses_sold >= range_start)
                             & (houses_sold <= range_end))
    probability_values.append(inclusive_range / len(houses_sold)
                              ) if len(houses_sold) != 0 else 0

print('------------ Probability ------------')
for i, probability in enumerate(probability_values):
    print(f'Year: {2001 + i} | Probability: {probability}')

ax[2].bar(years_range, probability_values, color='red', alpha=0.6)
ax[2].set_title('Yearly Probability of Price between $200,000-$300,000')
ax[2].set_xlabel('List Year')
ax[2].set_ylabel('Probability P()')
ax[2].set_xticks(years_range)
ax[2].set_xticklabels([str(int(year)) for year in years_range], rotation=45)

plt.tight_layout()
plt.show()
