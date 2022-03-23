#Application for filtering images
#Author: Kamil Sikora
#Date: 03.03.2022
#<kamil.qvr@gmail.com>



from func import *
import tkinter
from tkinter import ANCHOR
from tkinter import filedialog, Text
import cv2


# Values
scale = 1
filepath = ''
tab = []
listbox_clear = True
color_val = 'none'

filter_list = {'orginal': original_img, 'resolution': resolution, 'color': coloro, 'invert': inverted_img,
            'grey': grey_img, 'scale_up': scaleup_img,
            'gauss': gauss_img, 'sepia': sepia_img,
            'convert': convert_img, 'brightness': brightnesschange_img, 'edge': edge_img,
            'erosion': erosion_img, 'dilatation': dilatation_img,
            'skeletonization': skeletonization_img, 'rotate_angle': rotate_angle,
            'flip': flip_img, 'binarization': bin}

my_functions = ('orginal', 'resolution', 'invert', 'color', 'grey', 'scale_up', 'gauss',
                'sepia', 'convert', 'brigthness', 'edge', 'erosion',
                'dilatation', 'skeletonization', 'rotate_angle', 'flip', 'binarization')


# Functions
def use_filter(img, choice):
    global to_save
    for fun in filter_list.keys():
        if choice == fun:
            if choice == 'scale_up':
                try:
                    scale_x = float(get_option.get())
                    scale_y = float(get_option2.get())
                    if scale_x < 0.1 or scale_y < 0.1 or scale_x > 2 or scale_y > 2:
                        l5.pack()
                        l5.config(text='wrong values')
                    else:
                        l3.pack_forget()
                        to_save = filter_list[fun](img, scale_x, scale_y)
                except ValueError:
                    l5.pack()
                    l5.config(text='Wrong value or box is empty !', fg='red', font='Helvetica 18 bold')

            elif choice == 'brightness':
                try:
                    l5.pack_forget()
                    brightness = int(get_option.get())
                    to_save = filter_list[fun](img, brightness)
                except ValueError:
                    l5.pack()
                    l5.config(text='Empty box !', fg='red', font='Helvetica 18 bold')

            elif choice == 'rotate_angle':
                try:
                    l5.pack_forget()
                    rotate_ang = int(get_option.get())
                    to_save = filter_list[fun](img, rotate_ang)
                except ValueError:
                    l5.pack()
                    l5.config(text='Empty box !', fg='red', font='Helvetica 18 bold')

            elif choice == 'resolution':
                try:
                    new_width = int(get_option.get())
                    new_height = int(get_option2.get())
                    l3.pack_forget()
                    to_save = filter_list[fun](img, new_width, new_height)
                except ValueError:
                    l5.pack()
                    l5.config(text='Wrong value or box is empty !', fg='red', font='Helvetica 18 bold')

            elif choice == 'color':
                if color_val == "none":
                    l5.pack()
                    l5.config(text='Choose one option !', fg='red', font='Helvetica 18 bold')
                else:
                    to_save = filter_list[fun](img, color_val)
            else:
                to_save = filter_list[fun](img)


def add_path_list(add):
    text = 'Add file: ' + add
    global listbox_clear
    if listbox_clear:
        listbox.delete(0)
        listbox_clear = False
    listbox.insert(0, text)


def find_name():
    my_path = listbox.get(ANCHOR)
    num = my_path.find('.')
    napis = ""
    for k in range(num-1, (len(my_path)-num), -1):
        if my_path[k] == "/":
            break
        napis = napis + my_path[k]

    reversed = napis[len(napis)::-1]
    return reversed


def save_to_file():
    path_to_save = filedialog.askdirectory(title="Select Directory")
    # print('save to : '+ path_to_save)

    try:
        #print(type(to_save))
        cv2.imshow('save picture below', to_save)
        path_to_save2 = path_to_save + '/' + find_name() + '_' + spin_box.get() + '.png'
        #print(path_to_save2)
        cv2.imwrite(path_to_save2, to_save)
        # print('First click go')
        l5.pack()
        l5.config(text='Successful save file!', fg='green', font='Helvetica 18 bold')
    except NameError:
        # print('First click go')
        l5.pack()
        l5.config(text='First filter picture !', fg='red', font='Helvetica 18 bold')


def add_picture_path():
    l5.pack_forget()
    button_add_picture_text.set('loading...')
    filepath = filedialog.askopenfilename( initialdir="/", title="Select File",
                                           filetypes=(("all files", "*.*"), ("executables", ".exe")))

    if filepath != '':
        tab.append(filepath)
        add_path_list(filepath)

    button_add_picture_text.set('ADD PICTURE')


