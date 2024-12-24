import random

# 读取path.txt文件中的所有行
with open('path.txt', 'r') as file:
    lines = file.readlines()

# 打乱行的顺序
random.shuffle(lines)

# 计算95%和5%的索引
train_size = int(len(lines) * 0.95)

# 划分训练集和验证集
train_lines = lines[:train_size]
validation_lines = lines[train_size:]

# 将训练集写入train.txt
with open('train.txt', 'w') as train_file:
    train_file.writelines(train_lines)

# 将验证集写入validation.txt
with open('validation.txt', 'w') as validation_file:
    validation_file.writelines(validation_lines)

print(f'Total lines: {len(lines)}')
print(f'Train lines: {len(train_lines)}')
print(f'Validation lines: {len(validation_lines)}')
