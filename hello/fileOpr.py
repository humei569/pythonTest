# 文件操作相关
# 打开文件
file = open("hello/input.txt", "r")  # 读模式打开文件
# print(file.name)  # 文件名
# print(file.mode)  # 文件打开模式

# 读文件
# print(file.readline())  # 读取文件的一行内容
# print(file.readlines())  # 读取文件内容，返回列表
# print(file.read(50))  # 获取文件指针位置
file.close()
# 写文件
# f = open("hello/output.txt", "w")  # 写模式打开文件
# # f.write("hello world\n")  # 写入文件
# f.writelines(["hello python\n", "hello java\n"])  # 写入多行

# f = open("hello/output.txt", "a")  # 追加模式打开文件，此模式不可读
f = open("hello/output.txt", "a+")  # 追加读写模式打开文件
# f.seek(0)  # 将文件指针移动到文件开头
# print(f.tell())
# print(f.read())  # 读取文件内容，返回列表(无法读取内容)
# f.write("hello redis\n")  # 追加写入文件
# 关闭文件
f.close()  # 关闭文件

# with open 语句
# 作用：代码执行完毕后，自动关闭文件
# with open("hello/input.txt", "r") as f:
    # print(f.read())


# 复制图片
#   读取图片的二进制数据
# with open(r"C:\Users\humei\Desktop\20210928210603812.png", "rb") as file:
#     img = file.read()
#     print(img)

#   将二进制数据写入到新的图片文件中
# with open("hello\output.png", "wb") as file:
#     file.write(img)


# 文件和目录操作
import os

# 文件重命名
os.rename("hello/output.txt", "hello/output_rename.txt")
