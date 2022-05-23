#cattle database

from tinydb import TinyDB, Query
db= TinyDB('first_db.json')
db.all()


def menu():

    print()
    print()
    print()
    print()
    print('---------------------------')
    print("1>Print Herd")
    print("2>Add Cow")
    print('3> Edit Cow')
    print('4>Delete Cow')
    print('Q>uit')
    choice=input('enter your choice')
    print()
    print()
    return choice

def print_herd(db):
    for cow in db:
        print (cow['name'],cow['age'])


    input('press return to continue')

def add_cow(db):
    print('you are in the add cow option')
    cow_name= input('enter the name:')
    cow_age=int(input('enter the age:'))

    cow_d={'name':cow_name, 'age':cow_age}
    db.insert(cow_d)
    input('press return to continue')

def edit_cow(db):
    print('you are in the edit cow option')
    input('press return to continue')
def delete_cow(db):
    print('you are in the delete cow option')
    for i,cow in enumerate(db):
        print(cow['name'],cow['age'])

    kill_cow=int(input('enter the number of the cow to delete:'))
    db.remove(kill_cow)

    input('press return to continue')






#main program--------------------
action="?"
#while action.upper="Q":
    #action=menu

action=menu()
if action== '1':
        db.all()
        print (db.all())
        print_herd(db)
elif action=='2':
        add_cow(db)
elif action== '3':
        edit_cow(db)
elif action== '4':
        delete_cow(db)



