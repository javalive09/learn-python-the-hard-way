# coding=utf-8
# 模块, 类和对象

# 模块
# 包含一些函数和变量的python文件
# 你可以导入这个文件
# 你可以用.操作符访问这个模块的函数和变量


# 类
# 这正是为什么要使用类而不是仅有模块的原因：你可以使用Mystuff这个类，还可以用它来创建更多个Mystuff，而他们之间也不会互相冲突。当你导入一个模块时，你的整个项目也就只有一个这个模块。


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"
# python 查找 MyStuff() 并确认它是你已经定义过的类
# python创建一个空的对象，该对象拥有你在类中用def创建的所有函数
# python看你是否创建了__init__函数，如果有，调用该方法初始化你新创建的空对象
# 在MyStuff中，__init__方法有一个额外的变量self，这是python为我创建的一个空的对象，我可以在其上设置变量。
# 然后，我给self.tangerine设置一首歌词，然后初始化这个对象
# python可以使用这个新创建好的对象，并将其分配给我可以使用的变量thing。

# 类和对象与模块是有区别的
# 类是用来创建迷你模块的蓝本或定义
# 实例化是如何创建这些小模块，并在同一时间将其导入。实例化仅仅是指通过类创建一个对象。
# 由此产生的迷你模块被称为对象，你可以将其分配给一个变量，让它开始运行

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()