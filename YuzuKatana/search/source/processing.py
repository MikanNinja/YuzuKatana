# coding = utf-8

import xlrd
import json

#
# l = []
# d = {}
# num = 1
#
# with open('level-1.txt', mode='r', encoding='utf-8') as f:
#     l = f.readlines()
#     for i in l:
#         d[i[0]] = {"id": num, "level": 1}
#         num = num + 1
# with open('level-2.txt', mode='r', encoding='utf-8') as f:
#     l = f.readlines()
#     for i in l:
#         d[i[0]] = {"id": num, "level": 2}
#         num = num + 1
# with open('level-3.txt', mode='r', encoding='utf-8') as f:
#     l = f.readlines()
#     for i in l:
#         d[i[0]] = {"id": num, "level": 3}
#         num = num + 1
#
# #到这里已经读好了三级字表里每个汉字的id和等级。
#
#
#
# yisheng = ['ā', 'ō', 'ē', 'ī', 'ū', 'ǖ']
# ersheng = ['á','ó','é','í','ú','ǘ']
# sansheng = ['ǎ','ǒ','ě','ǐ','ǔ','ǚ']
# sisheng = ['à','ò','è','ì','ù','ǜ']
# rep = ['a','o','e','i','u','u']
# yunmu = [yisheng, ersheng, sansheng, sisheng]
#
# def pinyin_chaijie(pinyin):
#     if isinstance(pinyin, str) != True:
#         return "error"
#     pinyin_mod = ''
#     found = 0
#     for i in range(4):
#         for j in range(6):
#             if yunmu[i][j] in pinyin:
#                 pinyin_mod = pinyin + str(i + 1)
#                 pinyin_mod = pinyin_mod.replace(yunmu[i][j], rep[j])
#                 found = 1
#                 break
#         if(found):
#             break
#         pinyin_mod = pinyin + '0'
#     if 'ü' in pinyin_mod:
#         pinyin_mod = pinyin_mod.replace('ü', 'u')
#     if ' ' in pinyin_mod:
#         pinyin_mod = pinyin_mod.replace(' ', '')
#     d = {}
#     if pinyin_mod.startswith('a') or pinyin_mod.startswith('o') or pinyin_mod.startswith('e'):
#         d['shengmu'] = '0'
#         d['yunmu'] = pinyin_mod[:-1]
#         d['shengdiao'] = pinyin_mod[-1:]
#     elif pinyin_mod.startswith('zh') or pinyin_mod.startswith('ch') or pinyin_mod.startswith('sh'):
#         d['shengmu'] = pinyin_mod[:2]
#         d['yunmu'] = pinyin_mod[2:-1]
#         d['shengdiao'] = pinyin_mod[-1:]
#     else:
#         d['shengmu'] = pinyin_mod[:1]
#         d['yunmu'] = pinyin_mod[1:-1]
#         d['shengdiao'] = pinyin_mod[-1:]
#     return d
#
#
# pinyin_data = xlrd.open_workbook('pinyin_data.xls')
# sheet = pinyin_data.sheet_by_index(0)
# nrows = sheet.nrows
# ncols = sheet.ncols
#
# for i in range(nrows):
#     zi = sheet.cell(i, 0).value
#     if zi in d.keys():
#         d[zi]["pinyin"] = []
#         for j in range(1, ncols):
#             if sheet.cell(i, j).value == '':
#                 break
#             else:
#                 d[zi]["pinyin"].append(pinyin_chaijie(sheet.cell(i, j).value))
#
# with open('zi_data.json', mode='w', encoding='utf-8') as f2:
#     json.dump(d, f2, ensure_ascii=False)

############################

#汉字数据部分完成#

#以下是成语处理，从数据集中抽取成语名称，排成列表

############################

with open('idiom.json', mode='r', encoding='utf-8') as f3:
    idioms = f3.read()

idioms_data = json.loads(idioms)

idioms_list = []
for i in idioms_data:
    idioms_list.append(i["word"])

with open('idiom_data.json', mode='w', encoding='utf-8') as f2:
    json.dump(idioms_list, f2, ensure_ascii=False)



