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
federalCandidates = ['DEPUTADO FEDERAL,', 'DEPUTADO ESTADUAL',
                                  'SENADOR', 'GOVERNADOR', 'PRESIDENTE']
numberKeys = [4, 4, 3, 2, 2]

for position, item in enumerate(federalCandidates):
    if item == 'SENADOR':
        print(numberKeys[position])