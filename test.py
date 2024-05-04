import os
import csv

# 标签文件所在目录
label_dir = 'D:/aoi/0303'

# CSV文件名
csv_file = 'labels.csv'

# 打开CSV文件进行写入
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)

    # 遍历标签文件
    for file_name in os.listdir(label_dir):
        if file_name.endswith('.txt'):
            # 读取标签文件内容
            with open(os.path.join(label_dir, file_name), 'r') as f_label:
                labels = f_label.readlines()

            # 写入CSV文件
            for label in labels:
                label_info = label.strip().split()
                object_class = label_info[0]
                writer.writerow((file_name, object_class))