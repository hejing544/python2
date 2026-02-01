import random

# 1. 定义周一到周日的列表
week_days = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

print("原始列表：", week_days)
# 先演示：通过索引访问固定元素（列表索引从0开始，0对应第一个元素，6对应最后一个）
print("通过索引访问（第1天）：", week_days[0])
print("通过索引访问（最后1天）：", week_days[-1])  # 负数索引：-1表示最后一个元素，新手可选学
print("-" * 30)

# 2. 随机索引访问（先随机生成一个合法索引，再通过索引获取元素）
# 列表长度是7，索引范围是0-6，用random.randint(0, 6)生成随机索引
random_index = random.randint(0, len(week_days)-1)  # len(week_days)获取列表长度，更灵活，避免硬编码
random_day = week_days[random_index]
print(f"随机索引{random_index}对应的日期：", random_day)
print("-" * 30)

# 3. 重复随机抽取3次（循环+随机，巩固新手知识点）
print("重复随机抽取3次：")
for i in range(3):
    day = random.choice(week_days)
    print(f"第{i+1}次抽取：", day)