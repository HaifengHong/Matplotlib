import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']

plt.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All Devs')
plt.plot(ages, py_salaries, label='Python')

# overall_median = 57287
# 后面改为：where=(py_salaries > overall_median)

# 注意fill_between里前面部分传入三个变量
# interpolate参数作用？
plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries > dev_salaries), interpolate=True, alpha=0.2,
                 label='Above Avg')
plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries <= dev_salaries), interpolate=True, color='red',
                 alpha=0.2, label='Below Avg')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.savefig('fill_between')
plt.show()
