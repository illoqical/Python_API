'''



Author: Kamil Sikora

'''


from func import *
import tkinter
from tkinter import ANCHOR
from tkinter import filedialog, Text
import cv2
import numpy


#Values
scale= 1
filepath = ''
tab= []
funtab = []
funtab = [grey_img,gauss_img, original_img]
listbox_clear = True
print(type(funtab))
funfuntab = { 'orginal': original_img, 'resolution':resolution, 'invert': inverted_img,
            'grey': grey_img, 'scale_up': scaleup_img,
            'gauss': gauss_img, 'sepia': sepia_img,
            'convert': convert_img, 'brigthness': brightnesschange_img,'edge' :edge_img,
            'erosion': erosion_img, 'dilatation': dilatation_img,
            'skeletonization': skeletonization_img, 'rotate_angle': rotate_angle,
            'flip': flip_img, 'binaration': bin}

my_functions = ('orginal','resolution' ,'invert', 'grey', 'scale_up', 'gauss',
                'sepia', 'convert', 'brigthness', 'edge', 'erosion',
                'dilatation', 'skeletonization', 'rotate_angle', 'flip', 'binaration')



#Functions
def Picture2(img, choice):
    global to_save
    for fun in funfuntab.keys():
        if choice == fun:
            if choice == 'scale_up':
                try:
                    scale_x = float(get_option.get())
                    scale_y = float(get_option2.get())

                    if scale_x < 0.1 or scale_y < 0.1 or scale_x > 2 or scale_y > 2 :
                        l5.pack()
                        l5.config(text='wrong values')
                    else:
                        l3.pack_forget()
                        to_save = funfuntab[fun](img, scale_x, scale_y)
                except ValueError:
                    l5.pack()
                    l5.config(text='Wrong value or box is empty !', fg='red', font='Helvetica 18 bold')

            elif choice == 'brigthness':
                # if int(get_option.get()) == '':
                #     l5.pack()
                #     l5.config(text='Empty box !')
                try:
                    l5.pack_forget()
                    brightness = int(get_option.get())
                    to_save = funfuntab[fun](img, brightness)
                except ValueError:
                    l5.pack()
                    l5.config(text='Empty box !', fg='red',font='Helvetica 18 bold')
            elif choice == 'rotate_angle':
                try:
                    l5.pack_forget()
                    rotate_ang = int(get_option.get())
                    to_save = funfuntab[fun](img, rotate_ang)
                except ValueError:
                    l5.pack()
                    l5.config(text='Empty box !', fg='red', font='Helvetica 18 bold')
            elif choice == 'resolution':
                try:
                    new_width = int(get_option.get())
                    new_height = int(get_option2.get())

                    # if scale_x < 0.1 or scale_y < 0.1 or scale_x > 2 or scale_y > 2 :
                    #     l5.pack()
                    #     l5.config(text='wrong values')
                    # else:
                    l3.pack_forget()
                    to_save = funfuntab[fun](img, new_width, new_height)
                except ValueError:
                    l5.pack()
                    l5.config(text='Wrong value or box is empty !', fg='red', font='Helvetica 18 bold')

            else:
                to_save = funfuntab[fun](img)



def add_path_list(add):
    #button_add_picture_text.set('ADD PICTURE')
    text = 'Add file: ' + add
    global listbox_clear
    if listbox_clear:
        listbox.delete(0)
        listbox_clear = False
    listbox.insert(0, text)


def click_button():
    print('wcisnieto przycisk')
    print(list(tab))


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
    path_to_save = filedialog.askdirectory(title = "Select Directory")
    print('save to : '+ path_to_save)

    try:
        #print(type(to_save))
        cv2.imshow('save picture below', to_save)
        path_to_save2 = path_to_save + '/' + find_name() + '_' + spin_box.get() + '.png'
        #print(path_to_save2)
        cv2.imwrite(path_to_save2, to_save)
        print('First click go')
        l5.pack()
        l5.config(text='Successful save file!', fg='green', font='Helvetica 18 bold')
    except NameError:
        print('First click go')
        l5.pack()
        l5.config(text='First filter picture !', fg='red', font='Helvetica 18 bold')


