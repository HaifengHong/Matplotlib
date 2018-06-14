# _*_ coding: utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt




# 绘制多个图形，同时独立显示
# 方法一：无法对已经绘制好的图案进行后续操作（如添加标题、坐标轴、添加后续图形等）
fig1 = plt.figure()  # fig=也可省略
plt.plot([1,2,3,4,5,6])
fig2 = plt.figure()
plt.plot([1,3,5,7,8,10,12])
plt.show()

# 方法二：可以对已经绘制好的图案进行后续操作（如添加标题、坐标轴、添加后续图形等）
# 例一
fig1 = plt.figure().add_subplot(111)
plt.plot([1,2,3,4,5,6])
fig2 = plt.figure().add_subplot(111)
plt.plot([1,3,5,7,8,10,12])
fig1.set_xlabel('This is x axis')
fig2.set_title('Figure2')
plt.show()

# 例二
fig1 = plt.figure('F1',figsize = (6,4)).add_subplot(111)
fig1.plot([1,2,3,4],[5,6,7,8])
fig2 = plt.figure('F2',figsize = (6,4)).add_subplot(111)
fig2.plot([4,5,2,1],[3,6,7,8])
fig1.set_title('Figure1')
fig2.set_xlabel('This is x axis')
plt.show()




# 多个subplot
data1 = np.arange(100, 201)
plt.subplot(2, 1, 1) # plt.subplot(211)
plt.plot(data1)
data2 = np.arange(200, 301)
plt.subplot(212)
plt.plot(data2)
plt.show()

a = np.arange(3) # [0 1 2]
plt.plot([0, 1, 2], [3, 6, 9], '-r*')
plt.plot(a, [2, 4, 9], 'o:g') # 三个属性先后顺序任意
plt.show()




# 散点图scatter
# 例一
N = 100
x = np.random.randn(N)
y = x + np.random.randn(N) * 0.5
plt.scatter(x, y, s=500, c='r', marker='o', alpha=0.5) # c可写成color，默认blue
plt.show()
# 例二
open, high = np.loadtxt('F:/Books and Tutorials for Python/Matplotlib/麦子学院_素材文件和源代码/000001.csv', delimiter=',', skiprows=1, usecols=(1,2), unpack=True) # 路径中\改成/，可以有空格、中文
diff = high - open
yesterday = diff[1:]
today = diff[:-1]
plt.scatter(today, yesterday, s=10, c='green', marker='o', alpha=0.5)
plt.show() # 上面的图关闭后才会显示本图，为何？
# 让两张图同时显示（创建多个图）：
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot([1,2,3], [1,2,3])
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
plt.plot([1,2,3], [3,2,1])
plt.show()




# 折线图plot、plot_date
import matplotlib.dates as mdates
def convert_date(date_bytes):
    return mdates.strpdate2num('%m/%d/%Y')(date_bytes.decode('ascii')) # 将'ascii'省略也可以。%Y：2014，%y：14    %m：12，%b：Dec    %d：28   %H：13，%I：01   %M：49    %S：30
date, open, close = np.loadtxt('F:/Books and Tutorials for Python/Matplotlib/麦子学院_素材文件和源代码/000001.csv', delimiter=',', converters={0:convert_date}, skiprows=1, usecols=(0,1,4), unpack=True) # Skip the first skiprows lines
# converters: A dictionary mapping column number to a function that will convert that column to a float.  # skiprows=1跳过第一行
# date, open, close = np.loadtxt('F:/Books and Tutorials for Python/Matplotlib/麦子学院_素材文件和源代码/000001.csv', delimiter=',', converters={0:mdates.strpdate2num('%m/%d/%Y')}, skiprows=1, usecols=(0,1,4), unpack=True, encoding='ascii') # 换成utf-8也可以
plt.plot_date(date, open, linestyle='-', color='red', marker='o') # 时间序列图
plt.plot_date(date, close, linestyle='--', color='b', marker='<')
plt.show()




