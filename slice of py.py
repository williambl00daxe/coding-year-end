# Write your code here :-)
import PySimpleGUI as sg


def create_cow():
    sg.theme('DarkRed2')   # Add some color to the thing
    # All the stuff inside your window.
    layout = [  [sg.Text('Enter the Information for a Cow')],
            [sg.Text('Cow ID '), sg.InputText()],
            [sg.Text('Cow Name '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Cattle Herd', layout)
    # Event get the "values" of the inputs
    event, values = window.read()
    window.close()
    print('You entered ', values[0],values[1])

def read_cow():
    print("You are in read_cow")

def update_cow():
    print('you are updating the cow')

def delete_cow():
    print('what cow do you want to delete')

def show_crud():
    sg.theme('DarkRed2')
    layout = [ [sg.Button('New Cow'),
                sg.Button('Show Cow'),
                sg.Button('Edit Cow'),
                sg.Button('Delete Cow'),
                sg.Button('Quit')] ]

    # Create the Window
    window = sg.Window('Cattle Herd', layout)
    # get the "values" of the inputs
    event, values = window.read()
    window.close()
    return event

# main program
# show form to get CRUD
menu_event = show_crud()
while menu_event != 'Quit':
    if menu_event == 'New Cow':
        create_cow()
    elif menu_event == 'Show Cow':
        read_cow()
    elif menu_event == 'Edit Cow':
        update_cow()
    elif menu_event == 'Delete Cow':
        delete_cow()

    menu_event = show_crud()
