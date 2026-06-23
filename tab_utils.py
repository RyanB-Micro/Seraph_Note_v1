
from tkinter import *
from tkinter import ttk
from tkinter import filedialog



main_tab = None
bond_tab = None
node_tab = None
fact_tab = None
source_tab = None
root_window = None


def quit_all():
    # Stop tk window
    root_window.quit()
    root_window.destroy()



def create_main_tab(tab):
    sheet_listbox = Listbox(tab)
    sheet_listbox.pack()




def create_node_tab(node_tab):
    global node_label_entry

    title_label = Label(node_tab, text="Node Control Panel")
    title_label.pack(pady=7)

    entry_frame = Frame(node_tab)
    control_frame = Frame(node_tab)
    #entry_frame.pack(anchor="w", pady=7)
    entry_frame.pack(pady=7)
    control_frame.pack(pady=(7, 0))


    # Label(node_tab, text="Node Name").pack(anchor="w", pady=(7, 0))
    Label(entry_frame, text="Node Name: ").pack(side=LEFT)
    node_label_entry = Entry(entry_frame, width=30)
    node_label_entry.pack(side=LEFT, padx = 7)

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




def setup_window():
    global root_window, main_tab, bond_tab, node_tab, fact_tab, source_tab

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