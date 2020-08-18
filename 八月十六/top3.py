'''
编写代码模拟用户登陆。要求：用户名为 python，密码 123456，如果输入正确，打印“欢迎光临”，程序结束，如果输入错误，提示用户输入错误并重新输入

#### 训练目标

- while中的break的使用
'''

user = "python"
password = "123456"

while 1:
    input_user = input("请输入用户名：")
    input_password = input("请输入密码：")
    if input_user == user and input_password == password :
        print("欢迎光临！")
        break
    else:
        print("输入用户或密码错误，请重新输入")
