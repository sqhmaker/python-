'''
1，判断单词great是否在这个字符串中，如果在，则将每一个great后面加一个s， 如果不在则输出 great不在该字符串中
2，将整个字符串的每一个单词都变成小写，并使每一个单词的首字母变成大写
3，去除首尾的空白，并输出处理过后的字符串

#### 训练目标

1. 字符串的相关操作
'''

words = " great craTes Create great craters, But great craters Create great craters "

if 'great' in words :
    changed_words = words.replace('great', 'greats')
    print(changed_words)
else:
    print("great不在该字符串中")

lower_words = words.lower()
title_words = lower_words.title()
print(title_words)

stripped_words = title_words.strip()
print(stripped_words)