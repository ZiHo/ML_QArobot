from src.url import getIntent

while 1:
    question = input("输入问题 (输入'q'退出) ：")
    if question=='q':
        break
    getIntent(question)
