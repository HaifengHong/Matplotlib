import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes = np.arange(len(ages_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes - width, dev_y, width=width, color='#444444', label='All Dev')    # 注意要加上width=width
plt.bar(x_indexes, py_dev_y, width=width, color='#008fd5', label='Python')
plt.bar(x_indexes + width, js_dev_y, width=width, color='#e5ae38', label='JavaScript')

plt.legend()

plt.xticks(ticks=x_indexes, labels=ages_x)  # x轴用ages_x的数据

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()





——————————————————————————————————————————————————————————

### 从csv文件读入数据，画图

from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()    # 用于计数各个language的使用人数，tuple类型

for response in lang_responses:
    language_counter.update(response.split(';'))    # update()更新该次迭代新增的list中各元素的数量

language = []
popularity = []

for item in language_counter.most_common(15):   # 取前15个最common的
    language.append(item[0])
    popularity.append(item[1])

language.reverse()  # inplace。为了后面使用barh()时，根据人数多少，从上往下降序排列显示
popularity.reverse()    # 与language保持一致

plt.barh(language, popularity)  # 横向显示bar。注意里面的参数先后顺序

plt.title('Most Popular Languages')
plt.xlabel('Number of People Who Use')  # 注意是xlabel

plt.tight_layout()

plt.savefig('barh')

plt.show()
