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

teste = [["1","2","3"],["4","5","6"],["7","8","9"]]

# for list_position, list_position_item in enumerate(teste):
#     for list_in_list_position, list_in_list_item in enumerate(list_position_item):
#         if list_in_list_item == "9":
#             print(list_position, list_in_list_position, list_in_list_item)

texto = "HI LORENA"
print (texto)

texto = texto.replace("HI LORENA", "NOVO")
print(texto)