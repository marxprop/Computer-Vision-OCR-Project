
import keyboard
from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Yoruba Editor")
root.geometry("1100x1000")

global open_status_name
open_status_name = False

global selected
selected = False

keyboard.add_abbreviation('a+', 'á', match_suffix = True)
keyboard.add_abbreviation('e+', 'é', match_suffix = True)
keyboard.add_abbreviation('e+q', 'ẹ́', match_suffix = True)
keyboard.add_abbreviation('i+', 'í', match_suffix = True)
keyboard.add_abbreviation('o+', 'ó', match_suffix = True)
keyboard.add_abbreviation('o+q', 'ọ́', match_suffix = True)
keyboard.add_abbreviation('u+', 'ú', match_suffix = True)

keyboard.add_abbreviation('a=', 'à', match_suffix = True)
keyboard.add_abbreviation('e=', 'è', match_suffix = True)
keyboard.add_abbreviation('e=q', 'ẹ̀', match_suffix = True)
keyboard.add_abbreviation('i=', 'ì', match_suffix = True)
keyboard.add_abbreviation('o=', 'ò', match_suffix = True)
keyboard.add_abbreviation('o=q', 'ọ̀', match_suffix = True)
keyboard.add_abbreviation('u=', 'ù', match_suffix = True)

keyboard.add_abbreviation('A+', 'Á', match_suffix = True)
keyboard.add_abbreviation('E+', 'É', match_suffix = True)
keyboard.add_abbreviation('E+q', 'Ẹ́', match_suffix = True)
keyboard.add_abbreviation('I+', 'Í', match_suffix = True)
keyboard.add_abbreviation('O+', 'Ó', match_suffix = True)
keyboard.add_abbreviation('O+q', 'Ọ́', match_suffix = True)
keyboard.add_abbreviation('U+', 'Ú', match_suffix = True)

keyboard.add_abbreviation('A=', 'À', match_suffix = True)
keyboard.add_abbreviation('E=', 'È', match_suffix = True)
keyboard.add_abbreviation('E=q', 'Ẹ̀', match_suffix = True)
keyboard.add_abbreviation('I=', 'Ì', match_suffix = True)
keyboard.add_abbreviation('O=', 'Ò', match_suffix = True)
keyboard.add_abbreviation('O=q', 'Ọ̀', match_suffix = True)
keyboard.add_abbreviation('U=', 'Ù', match_suffix = True)

keyboard.add_abbreviation('Sq', 'Ṣ', match_suffix = True)
keyboard.add_abbreviation('sq', 'ṣ', match_suffix = True)

keyboard.add_abbreviation('Eq', 'Ẹ', match_suffix = True)
keyboard.add_abbreviation('eq', 'ẹ', match_suffix = True)

keyboard.add_abbreviation('Oq', 'Ọ', match_suffix = True)
keyboard.add_abbreviation('oq', 'ọ', match_suffix = True)



def new_file():
    my_text.delete("1.0", END)
    root.title("New File - Yoruba Editor")
    status_bar.config(text = "New File     ")
    global open_status_name
    open_status_name = False
    
def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(initialdir = "", title = "Open File", filetypes = (("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All files", "*.*")))
    if text_file:
        global open_status_name
        open_status_name = text_file
    
    name = text_file
    status_bar.config(text = name)
    name = name.split("/")[-1]
    root.title(name + " - Yoruba Editor")
    #open file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    
    my_text.insert(END, stuff)
    #close opened file
    text_file.close()
    
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension = ".*", initialdir = "", title = "Save File", filetypes = (("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text = f'Saved!   {name}')
        name = name.split("/")[-1]
        root.title(name + " - Yoruba Editor")
        
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text.close()

def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text.close()
        
        status_bar.config(text = f'Saved!   {open_status_name}')
    else:
        save_as_file()

def cut_text(e):
    global selected
    
    if e:
        selected = root.clipboard_get()
        
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            
            root.clipboard_clear()
            root.clipboard_append(selected)
      
def copy_text(e):
    global selected
    
    #check for keyboard shortcut
    if e:
        selected = root.clipboard_get()
        
    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)
    
def paste_text(e):
    global selected
    
    if e:
        selected = root.clipboard_get()
        
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)
            
            
def bold_text():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")
    
    #configure tag
    my_text.tag_configure("bold", font=bold_font)
    
    current_tags = my_text.tag_names("sel.first")
    #condition to see for set tag
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")
        
def italic_text():
    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")
    
    #configure tag
    my_text.tag_configure("italic", font=italic_font)
    
    current_tags = my_text.tag_names("sel.first")
    #condition to see for set tag
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

def select_all(e):
    my_text.tag_add('sel', '1.0','end')

def clear_all():
    my_text.delete(1.0, END)
    
#toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill = X)
            
# main frame
my_frame = Frame(root)
my_frame.pack(pady = 5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side = RIGHT, fill = Y)

my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 15), selectbackground = "yellow", selectforeground = "black", undo = True, yscrollcommand = text_scroll.set)
my_text.pack()

text_scroll.config(command = my_text.yview)

#Create Menu
my_menu = Menu(root)
root.config(menu = my_menu)

