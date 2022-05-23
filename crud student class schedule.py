
from tinydb import TinyDB,Query


def menu():

    print()
    print()
    print('-------------------')
    print( "1>Print Schedule")
    print('2>Add Class')
    print('3>Edit Class')
    print('4>Delete Class')
    print('Q>to Quit')
    choice=input('enter your choice')
    print()
    print()
    return choice

def print_schedule():
    print('you are in the print schedule menu')
def add_class():
    print('you are in the add class menu')

def edit_class():
    print('you are in the edit class menu')
def delete_class():
    print('you are in the delete class menu')




# MAIN CODE---------------------------
action='?'
while action.upper()!="Q":
    action=menu()
if acton=="1":
    print_schedule()
elif action=='2':
    add_class()
elif action=='3':
    edit_class()
elif action=='4':
    delete_class

db.close()