def spin_layout_1x1(text_val, text_1):
    l6.grid(columnspan=2, row=0, padx=10, pady=5)
    l6.config(text=text_val)
    l7.grid(column=0, row=1, pady=5)
    l7.config(text=text_1)
    get_option.grid(column=1, row=1, pady=5)
    frame2.pack()


def spin_layout_2x2(text_val, text_1, text_2):
    l3.pack()
    frame2.pack(pady=5)
    l6.grid(columnspan=2, row=0, padx=10, pady=5)
    l6.config(text=text_val)
    l7.grid(column=0, row=1, pady=5)
    l7.config(text=text_1)
    l8.grid(column=0, row=2, pady=5)
    l8.config(text=text_2)
    get_option.grid(column=1, row=1, pady=5)
    get_option2.grid(column=1, row=2, pady=5)


def spin_set():
    l5.pack_forget()
    if 'scale_up' == spin_box.get():
        spin_layout_2x2('write from 1 to 2', 'set value x: ', 'set value y: ')

    elif 'resolution' == spin_box.get():
        spin_layout_2x2('write new resolution value','set value x: ','set value y: ')

    elif 'brigthness' == spin_box.get():
        spin_layout_1x1('write value from 0 to 200','set value : ')

    elif 'rotate_angle' == spin_box.get():
        spin_layout_1x1('write angle from 0 to 360', 'set value : ')
    elif 'color' == spin_box.get():
        c1_r.pack()
        c2_g.pack()
        c3_b.pack()
    else:
        l3.pack_forget()
        l6.grid_forget()
        l7.grid_forget()
        l8.grid_forget()
        c1_r.pack_forget()
        c2_g.pack_forget()
        c3_b.pack_forget()
        get_option.grid_forget()
        get_option2.grid_forget()
        frame2.pack_forget()


def listbox_delete():
    listbox.delete(ANCHOR)


def main_prog():
    word1 = listbox.get(ANCHOR)
    # print('cc')
    # print(word1)
    if word1 == '':
        l5.pack(pady=35)
        l5.config(text='SELECT FILE PTAH FROM LIST !', fg='red', font='Helvetica 18 bold')
    elif word1 == 'paths...':
        l5.pack(pady=35)
        l5.config(text='WRONG PATH !', fg='red', font='Helvetica 18 bold')
    else:
        l5.pack_forget()
        use_filter(cv.imread(word1.replace("Add file: ", "")), spin_box.get())


def make_label_short(name, text, font, background):
    new_label1 = tkinter.Label(name,
               text=text,
               anchor='center',
               font=font,
               fg='white',background=background)

    return new_label1


def make_label_long(name, text, anchor, font, fg, backgorund):
    new_label2 = tkinter.Label(name,
               text=text,
               anchor=anchor,
               font=font,
               fg=fg,
               background=backgorund)

    return new_label2


def checkbox_selection():
    print('cos dziala')
    global color_val
    if (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0):
        color_val = 'red'
        l5.pack_forget()
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0):
        color_val = 'green'
        l5.pack_forget()
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1):
        color_val = 'blue'
        l5.pack_forget()
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0):
        color_val = 'none'
    else:
        var1.set(0)
        var2.set(0)
        var3.set(0)
        l5.pack()
        l5.config(text='You must choose only one option !', fg='red', font='Helvetica 18 bold')


# API START HERE
root = tkinter.Tk()                         # create window
root.geometry('755x600')                    # window size
root.resizable(width=False, height=False)   # block resize
root.config(background='#8E8BFF')
root.title("VqApp")


# frames
frame1 = tkinter.Frame(root, heigh=400, bd=2)
frame1.place(x=55, y=350)
frame1.config(background='white')

frame3 = tkinter.Frame(root, heigh=400, bd=2)
frame3.place(x=305, y=40)
frame3.config(background= '#8E8BFF')
# frame3.config(background= 'white')


# options
text_standard = ('Raleway', 15)
main_background_color = '#8E8BFF'

# labels - root
l = make_label_short(root, 'Img Aplication', ('Raleway', 20, 'bold'), main_background_color)
l.pack()
l2 = make_label_short(root, 'list of added photos paths', ('Raleway', 13), main_background_color)
l2.place(x=40, y=60)
l4 = make_label_short(frame3, '1. Add picture \n2. Select photo path'
        '\n3. Click to select option form list \n4. Click button "GO".',
                      text_standard, main_background_color)
l4.pack(pady=20, padx=60)
l3 = make_label_short(frame3,'Set resize prop.', text_standard, main_background_color)
l5 = make_label_short(frame3,'', text_standard, main_background_color)


