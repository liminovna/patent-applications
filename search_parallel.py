import re
import os

"""
grab tagged zh text and untagged ru text and investigate them for the word needed. 
go through every line in zh text and if found, search for the same word in the same line in the ru counterpart. 
print both original and translated lines into a file without tags
"""
root = os.getcwd()

# word_l = ['用于', '赘述', '对应', '接入', '配置', '实施', '接收', '参考', '位于', '连接', '示', '生成', '输入', '包括', '相应',
#           '包含', '发送', '参照', '执行', '发明', '描述', '显示', '使得', '设置', '便于', '公开', '涵盖', '确定', '结合', '采用', '涉及',
#           '替换', '实现', '存储', '局限',  '提供', '控制', '进行', '处理']
word_l = ['_nw']


ru_folder = '_ru'
zh_folder = '_zh'


def find_ru_line():

    f_name = f[:f.find('zh')] + 'ru.txt'
    ru_line_counter = 0
    with open(f'_ru/{f_name}', 'r', encoding='utf8') as ru:

        for line in ru:

            if ru_line_counter == zh_line_counter:
                ru_line = line
                return ru_line

            else:
                ru_line_counter += 1


for f in os.listdir(zh_folder):

    with open(f'_zh/{f}', 'r', encoding='utf8') as zh:

        zh_line_counter = 0

        for zh_line in zh:

            if zh_line != '\n':
                for word in word_l:

                    if word in zh_line:

                        ru_line = find_ru_line()
                        with open(f'{word}_par.txt', 'a+', encoding='utf8') as par:

                            print('['+f[:f.find('_')]+']'+' line:'+str(zh_line_counter), zh_line[:-1], ru_line[:-1], '-'*50, sep='\n', end='\n', file=par)

            zh_line_counter += 1

    print(f)



