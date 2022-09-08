# from Class.urna import *
#
# urna = Urna()
#
# print(urna.federalCandidates)
# print(urna.numberKeys)
#
# testlist = [1,2,3,5,3,1,2,1,6]
# for position, item in enumerate(testlist):
#     if item == 1:
#         print (position)
#

# federalCandidates = ['DEPUTADO FEDERAL', 'DEPUTADO ESTADUAL',
#                                   'SENADOR', 'GOVERNADOR', 'PRESIDENTE']
# numberKeys = [4, 4, 3, 2, 2]
#
#
# for i in federalCandidates:
#     was_message_read = False
#     if i == 'SENADOR':
#         print(i)
#         was_message_read = True
#     if was_message_read == True:
#         print("Nada")
#         break
#     print("tentando")

# listtest = ["['TREINAMENTO', 'Deputado Federal', 'Áudio ativado', '0', '@EBOLP']", "['TREINAMENTO', 'Deputado Federal', 'Áudio ativado', '@', '@EBOLD']"]
#
# for i in listtest:
#     for j in i:
#         print(j)

# list = ['1','2','3','4','5','6','7']
# for i in range(5, len(list)+1):
#     print (i)
#     str(list[i]).replace('1000')
#     print(list[i])

# teste = [["1","2","3"],["4","5","6"],["7","8","9", "10"]]
#
# # for list_position, list_position_item in enumerate(teste):
# #     for list_in_list_position, list_in_list_item in enumerate(list_position_item):
# #         if list_in_list_item == "9":
# #             print(list_position, list_in_list_position, list_in_list_item)
# #
# # print(len(teste))
#
# from Class.urna import *
#
# urna = Urna()
#
# for i in urna.federalCandidates:
#     print(i)

# INSERINDO NOVOS ITENS EM DICIONÁRIO
# twoDigits = {'1-1': None}
#
# twoDigits['1-1'] = 1.2, 1.3, 1.4
# twoDigits['1-1'] = twoDigits['1-1'],1.2
# print(twoDigits)

twoDigits = {
             '1-1': [None], '1-2': [None], '1-3': [None, 3], '1-4': [None], '1-5': [None], '1-6': [None], '1-7': [None], '1-8': [None],
             '1-9': [None], '1-0': [None], '1-CONFIRMA': [None], '1-BRANCO': [None], '1-CORRIGE': [None],

             '2-1': [None], '2-2': [None], '2-3': [None], '2-4': [None], '2-5': [None], '2-6': [None], '2-7': [None], '2-8': [None],
             '2-9': [None], '2-0': [None], '2-CONFIRMA': [None], '2-BRANCO': [None], '2-CORRIGE': [None],

             '3-1': [None], '3-2': [None], '3-3': [None], '3-4': [None], '3-5': [None], '3-6': [None], '3-7': [None], '3-8': [None],
             '3-9': [None], '3-0': [None], '3-CONFIRMA': [None], '3-BRANCO': [None], '3-CORRIGE': [None],

             '4-1': [None], '4-2': [None], '4-3': [None], '4-4': [None], '4-5': [None], '4-6': [None], '4-7': [None], '4-8': [None],
             '4-9': [None], '4-0': [None], '4-CONFIRMA': [None], '4-BRANCO': [None], '4-CORRIGE': [None],

             '5-1': [None], '5-2': [None], '5-3': [None], '5-4': [None], '5-5': [None], '5-6': [None], '5-7': [None], '5-8': [None],
             '5-9': [None], '5-0': [None], '5-CONFIRMA': [None], '5-BRANCO': [None], '5-CORRIGE': [None],

             '6-1': [None], '6-2': [None], '6-3': [None], '6-4': [None], '6-5': [None], '6-6': [None], '6-7': [None], '6-8': [None],
             '6-9': [None], '6-0': [None], '6-CONFIRMA': [None], '6-BRANCO': [None], '6-CORRIGE': [None],

             '7-1': [None], '7-2': [None], '7-3': [None], '7-4': [None], '7-5': [None], '7-6': [None], '7-7': [None], '7-8': [None],
             '7-9': [None], '7-0': [None], '7-CONFIRMA': [None], '7-BRANCO': [None], '7-CORRIGE': [None],

             '8-1': [None], '8-2': [None], '8-3': [None], '8-4': [None], '8-5': [None], '8-6': [None], '8-7': [None], '8-8': [None],
             '8-9': [None], '8-0': [None], '8-CONFIRMA': [None], '8-BRANCO': [None], '8-CORRIGE': [None],

             '9-1': [None], '9-2': [None], '9-3': [None], '9-4': [None], '9-5': [None], '9-6': [None], '9-7': [None], '9-8': [None],
             '9-9': [None], '9-0': [None], '9-CONFIRMA': [None], '9-BRANCO': [None], '9-CORRIGE': [None],

             '0-1': [None], '0-2': [None], '0-3': [None], '0-4': [None], '0-5': [None], '0-6': [None], '0-7': [None], '0-8': [None],
             '0-9': [None], '0-0': [None], '0-CONFIRMA': [None], '0-BRANCO': [None], '0-CORRIGE': [None]
             }

# twoDigits['1-1'].append(2)
# twoDigits['1-1'].append(3)

for i in twoDigits:
    for j in twoDigits[i]:
        print(j)

digit1 = '1'
digit2 = 'CORRIGIR'
name_of_dict = "["+str(digit1)+"-"+str(digit2)+"]"
print(name_of_dict)
# import re
#
# a = "dsaojdhsa2121DLKSAJ9"
# all_b_read = ""
#
# for i in a:
#     all_b_read = all_b_read + i
#
# justNumbersInFrame = re.sub('[^0-9]', '', all_b_read)
#
# print(justNumbersInFrame)
#
# print(justNumbersInFrame[-2])
# print(justNumbersInFrame[-1])
#
# list = [[1,2,3],[11,12,13]]
#
# for i in range(len(list)):
#     print(list[i][1])

# texto = "12"
#
# print(len(texto))