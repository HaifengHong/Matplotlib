#### histgram用于统计在各范围内出现的频数



import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

# plt.hist(ages, bins=5, edgecolor='black')

bins = [10, 20, 30, 40, 50, 60]
plt.hist(ages, bins=bins, edgecolor='black')

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.savefig('hist_simple_bins=bins')
plt.show()





——————————————————————————————————
# 从csv文件读入数据
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)  # y轴数据用对数表示

# 画一条纵向的线
median_age = 29
plt.axvline(median_age, color='#fc4f30', label='Age Median', linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.savefig('hist_csv')
plt.show()
