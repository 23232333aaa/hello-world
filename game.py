"""第一个游戏"""

temp = input("猜一下数字")
guess = int(temp)

if guess == 8:
    print("你是我心里的蛔虫吗？")
    print("猜中了也没用")
else:
    print("猜错了，是8")

print("游戏结束")