def add_picture_path():
    l5.pack_forget()
    button_add_picture_text.set('loading...')
    filepath = filedialog.askopenfilename( initialdir = "/", title = "Select File",
                                           filetypes=(("all files","*.*"),("executables",".exe")))

    if filepath != '' :
        tab.append(filepath)
        add_path_list(filepath)
    click_button()
    button_add_picture_text.set('ADD PICTURE')


def select_fun(img):
    for fun in funtab:
        if current_value.get() == fun:
            fun(img[1])
    print(current_value.get())

def entry():
    print('abs')


def spin_set():
    #l3.config(text = spin_box.get())
    #return spin_box.get()
    l5.pack_forget()
    if 'scale_up' == spin_box.get():
        scale=0
        l3.pack()
        frame2.pack(pady=5)

        if 'scale_up' == spin_box.get():
            #l6.pack()
            l6.grid(columnspan=2, row=0,padx= 10, pady= 5)
            l6.config(text='write value from 1 to 2')
            l7.grid(column= 0,row=1, pady= 5)
            l7.config(text='set value x: ')
            l8.grid(column= 0,row=2, pady= 5)
            l8.config(text='set value y: ')

        get_option.grid(column= 1,row=1, pady= 5)
        get_option2.grid(column= 1,row=2, pady= 5)
    elif 'resolution' == spin_box.get():
        scale=0
        l3.pack()
        frame2.pack(pady=5)


        #l6.pack()
        l6.grid(columnspan=2, row=0,padx= 10, pady= 5)
        l6.config(text='write new resolution value')
        l7.grid(column= 0,row=1, pady= 5)
        l7.config(text='set value x: ')
        l8.grid(column= 0,row=2, pady= 5)
        l8.config(text='set value y: ')

        get_option.grid(column= 1,row=1, pady= 5)
        get_option2.grid(column= 1,row=2, pady= 5)
    elif 'brigthness' == spin_box.get():
        l6.grid(columnspan=2, row=0,padx= 10, pady= 5)
        l6.config(text='write value from 0 to 200')
        l7.grid(column=0, row=1, pady=5)
        l7.config(text='set value : ')
        get_option.grid(column= 1,row=1, pady= 5)
        frame2.pack()
    elif 'rotate_angle' == spin_box.get():
        l6.grid(columnspan=2, row=0,padx= 10, pady= 5)
        l6.config(text='write angle from 0 to 360')
        l7.grid(column=0, row=1, pady=5)
        l7.config(text='set value : ')
        get_option.grid(column= 1,row=1, pady= 5)
        frame2.pack()

    else:
        l3.pack_forget()
        l6.grid_forget()
        l7.grid_forget()
        l8.grid_forget()
        get_option.grid_forget()
        get_option2.grid_forget()
        frame2.pack_forget()


def fileSelection(self):
    selection = listbox.curselection()
    print(selection)


def listbox_delete():
    listbox.delete(ANCHOR)
    print(tab)


def main_prog():
    word1 = listbox.get(ANCHOR)
    print('cc')
    print(word1)
    if word1 == '':
        #l5.place(x=300, y=600)
        l5.pack(pady=35)
        l5.config(text='SELECT FILE PTAH FROM LIST !',fg='red',font='Helvetica 18 bold')
    elif word1 == 'paths...':
        l5.pack(pady=35)
        l5.config(text='WRONG PATH !',fg='red',font='Helvetica 18 bold')
        print(l5.pack_info())

    else:
        l5.pack_forget()
        kk = cv.imread(word1.replace("Add file: ", ""))
        Picture2(kk,spin_box.get())




#API START HERE
root = tkinter.Tk()  #creat window
root.geometry('800x600') # window size
root.resizable(width=False, height=False) #block resize
root.config(background='#8E8BFF')
root.title("VqApp")

#frame
frame1 = tkinter.Frame(root, heigh=400, bd=2)
frame1.place(x=55, y=350)
frame1.config(background='white')


#labels
l = tkinter.Label(root,
   text='Image Aplication',
   font=('Raleway',20, 'bold'),
   fg='white')
l.pack()
l.config(background='#8E8BFF')

l2 = tkinter.Label(root,
   text='list of added photos paths',
   anchor='center',
   font=('Raleway', 13),
   fg='white')
l2.place(x=40,y=60)
l2.config(background='#8E8BFF')

