import matplotlib.pyplot as plt

plt.style.use('seaborn')

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

plt.scatter(x, y, s=100, c='green', edgecolor='black', linewidths=1, alpha=0.75)
# s大小，c颜色，marker的'X'和'x'不同（'X'粗短，'x'细长）。

plt.tight_layout()
plt.savefig('scatter_simple')
plt.show()





——————————————————————————————————————————
# 增加colorbar、sizes
import matplotlib.pyplot as plt

plt.style.use('seaborn')

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', edgecolor='black', linewidths=1, alpha=0.75)
# 如果没有cmap参数，则颜色是灰色。cmap=''里大小写敏感

cbar = plt.colorbar()
cbar.set_label('Satisfaction')

plt.tight_layout()
plt.savefig('scatter_colorbar&sizes')
plt.show()





——————————————————————————————————————————
# 读取csv文件
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn')

data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c=ratio, cmap='summer', edgecolors='black', linewidths=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.title('Trending Youtube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()
plt.savefig('scatter_csv')
plt.show()