# 条形图bar
# 例一
x = np.arange(5)
y = [10, 5, 15, 20, 30]
plt.bar(x, height=y) # height=可省略，默认width=0.8, aligh='center'
plt.bar(x, y, width=0.5, align='edge') # 条左侧与x坐标对齐，width=可省略,align=不可省略
plt.bar(x, height=y, width=-0.5, align='edge') # 条右侧与坐标对齐（width赋负值）
plt.bar(left=0, bottom=x, width=y, height=0.5, facecolor='red', edgecolor='b', linewidth=5, orientation='horizontal') # 条形水平显示 # facecolor/color，linewidth/lw
plt.barh(x, width=y, height=0.5, color='red') # 与上行等效，width=可省略
# 例二（并列条与层叠条）
x = np.arange(5)
y = [10, 5, 15, 20, 30]
y1 = [i*1.5 for i in y] # y*2是y = [10, 5, 15, 20, 30, 10, 5, 15, 20, 30]。区别于list与ndarray
bar_width = 0.4
plt.bar(x, y, bar_width)
# plt.bar(x + bar_width, y1, bar_width, color='red') # 并列条
plt.bar(x, y1, bar_width, bottom=y, color='red') # 层叠条（注意bottom=y）
plt.show()




# 直方图hist
mu = 100 # 样本均值
sigma = 20 # 样本标准差
x = mu + sigma * np.random.randn(200) # 正态分布
plt.hist(x, bins=100, color='red', normed=True) # normed=True（布尔值，非0数字也可以）表示个数除以总体个数，纵坐标表示概率
plt.hist(x, bins=100, color='red', normed=False) # normed=True（0也可以）纵坐标表示个数
plt.show()




# 饼状图pie
frac = [15, 30, 25, 5]
label = ['A', 'B', 'C', 'D']
plt.axis('equal') # plt.axes(aspect=1)等效,将x/y轴比例设成1:1
explode = [0, 0.05, .08, 2] # 数值的大小是分割出来的与其他两块的间隙
plt.pie(x=frac, labels=label, explode=explode, autopct='%.1f%%', shadow=True)
plt.show()




# 颜色和样式

# 颜色表示方法：内置颜色{'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}、灰度、HTML十六进制、RGB(values should be within 0-1 range,除以255.0即可)
y = np.arange(1, 5) # [1 2 3 4]
plt.plot(y, c='y')
plt.plot(y + 1, color='0.5')
plt.plot(y + 2, color='#ADFF2F')
plt.plot(y + 3, color=(186/255.0, 85/255.0, 211/255.0))
plt.show()


# 点型
y = np.arange(1, 5)
plt.plot(y, marker='o') # 写出marker=，会显示线段
plt.plot(y + 1, '*') # 未写出marker=，则不会显示线段
plt.plot(y + 2, marker='+')
plt.plot(y + 3, 'D')
plt.show()


# 线型（-实线、--虚线、-./.-点划线不同、:点线）
y = np.arange(1, 5)
plt.plot(y, '-')
plt.plot(y + 1, '--')
plt.plot(y + 2, '-.')
plt.plot(y + 3, ':')
plt.show()


# 样式字符串（颜色、点型、线型写在同一个字符串，会显示线段）
y = np.arange(1, 5)
plt.plot(y, 'rx-')
plt.plot(y + 1, 'kp--')
plt.plot(y + 2, c='m', marker='o', ls='-.')
plt.show()




# pylab的方式

# 面向对象OO的方式
x = np.arange(1,10)
y = np.random.randn(len(x))
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x, y) # plt.plot(x, y) 等效
ax.set_title('Object Oriented')
plt.show()




# 子图subplot
# 方法一(面向对象)
x = np.arange(1, 101)
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(x, x)
ax4 = fig.add_subplot(224)
ax4.plot(x, np.log(x))
plt.show()
# 方法二
x = np.arange(1, 101)
plt.subplot(221)
plt.plot(x, x)
plt.subplot(224)
plt.plot(x, np.log(x))
plt.show()




# 网格grid
x = np.arange(1, 6)
plt.plot(x, x * 2)
plt.grid() # plt.grid(True)
plt.grid(True, color='r', linewidth=2, linestyle='--') # True、False或不写效果都一样，只要后面指定了属性就显示网格
plt.show()




