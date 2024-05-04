# 打开文件并逐行处理
with open("D:/aoi/55.txt", 'r') as f:
    # 读取输入文件中的每一行并创建一个输出文件
    for line in f:
        # 去掉行末的换行符并使用该行文本作为输出文件名
        filename = line.rstrip() + '.txt'
        # 创建一个新的输出文件并将行文本写入其中
        with open(filename, "w") as out_file:
            out_file.write("5 0.5 0.5 1 1")