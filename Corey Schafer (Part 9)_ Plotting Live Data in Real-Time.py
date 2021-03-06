import matplotlib.pyplot as plt
import random
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))  # 包括5
    plt.cla()   # 清理掉之前的axis（不然每次重新画brand-new的图，叠加之前的，导致每次颜色都不同）
    plt.plot(x_vals, y_vals)


ani = FuncAnimation(plt.gcf(), animate, interval=1000)  # interval单位ms。interval=1000为间隔1s

plt.tight_layout()
plt.savefig('livedata_simple')
plt.show()





————————————————————————————————————
# 动态生成数据，写入csv，并同步动态画图，有点复杂，略去。
