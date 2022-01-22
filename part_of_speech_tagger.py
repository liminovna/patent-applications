from nlpir.native import ICTCLAS
import jieba
import jieba.posseg as pseg
from jieba import analyse
# from nlpir.native import ictclas, tools
import os
import pynlpir


 jieba.enable_paddle() # 启动paddle模式。 0.40版之后开始支持，早期版本不支持
 s = '所述存储执行模块，用于按照并行存储的方式将所述接收模块接收的数据存储到所述存储模块'


 def tknz(infile_PATH):
     with open(infile_PATH, 'r', encoding='utf8') as i, open('OUTPUT.txt', 'a+', encoding='utf8') as o:
         for line in i:
             if line != '\n':
                 token_list = jieba.lcut(line.strip(), cut_all=False)
                 o.write(' '.join(token_list) + '\n')

             # print(' '.join(token_list))


 def kwrds():
     jieba.analyse.set_stop_words(infile_PATH)


 def jb_tgs(text):
     # print(jieba.lcut(s))

     for l in text:
         words = pseg.cut(l)
         lines_l = []
         for w in words:
             lines_l.append('%s_%s' % (w.word, w.flag))

     return lines_l

def pnlpr_tgs(text):
    lines = []
    pynlpir.open()
    for l in text:
        prcssd = pynlpir.segment(l.strip())
        lines.append(prcssd)
    pynlpir.close()
    return lines


patent = 'WO2014008624A1.txt'
patent_p = 'WO2014008624A1_tagged.txt'
with open(patent, 'r', encoding='utf8') as intext, open(patent_p, 'a+', encoding='utf8') as outtext:
    for l in pnlpr_tgs(intext):
        s = ''
        for i in l:
            word, tag = (i[0], i[1])
            s += str('%s_%s ' % (word, tag))
        outtext.write(s + '\n')



