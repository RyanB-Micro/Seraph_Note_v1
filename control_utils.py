
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import project_utils as prog_ut


project_name = "SeraphNote__New_File__.pk1"
project = None


main_tab = None
bond_tab = None
node_tab = None
fact_tab = None
source_tab = None
root_window = None


sheet_listbox = None


def quit_all():
    # Stop tk window
    root_window.quit()
    root_window.destroy()


def update_label(node_item, new_label):
    pass

def add_sheet(project, label_entry):
    sheet_name = label_entry.get()
    project.create_sheet(sheet_name)
    update_sheet_list(project)

def delete_sheet(project):
    selected_list_index = sheet_listbox.curselection()
    if selected_list_index:
        index = selected_list_index[0]
        selection = sheet_listbox.get(index)
        project.delete_sheet(selection)
        update_sheet_list(project)


def update_sheet_list(project):
    # Get available project sheets
    sheet_listbox.delete(0, END)
    for sheet in project.project_sheets:
        if sheet.sheet_name not in sheet_listbox.get(0, END):
            sheet_listbox.insert(END, sheet.sheet_name)


def detect_sheet_detection(label_entry):
    selected_list_index = sheet_listbox.curselection()
    if selected_list_index:
        index = selected_list_index[0]
        selection = sheet_listbox.get(index)
        print(selection)
        label_entry.delete(0, END)
        label_entry.insert(END, selection)


def create_main_tab(tab, project):
    global sheet_listbox
    sheet_listbox = Listbox(tab)
    sheet_listbox.pack()

    update_sheet_list(project)

    Label(tab, text="Sheet Name: ").pack(side=LEFT)
    label_entry = Entry(tab, width=30)
    label_entry.pack(side=LEFT, padx=7)

    load_sheet_button = Button(tab, text="Load Sheet")
    load_sheet_button.config(command=lambda: detect_sheet_detection(label_entry))
    load_sheet_button.pack()

    add_sheet_button = Button(tab, text="Add Sheet")
    add_sheet_button.config(command=lambda: add_sheet(project, label_entry))
    add_sheet_button.pack()

    remove_sheet_button = Button(tab, text="Remove Sheet")
    remove_sheet_button.config(command=lambda: delete_sheet(project))
    remove_sheet_button.pack()



def create_node_tab(node_tab):
    title_label = Label(node_tab, text="Node Control Panel")
    title_label.pack(pady=7)

    entry_frame = Frame(node_tab)
    control_frame = Frame(node_tab)
    entry_frame.pack(pady=7)
    control_frame.pack(pady=(7, 0))


    Label(entry_frame, text="Node Name: ").pack(side=LEFT)
    label_entry = Entry(entry_frame, width=30)
    label_entry.pack(side=LEFT, padx = 7)

    update_label_button = Button(control_frame, text="Update Node")
    #update_label_button.config(command=lambda: change_node_text())
    update_label_button.pack(pady=7)

    cancel_label_button = Button(control_frame, text="Cancel")
    #cancel_label_button.config(command=lambda: cancel_node_edit())
    cancel_label_button.pack(pady=7)

    delete_node_button = Button(control_frame, text="Delete Node")
    #delete_node_button.config(command=lambda: delete_node())
    delete_node_button.pack(pady=(20,0))



def create_menus(window):
    # Declare menus
    menu = Menu(window)
    file_menu = Menu(menu, tearoff=False)
    info_menu = Menu(menu, tearoff=False)

    # file_menu.add_command(label="Save Project", command=save_project)
    # file_menu.add_command(label="Load Project", command=load_project)
    #
    # info_menu.add_command(label="Python Ver. " + str(platform.python_version()))
    # info_menu.add_command(label="PyGame Ver. " + str(screen_ut.pygame_version))
    # info_menu.add_command(label="Pandas Ver. " + str(pandas_ut.pandas_version))

    # Add menus within eachother
    menu.add_cascade(label="File", menu=file_menu)
    menu.add_cascade(label="Info", menu=info_menu)

    # Add menu to window
    window.config(menu=menu)


def init_control():
    global root_window, main_tab, bond_tab, node_tab, fact_tab, source_tab, project
    project = prog_ut.Project(project_name)

    root_window = Tk()
    root_window.geometry("400x300")
    root_window.protocol("WM_DELETE_WINDOW", quit_all)
    root_window.title("Seraph Command Panel")


    # Create notebook for storing tabs
    notebook = ttk.Notebook(root_window)

    # Declare tab frames
    main_tab = Frame(notebook)
    bond_tab = Frame(notebook)
    node_tab = Frame(notebook)
    fact_tab = Frame(notebook)
    source_tab = Frame(notebook)

    # Generate tab layouts
    create_node_tab(node_tab)
    create_main_tab(main_tab, project)

    # Add tabs to notebook
    notebook.add(main_tab, text="Main Control")
    notebook.add(bond_tab, text="Bond Control")
    notebook.add(node_tab, text="Node Control")
    notebook.add(fact_tab, text="Fact Control")
    notebook.add(source_tab, text="Source Control")
    notebook.pack(expand=1, fill="both")

    # Add tool strip menu
    create_menus(root_window)

    root_window.mainloop()