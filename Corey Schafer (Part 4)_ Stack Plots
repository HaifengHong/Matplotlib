import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]  # 随着minute的增加而累加的得分数
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
labels = ['player1', 'player2', 'player3']

colors = ['#008fd5', '#fc4f30', '#6d904f']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc='upper left')
# plt.legend(loc=(0.02, 0.1))  # 注意传入的是tuple，数字表示图例的百分比坐标

plt.title('My Awesome Stack Plot')

plt.tight_layout()
plt.savefig('Stack Plot')
plt.show()





————————————————————————————————————————————————————————————————————
# player数据与上面的不一样

import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]
labels = ['player1', 'player2', 'player3']

colors = ['#008fd5', '#fc4f30', '#6d904f']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc=(0.07, 0.05))
plt.title('My Awesome Stack Plot')

plt.tight_layout()
plt.savefig('StackPlot2')
plt.show()


