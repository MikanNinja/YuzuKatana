import json

with open('E:/Works/YuzuKatana/YuzuKatana/search/source/zi_data.json', mode='r', encoding='utf-8') as f:
    zi_data = json.loads(f.read())
with open('E:/Works/YuzuKatana/YuzuKatana/search/source/idiom_data.json', mode='r', encoding='utf-8') as f:
    idiom_data = json.loads(f.read())

def search(dic):
    l = 4
    res = []
    for idiom in idiom_data:
        li = len(idiom)
        lu = min(l, li)
        flag = 0
        for j in range(lu):
            zi = idiom[j]
            if zi not in zi_data.keys():
                flag = 1
                break
            zi_pinyin = zi_data[zi]["pinyin"]
            new_l = [[], [], []]
            for k in zi_pinyin:
                new_l[0].append(k['shengmu'])
                new_l[1].append(k['yunmu'])
                new_l[2].append(k['shengdiao'])
            values = list(dic.values())
            #注：这边+1是因为QueryDict返回的字典第一项会有个乱七八糟的键值。反正这段以后肯定要重写的，太乱来了。
            if values[3 * j + 1] != '' and values[3 * j + 1] not in new_l[0]:
                flag = 1
                break
            if values[3 * j + 2] != '' and values[3 * j + 2] not in new_l[1]:
                flag = 1
                break
            if values[3 * j + 3] != '' and values[3 * j + 3] not in new_l[2]:
                flag = 1
                break
        if flag == 0:
            res.append(idiom)

    return res

#print(search({1:'h', 2:'ao', 3:'3', 4:'z', 5:'i', 6:'4', 7:'w', 8:'ei', 9:'2', 10:'zh', 11:'i', 12:'1'}))

