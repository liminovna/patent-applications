from pymystem3 import Mystem
import re
import os


def mystem_tagger(text):

    for line in text:
        m = Mystem()
        analysed = m.analyze(line)
        s = ''

        for word in analysed:
            if word['text'] != ' ':
                try:
                    info = word['analysis'][0]['gr']
                    s += word['text'] + '_' + str(re.match('[A-Z]+', info).group() + ' ')
                except:
                    pass

        out.write(s + '\n')


# tags
root = os.getcwd()

for family in os.listdir(root):

    os.chdir(family)
    for pat in os.listdir(os.getcwd()):
        if pat.startswith('RU') or pat.startswith('EA'):
            pat_id = os.path.basename(os.path.abspath(pat))
            print(pat_id)
            with open(pat, 'r', encoding='utf8') as infile, \
             open(pat_id[:pat_id.find('.')] + '_tagged.txt', 'a+', encoding='utf8') as out:
                mystem_tagger(infile)
    os.chdir(root)







