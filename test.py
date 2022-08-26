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

listtest = ["['TREINAMENTO', 'Deputado Federal', 'Áudio ativado', '0', '@EBOLP']", "['TREINAMENTO', 'Deputado Federal', 'Áudio ativado', '@', '@EBOLD']"]

for i in listtest:
    for j in i:
        print(j)
