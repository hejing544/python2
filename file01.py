# 1. 定义周一到周日的列表（新手注意：列表用[]包裹，元素用逗号分隔，字符串用引号包裹）
week_days = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

# 打印原始列表，查看效果
print("原始列表：", week_days)
print("-" * 30)

# 2. 场景A：随机获取列表中的某一个元素（需要用到Python内置的random模块）
import random  # 导入随机数模块，新手记住：要实现随机功能，先导入这个模块

# 随机选择一个元素（核心函数：random.choice()）
lucky_day = random.choice(week_days)
print("随机抽取的幸运日：", lucky_day)
print("-" * 30)

# 3. 场景B：随机打乱整个列表的顺序（核心函数：random.shuffle()）
random.shuffle(week_days)  # 直接打乱原列表（注意：这个函数没有返回值，直接修改原列表）
print("打乱后的列表：", week_days)