l4 = tkinter.Label(root,
   text='1. Add picture \n2. Select photo path'
        '\n3. Click to select option form list \n4. Click button "GO".',
   anchor='center',
   font=('Raleway', 15),
   fg='white')
#l3.place(x=300,y=600)
l4.pack(pady=20)
l4.config(background='#8E8BFF')

l3 = tkinter.Label(root,
   text='Set resize prop.',
   anchor='center',
   font=('Raleway', 15),
   fg='white')
#l3.place(x=300,y=600)
l3.config(background='#8E8BFF')

l5 = tkinter.Label(root,
   anchor='center',
   font=('Raleway', 15),
   fg='white')
#l3.place(x=300,y=600)
l5.config(background='#8E8BFF')



current_value = tkinter.StringVar()
# c = tkinter.Spinbox(root, from_=1, to=2)
# c.pack()
# c.config(width=2, heigh=2)
spin_box = tkinter.Spinbox(
    root,
    from_=1,
    to=len(my_functions),
    values=my_functions,
    textvariable=current_value,
    wrap=False,
    command=spin_set,
    #font=Font(family='Helvetica', size=36, weight='bold'))
    font='Helvetica 12')
    #command=select_fun(filepath))
spin_box.pack()


#buttons
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
    # command=select_fun(tab))
    # command=find_name)
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

b5 = tkinter.Button(root,
    text='GO',
    bg='#7673F3',
    font=('Raleway', 12, 'bold'),
    fg='white',
    width=12, heigh=2,
    command=main_prog)
#b4.place(x=300, y=260)
b5.pack(pady=10)


#listbox
listbox = tkinter.Listbox(
    root,height=9,width = 30,
    selectmode='extended',fg='purple')
listbox.place(x=45, y=90)
listbox.insert(0,'paths...')


#frame
frame2 = tkinter.Frame(root, bd=2, bg= '#7673F3')
# frame2.config(background='red')

l6 = tkinter.Label(frame2,
   anchor='center',
   font=('Raleway', 15),
   fg='white')
#l3.place(x=300,y=600)
l6.config(background='#8E8BFF')

l7 = tkinter.Label(frame2,
   anchor='center',
   font=('Raleway', 15),
   fg='white')
#l3.place(x=300,y=600)
l7.config(background='#8E8BFF')

l8 = tkinter.Label(frame2,
   anchor='center',
   font=('Raleway', 15),
   fg='white')
#l3.place(x=300,y=600)
l8.config(background='#8E8BFF')


#entry
username = tkinter.StringVar()
get_option = tkinter.Entry(frame2, textvariable=username,width=5)
username2 = tkinter.StringVar()
get_option2 = tkinter.Entry(frame2, textvariable=username2,width=5)


#photos
# pic = tkinter.PhotoImage(file = 'lenna.png')
# pic.blank()


root.mainloop()

'''
#1 Przeksztalecenia barwne
coloro()                #ZMIANY RGB
grey_img()              #MONOCHROMATYCZNE
inverted_img()          #inwersja
convert_img()
cv.destroyAllWindows()
#2 PUNKT
brightnesschange_img()  #korekte poziomu jasnosci
resolution()            #zmiana rodzielczosci
hist2()                 #HISTOGRAM
two_in_one()            #dodawanie dwoch obrazow, mnozenie,binaryzacja
my_LUT()                #tablica LUT
bin()                   #binaryzacja
cv.destroyAllWindows()


# #3 PRZEKSZTALCENIA GEOMETR
rotate_angle60()    #rotacja o 60 i odbicie lustrzane
rotate_img()        #rotacja o 90
scaleup_img()       #zmiana skali
scaledown_img()     #zmiana skali
cv.destroyAllWindows()

# #4 przekształcenia morfologiczne
gauss_img()
sepia_img()
erosion_img()
dilation_img()
skeletonization_img()
cv.destroyAllWindows()


# #6 TRANSFORMACJA FOURIERA
furrier2()
cv.destroyAllWindows()


# #7 KOMPRESJA STRATNA
compression()
cv.destroyAllWindows()


# #8 PRZETWARZANIE OBRAZOW BINARNYCH  and / or / xor
andorxor()
cv.destroyAllWindows()

'''