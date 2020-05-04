import matplotlib.pyplot as plt  # 等效于 from matplotlib import pyplot as plt

# print(plt.style.available)    # 不同的style
# ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
# 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette',
# 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel',
# 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

# plt.style.use('fivethirtyeight')
plt.xkcd()  # 漫画(comics)风格

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x, dev_y, color='#444444', linestyle='--', marker='*', label='All Devs')   
# plot默认用line画出（plt.bar()画出条形图）
# color（可传入hex value)、linestyle、marker可分开写，也可合并写（省略参数名称）
# ['blue', 'Red', '#e5Ae37', 'GrEeN'] 表示颜色的字母大小写均可。'k'指黑色black

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, py_dev_y, 'b', linewidth=3, label='Python')

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='JavaScript')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

# 添加legend
# 方法一
# plt.legend(['All Devs', 'Python'])   # 上面的plot方法里不传入label参数。缺点：必须与前面dev_y、py_dev_y先后顺序相同（不推荐这种方法）
# 方法二：plot方法里传入label参数
plt.legend()

# plt.grid(True)    # 发现在xkcd风格下无效

plt.tight_layout()  # tight_layout()会自动调整子图参数，使之填充整个图像区域。padding

plt.show()

plt.savefig('plot')    # 默认png格式。亦可'plot.png'