# 图例legend
# 方法一
x = np.arange(1, 11)
plt.plot(x, x * 2, label = 'Normal')
plt.plot(x, x * 3, label = 'Fast')
plt.plot(x, x * 4, label = 'Faster')
plt.legend(loc='best', ncol=3) # loc='best'/0自适应图例位置（官网有对应关系），没有nrows
plt.show()
# 方法二
x = np.arange(1, 11)
plt.plot(x, x * 2)
plt.plot(x, x * 3)
plt.plot(x, x * 4)
plt.legend(['Normal', 'Fast', 'Faster'], ncol=3)
plt.show()




# 坐标轴范围axis/xlim/ylim
x = np.arange(-10, 11, 1)
plt.plot(x, x * x)
plt.axis([-8, 8, 20, 60])
plt.axis([-5, 5])
plt.xlim(xmin=-2)
plt.show()


# 坐标轴刻度（及日期序列的调整）locator_params(nbins=)
x = np.arange(1, 11, 1)
plt.plot(x, x)
# 方法一：plt
plt.locator_params(nbins=10)  # x/y轴都设定
# 方法二：面向对象（没有交互功能）
ax = plt.gca() # get current axis
ax.locator_params(nbins=10) # x/y轴都设定
ax.locator_params('x', nbins=10) # 只设定x轴
plt.show()


# 添加坐标轴twinx
x = np.arange(2, 20)
y1 = x * x
y2 = np.log(x)
# 方法一：plt
plt.plot(x, y1)
plt.twinx() # 右侧新加坐标轴，默认范围0~1
plt.plot(x, y2, 'r--') # 右侧新加的坐标轴范围改变
plt.show()
# 方法二：面向对象
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x, y1) # 也可用plt.plot
ax1.set_ylabel('Y1')
ax2 = ax1.twinx()
ax2.plot(x, y2, 'r--') # 也可用plt.plot
ax2.set_ylabel('Y2')
ax1.set_xlabel('Compare Y1 and Y2')
plt.show()




# 注释annotate
x = np.arange(-10, 11)
plt.plot(x, x * x)
plt.annotate('this is the bottom', xy=(0,1), xytext=(0,20), arrowprops=dict(facecolor='r',frac=0.2, headwidth=30, width=10)) # xy指箭头尖的坐标，xytext指文本起始位置，frac指箭头大占比
plt.show()




# 文字text size/fontsize
x = np.arange(-10, 11)
plt.plot(x, x * x)
plt.text(-2, 40, 'function: y = x', fontsize=10, family='fantasy', style='italic', weight='black', bbox=dict(facecolor='r', alpha=0.2)) # weight可以用0~1000的数字
plt.show()




# 公式text
plt.axis([1, 7, 1, 5])
plt.text(2, 4, r'$ \alpha_i \beta_j \pi \lambda \omega $', size=20)
plt.text(4, 4, r'$ \sin(0)=\cos(\frac{\pi}{2}) $', size=20)
plt.text(2, 2, r'$ \lim_{x \rightarrow y}\frac{1}{x^3} $', size=20)
plt.text(4,2, r'$ \sqrt[4]{x}=\sqrt{y} $', size=20)
plt.show()




# 填充fill、fill_between
x = np.linspace(0, 5 * np.pi, 2000)
y1 = np.sin(x)
y2 = np.sin(2 * x)
# fill的用法
plt.fill(x, y1, 'b', alpha=0.3)
plt.fill(x, y2, 'r', alpha=0.3)
plt.show()
# fill_between的用法
plt.plot(x, y1, 'r')
plt.plot(x, y2, 'b')
plt.fill_between(x, y1, y2, where=y1>=y2, facecolor='yellow') # 若x值少，仍要填充满则可以增加interpolate=True
plt.fill_between(x, y1, y2, where=y1<y2, facecolor='green')
plt.show()




