#-*- coding:utf-8 -*-

#上面怎么写都可以,只要符合coing[:=]\s*([-\w.]+)
#常见的有#coding=utf-8

"这里是一个标准模块的脚本的写作范式，此处为该脚本文档"

#这里给下一行做注释
new_str='这是一个全局变量' #这里也可以写注释

def hello():
    """
    这里是一个函数定义的多行注释。
    继续多行。
    没有问题。
    """

    return 'hello world!'

#程序主体
if __name__=='__main__':
    print hello()
