from functions import *

ClearConsole()
# Romane, F, 22, 56
# Mathieu, H, 45, 66
# Chrislain, H, 24, 65

""" nb_souris = int(input("Combien de souris à ajouter: "))

souris_ld = GetMiceInfo(nb_souris)
souris_info = ListOfDictsToLists(souris_ld) """

""" export_q = input("Enter a filename to dump or leave empty to void : ")
if export_q != "":
    ExportAsCSV(export_q, souris_info)
 """

old_mice = ImportCSV('test')
old_mice_lists = ListOfDictsToLists(old_mice)
print(old_mice_lists)
PrintMouseInfo(old_mice_lists)

nb_new_mice = int(input("Combien de souris à ajouter: "))
new_mice = GetMiceInfo(nb_new_mice)
new_mice_info = ListOfDictsToLists(new_mice)
print(new_mice_info)

export_question = input("Enter a filename to dump or leave empty to void : ")
if export_question != '':
    mice = ListOfDictsToLists(old_mice+new_mice)
    print(mice)
    ExportAsCSV(export_question, mice)

## TODO : la fin