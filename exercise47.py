# coding=utf-8
# 更复杂的用户输入


# 空格隔开的单词
stuff = raw_input('> ')
words = stuff.split()
print words

# 词汇元组
first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = [first_word, second_word, third_word]


# 异常和数字
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