# 形状
import matplotlib.patches as mpatches
fig, ax = plt.subplots() # 返回两个对象，The 1st one must be a figure object, and the other one should be a group of axes objects. # 本句等效于fig = plt.figure() ax = fig.add_subplot(111)
# 圆形
circle = mpatches.Circle([0.2,0.2], 0.1) # 圆心坐标（注意用[]括起来）、半径
ax.add_patch(circle)
# 矩形
rect = mpatches.Rectangle([0.2,0.8], 0.2, 0.1, color='r') # 左下角坐标、x宽度、y高度 # color不能简写成c
ax.add_patch(rect)
# 多边形
polygon = mpatches.RegularPolygon([0.8, 0.1], 5, 0.1, color='green') # 形心坐标、边数、形心到顶点距离
ax.add_patch(polygon)
# 椭圆
ellipse = mpatches.Ellipse([0.8,0.8], 0.4, 0.2, color='y') # 圆心、长直径、短直径
ax.add_patch(ellipse)
plt.xlim([0,1.2])
plt.axis('equal') # 要放到后面
plt.grid()
plt.show()




# 美化样式
print(plt.style.available) # available没有()
plt.style.use('bmh')
# fig, axes = plt.subplots(nrows=2, ncols=2)
# axes = plt.subplots(nrows=2, ncols=2)[1]
# ax1, ax2, ax3, ax4 = axes.ravel() # 把子图的坐标轴赋给四个对象
fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2) # 注意不是[ax1, ax2, ax3, ax4]
# ax1
x, y = np.random.normal(size=(2, 100))
ax1.plot(x, y, 'o')
# ax2
x = np.arange(10)
y = np.arange(10)
ncolors = len(plt.rcParams['axes.prop_cycle']) # 'axes.color_cycle'已被弃用。默认的颜色从七个变成十个
shift = np.linspace(0, 9, ncolors) # numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# print(shift) # [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
for s in shift:
    ax2.plot(x, y + s, ncolors) # 这里为何加ncolor?
# ax3
x = np.arange(5)
y1, y2, y3 = np.random.randint(1, 25, size=(3,5))
width = 0.3
ax3.bar(x, height=y1, width=width, align='edge', color=plt.rcParams['axes.prop_cycle'].by_key()['color'][1]) # 默认颜色序列中的第二个
ax3.bar(x + width, height=y2, width=width, align='edge', color=plt.rcParams['axes.prop_cycle'].by_key()['color'][2])
ax3.bar(x + width * 2, height=y3, width=width,  align='edge',color=plt.rcParams['axes.prop_cycle'].by_key()['color'][3])
# ax4
for i, color in enumerate(plt.rcParams['axes.prop_cycle'].by_key()['color']):
    xy = np.random.normal(size=2) # 圆心坐标 1行2列
    ax4.add_patch(plt.Circle(xy, radius=0.3, color=color))
    # x, y = np.random.normal(size=2)
    # ax4.add_patch(plt.Circle([x, y], radius=0.3, color=color))
ax4.axis('equal') # ax4.axes(aspect=1) 出现错误：TypeError: 'AxesSubplot' object is not callable 看来只能plt.axes(aspect=1)
plt.show()




# 极坐标（每个点包含角度、半径两个属性） 调用subplot()创建子图时通过设置projection='polar',便可创建一个极坐标子图
theta = [(np.pi / 2) * i for i in range(5)]
r = np.arange(1, 6)
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, 'r') # theta和r位置不能反了，否则画出的图不对
ax.grid(True, color = "g", linestyle=':', linewidth=2) # 对于ax.grid()第一次要指定True或False，而plt.grid()则不必。
ax.grid() # 若作为第一次，则不显示网格
ax.grid() # 又显示，按照上面的属性
plt.show()




# 函数积分图
from matplotlib.patches import Polygon # 多边形，注意P大写
def fun(x):
    return - (x - 2) * (x - 8) + 40