#File Menu
file_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New", command = new_file)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save", command = save_file)
file_menu.add_command(label = "Save As", command = save_as_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

#Edit Menu
edit_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut", command =lambda: cut_text(False), accelerator = "(Ctrl+x)")
edit_menu.add_command(label = "Copy", command =lambda: copy_text(False), accelerator = "(Ctrl+c)")
edit_menu.add_command(label = "Paste      ", command =lambda: paste_text(False), accelerator = "(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label = "Undo", command = my_text.edit_undo, accelerator = "(Ctrl+z)")
edit_menu.add_command(label = "Redo", command = my_text.edit_redo, accelerator = "(Ctrl+y)")
edit_menu.add_separator()
edit_menu.add_command(label = "Select All", command = lambda: select_all(False), accelerator = "(Ctrl+a)")
edit_menu.add_command(label = "Clear", command = clear_all)#, accelerator = "(Ctrl+y)")

#Edit Binding
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
root.bind('<Control-A>', select_all)
root.bind('<Control-a>', select_all)

# Add Status Bar
status_bar = Label(root, text = 'Ready        ', anchor = E)
status_bar.pack(fill = X, side = BOTTOM, ipady = 5)

#create buttons
bold_button = Button(toolbar_frame, text="Bold", command = bold_text)
bold_button.grid(row = 0, column=0, sticky = W, padx = 1)

italic_button = Button(toolbar_frame, text="Italic", command = italic_text)
italic_button.grid(row = 0, column=1, padx = 1)

undo_button = Button(toolbar_frame, text="Undo", command = my_text.edit_undo)
undo_button.grid(row = 0, column=2, padx = 1)

redo_button = Button(toolbar_frame, text="Redo", command = my_text.edit_redo)
redo_button.grid(row = 0, column=3, padx = 1)

one = Button(my_frame, text="  á  ", command = lambda: keyboard.write('á'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  é  ", command = lambda: keyboard.write('é'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  ẹ́  ", command = lambda: keyboard.write('ẹ́'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  í  ", command = lambda: keyboard.write('í'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  ó  ", command = lambda: keyboard.write('ó'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  ọ́  ", command = lambda: keyboard.write('ọ́'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  ú  ", command = lambda: keyboard.write('ú'))
one.pack(side = LEFT, expand = TRUE)

one = Button(my_frame, text="  à  ", command = lambda: keyboard.write('à'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  ẹ̀  ", command = lambda: keyboard.write('è'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  ẹ̀  ", command = lambda: keyboard.write('ẹ̀'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  ì  ", command = lambda: keyboard.write('ì'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  ò  ", command = lambda: keyboard.write('ò'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  ọ̀  ", command = lambda: keyboard.write('ọ̀'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  ù  ", command = lambda: keyboard.write('ù'))
one.pack(side = LEFT, expand = TRUE)

one1 = Button(my_frame, text="  Á  ", command = lambda: keyboard.write('Á'))
one1.pack(side = LEFT, expand = TRUE)
one2 = Button(my_frame, text="  É  ", command = lambda: keyboard.write('É'))
one2.pack(side = LEFT, expand = TRUE)
one3 = Button(my_frame, text="  Ẹ́  ", command = lambda: keyboard.write('Ẹ́'))
one3.pack(side = LEFT, expand = TRUE)
one4 = Button(my_frame, text="  Í  ", command = lambda: keyboard.write('Í'))
one4.pack(side = LEFT, expand = TRUE)
one5 = Button(my_frame, text="  Ó  ", command = lambda: keyboard.write('Ó'))
one5.pack(side = LEFT, expand = TRUE)
one6 = Button(my_frame, text="  Ọ́  ", command = lambda: keyboard.write('Ọ́'))
one6.pack(side = LEFT, expand = TRUE)
one7 = Button(my_frame, text="  Ú  ", command = lambda: keyboard.write('Ú'))
one7.pack(side = LEFT, expand = TRUE)

one = Button(my_frame, text="  À  ", command = lambda: keyboard.write('À'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  È  ", command = lambda: keyboard.write('È'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  Ẹ̀  ", command = lambda: keyboard.write('Ẹ̀'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  Ì  ", command = lambda: keyboard.write('Ì'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  Ò  ", command = lambda: keyboard.write('Ò'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  Ọ̀  ", command = lambda: keyboard.write('Ọ̀'))
one.pack(side = LEFT, expand = TRUE)
one = Button(my_frame, text="  Ù  ", command = lambda: keyboard.write('Ù'))
one.pack(side = LEFT, expand = TRUE)

status_bar = Label(root, text = 'HELP: \n "=" to apply "doh" tonal mark \n "+" to apply "mi" tonal mark \n Type "q" after "s" or "e" or "o" to apply "dot" underneath them \n \n For example to type "à" >>> Use "a=" \n     To type "á" >>> Use "a+" \n     To type "ẹ̀" >>> Use "e=q" \n     To type "s" >>> Use "sq"', anchor = E, font = ('Helvetica', 10))
status_bar.pack(side = BOTTOM, ipady = 5)

root.mainloop()































