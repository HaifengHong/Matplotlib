import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use('seaborn')

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot_date(dates, y, linestyle='solid')
# plt.plot(dates, y, linestyle='solid')   # 输出图形不一样（没有点）

plt.gcf().autofmt_xdate()   # gcf(): get current figure

plt.tight_layout()
plt.savefig('timeseriesdata_simple')
plt.show()





————————————————————————————————————
# 用DateFormatter

import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from datetime import datetime

plt.style.use('seaborn')

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot_date(dates, y, linestyle='solid')

plt.gcf().autofmt_xdate()

date_format = mpl_dates.DateFormatter('%b %d, %Y')
# '%b %d, %Y'格式如：May 24, 2019
# '%m %d, %Y'格式如：05 24, 2019

plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()
plt.savefig('timeseriesdata_DateFormatter')
plt.show()





————————————————————————————————————
# 读取csv文件

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn')

data = pd.read_csv('data.csv')

data['Date'] = pd.to_datetime(data['Date'])  # 将string转化为datatime
data.sort_values('Date', inplace=True)  # 因为csv最后一行是2019-05-17，sort使之按日期先后顺序排列
# 注意：在pycharm打开csv文件更改内容，会直接更改源文件

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')

plt.gcf().autofmt_xdate()

plt.title('Bitcoin Price')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()
plt.savefig('timeseriesdata_csv')
plt.show()