x = np.linspace(0, 10) # 默认num=50
y = fun(x)
fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
a, b = 2, 9
ax.set_xticks([a, b]) # 设置x轴显示坐标刻度为2和9
ax.set_yticks([]) # 设置y轴不显示坐标刻度
ax.set_xticklabels([r'$ \mathrm{a} $', r'$ b $']) # 把2变成a，9变成b
plt.figtext(0.9, 0.05, r'$ x $')
plt.figtext(0.1, 0.9, r'$ y $')
ix = np.linspace(a, b)
iy = fun(ix)
ixy = zip(ix, iy) # 打包成坐标对。zip()返回类型是zip，将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。[( , ), ( , ), ( , ), ……]
verts = [(a, 0)] + list(ixy) + [(b, 0)] # verts外边的点的坐标tuple构成的列表list。需将zip类型转化为list
# verts = list((a, 0)) + list(ixy) + list((b, 0)) # [2, 0, (2.0, 40.0), ……,  (9.0, 33.0), 9, 0] 有误
# print(list(zip(ix, iy))) # 输出正确
# print(list(ixy)) # 输出[] 空的，不同于上行，为何？受到verts = [(a, 0)] + list(ixy) + [(b, 0)]中list(ixy)的影响，若放在此句前，则输出正确
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5') # 注意数字外加'' 用灰度值表示颜色（值越大灰色越浅）
ax.add_patch(poly)
# horizontalalignment controls whether the x positional argument for the text indicates the left, center or right side of the text bounding box.
plt.text(2.5,35, r'$ \int_a^b (- (x - 2) * (x - 8) + 40) dx $', fontsize=12, horizontalalignment='left') # 将文字框左对齐于此x坐标2.5
plt.show()




# 散点、条形图




# 球员能力图
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc', size=10)

plt.style.use('ggplot') # 必须放在前面，放在后面无效果

ability_size = 6
ability_label = ['进攻', '防守', '盘带', '速度', '体力', '射术']
players = {
    'M': np.random.randint(low=60, high=100, size=ability_size),
    'H': np.random.randint(low=60, high=100, size=ability_size),
    'P': np.random.randint(low=60, high=100, size=ability_size),
    'Q': np.random.randint(low=60, high=100, size=ability_size), # 最后一行的,可省略
}

theta = np.linspace(0, 2*np.pi, num=7)

players['M'] = np.append(players['M'], players['M'][0]) # 将‘进攻’增加至列表，与theta数量一致，一一对应
# players['M'].append(players['M'][0]) # 错误，AttributeError: 'numpy.ndarray' object has no attribute 'append'
players['H'] = np.append(players['H'], players['H'][0])
players['P'] = np.append(players['P'], players['P'][0])
players['Q'] = np.append(players['Q'], players['Q'][0])

fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(nrows=2, ncols=2, subplot_kw=dict(projection='polar')) # 在这里subplots这样设定polar，或者ax1.subplot(221, projection='polar'))

ax1.plot(theta, players['M'], 'r')
ax1.set_xticks(theta) # 圈边上的刻度默认将一圈分成8等分，而theta是将一圈分成了6等分，因此对不齐，这行代码将一圈上的刻度设置成跟theta一样
ax1.set_yticks([20, 40, 60, 80, 100]) # 效果不对，为何？
# print(players['M']) # [84 78 98 84 90 72 84]
ax1.set_xticklabels(ability_label, y=0.01, fontproperties=font) # y=数字（0~1）是设定标签与圆心之间的距离（数字越小距离越远，但有个最远距离，刚合适）
ax1.set_title('梅西', position=(0.5, 0.98),fontproperties=font, size=15, color='r') # position设置title文本的位置，这里的color不能简写成c或省略
ax1.fill(theta, players['M'], 'r', alpha=0.3)

ax2.plot(theta, players['H'], 'g')
ax2.set_xticks(theta)
ax2.set_xticklabels(ability_label, y=0.01, fontproperties=font)
ax2.set_title('哈维', position=(0.5, 0.98),fontproperties=font, size=15, color='g')
ax2.fill(theta, players['H'], 'g', alpha=0.3)

ax3.plot(theta, players['P'], 'b')
ax3.set_xticks(theta)
ax3.set_xticklabels(ability_label, y=0.01, fontproperties=font)
ax3.set_title('皮克', position=(0.5, 0.98), fontproperties=font, size=15, color='b')
ax3.fill(theta, players['P'], 'b', alpha=0.3)

ax4.plot(theta, players['Q'], 'y')
ax4.set_xticks(theta)
ax4.set_xticklabels(ability_label, y=0.01, fontproperties=font)
ax4.set_title('切赫', position=(0.5, 0.98),fontproperties=font, size=15, color='y')
ax4.fill(theta, players['Q'], 'y', alpha=0.3)

plt.show()