current_value = tkinter.StringVar()
# c = tkinter.Spinbox(root, from_=1, to=2)
# c.pack()
# c.config(width=2, heigh=2)
spin_box = tkinter.Spinbox(
    frame3,
    from_=1,
    to=len(my_functions),
    values=my_functions,
    textvariable=current_value,
    wrap=False,
    command=spin_set,
    font='Helvetica 12')
spin_box.pack()


# buttons
button_add_picture_text = tkinter.StringVar()
button_add_picture = tkinter.Button(root,
    textvariable=button_add_picture_text,
    bg='#7673F3',
    font=('Raleway', 10, 'bold'),
    fg='white',
    width=11, heigh=2,
    command=add_picture_path)
button_add_picture.place(x=40, y=260)
button_add_picture_text.set('Add Picture')

b1 = tkinter.Button(frame1,
    text='EXIT',
    bg='#7673F3',
    font=('Raleway', 12, 'bold'),
    fg='white',
    width=12, heigh=2,
    command=root.quit)
b1.pack(side=tkinter.BOTTOM, pady=5, padx=5)

b2 = tkinter.Button(frame1,
    text='None',
    bg='#7673F3',
    font=('Raleway', 12, 'bold'),
    fg='white',
    width=12, heigh=2)
b2.pack(side=tkinter.BOTTOM, pady=5, padx=5)

b3 = tkinter.Button(frame1,
    text='save',
    bg='#7673F3',
    font=('Raleway', 12, 'bold'),
    fg='white',
    width=12, heigh=2,
    command=save_to_file)
b3.pack(side=tkinter.BOTTOM, pady=5, padx=5)

b4 = tkinter.Button(root,
    text='Delete',
    bg='#7673F3',
    font=('Raleway', 10, 'bold'),
    fg='white',
    width=10, heigh=2,
    command=listbox_delete)
b4.place(x=150, y=260)

b5 = tkinter.Button(frame3,
    text='GO',
    bg='#7673F3',
    font=('Raleway', 12, 'bold'),
    fg='white',
    width=12, heigh=2,
    command=main_prog)
b5.pack(pady=10)


# listbox
listbox = tkinter.Listbox(
    root,height=9,width = 30,
    selectmode='extended',fg='purple')
listbox.place(x=45, y=90)
listbox.insert(0,'paths...')


# frame
frame2 = tkinter.Frame(frame3, bd=2, bg='#7673F3')


# labels  - frame2
l6 = make_label_short(frame2,'', text_standard, main_background_color)
l7 = make_label_short(frame2,'', text_standard, main_background_color)
l8 = make_label_short(frame2,'', text_standard, main_background_color)


# entry
username = tkinter.StringVar()
get_option = tkinter.Entry(frame2, textvariable=username, width=5)
username2 = tkinter.StringVar()
get_option2 = tkinter.Entry(frame2, textvariable=username2, width=5)


# checkbox
var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
var3 = tkinter.IntVar()
c1_r = tkinter.Checkbutton(frame3, text='RED', variable=var1, onvalue=1, offvalue=0, command=checkbox_selection())
c2_g = tkinter.Checkbutton(frame3, text='GREEN', variable=var2, onvalue=1, offvalue=0, command=checkbox_selection)
c3_b = tkinter.Checkbutton(frame3, text='BLUE', variable=var3, onvalue=1, offvalue=0, command=checkbox_selection)
c1_r.config(background=main_background_color, font = ('Raleway', 12, 'bold'), fg='red')
c2_g.config(background=main_background_color, font = ('Raleway', 12, 'bold'), fg='green')
c3_b.config(background=main_background_color, font = ('Raleway', 12, 'bold'), fg='blue')


if __name__ == "__main__":
    root.mainloop()

'''
OPTIONS - PL

#1 Przeksztalecenia barwne
coloro()                #ZMIANY RGB
grey_img()              #MONOCHROMATYCZNE
inverted_img()          #inwersja
convert_img()
brightnesschange_img()  #korekte poziomu jasnosci
resolution()            #zmiana rozdzielczosci
hist2()                 #HISTOGRAM
two_in_one()            #dodawanie dwoch obrazow, mnozenie, binaryzacja
my_LUT()                #tablica LUT
bin()                   #binaryzacja
rotate_angle60()        #rotacja o 60 i odbicie lustrzane
rotate_img()            #rotacja o 90
scaleup_img()           #zmiana skali
scaledown_img()         #zmiana skali
gauss_img()             #rozmycie gaussa
sepia_img()             #sepia
erosion_img()           #erozja
dilation_img()          #dylatacji
skeletonization_img()   #szkieletyzacja
compression()
andorxor()
'''