import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]  # 0.1是指本块的尖端与圆心之间的距离占半径的百分比

plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=30, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})
# edgecolor指定块之间的颜色。startangle指定第一块右边缘线与水平线之间的角度。autopct显示百分比。

plt.title('My Awesome Pie Chart')
plt.tight_layout()
plt.savefig('pie')
plt.show()
