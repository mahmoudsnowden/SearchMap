from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
from Bridth import *
from Depth import *
from A_search import *



root = Tk()
root.title('SearchLocation')
frame_1= Frame(root)
frame_1.grid(row=0,column=1,columnspan=3)
frame_1.config(width=300,heigh=5,relief=RIDGE)
# label

my_label_1 = Label(root, text='From', background='#85adad')
my_label_1.grid(row=1, column=0, sticky='snew')
my_label_2 = Label(root, text='To', background='#85adad', width=12)
my_label_2.grid(row=3, column=0, sticky='snew')
# my_label_3 = Label(root, text=, background='#85adad', width=12)
# my_label_3.grid(row=5, column=0, sticky='snew')

# radiobutton
seartech = StringVar()
cheek_1 = Radiobutton(root, text='BFS', variable=seartech, value="BFS")
cheek_1.grid(row=4, column=0, sticky='snew')
cheek_2 = Radiobutton(root, text='DFS', variable=seartech, value="DFS")
cheek_2.grid(row=4, column=1, sticky='snew')
cheek_3 = Radiobutton(root, text='A*', variable=seartech, value="A*")
cheek_3.grid(row=4, column=2, sticky='snew')

# ---------------
# dropminu
clicked_1 = StringVar()
e1 = OptionMenu(root, clicked_1,
                'Giza',
                'Cairo',
                'October',
                'Madinati',
                'Alshuruq',
                'Aleubur',
                'ShubraAlkhayma',
                'Qalyub',
                'Smadun',
                'Belbeis',
                'Sadat',
                'SirsAlliyan',
                'Banha',
                'MinyaAlqamh',
                'Zagzig',
                'Alsharqia',
                'Menouf',
                'ShbeenElkoom',
                'AbuKabir',
                'Alshuada',
                'Tala',
                'Mtgmer',
                'Tanta',
                'KafrElzayat',
                'Shabrakhit',
                'Damanhour',
                'Desouq',
                'KafrElsheikh',
                'AlmahallaAlkubra',
                'Mansoura',
                'Sinbillawain',
                'Abushaqq'
                
                ).grid(row=1, column=1, columnspan=3, sticky='snew')

clicked_2 = StringVar()
e2 = OptionMenu(root, clicked_2,
                'Giza',
                'Cairo',
                'October',
                'Madinati',
                'Alshuruq',
                'Aleubur',
                'ShubraAlkhayma',
                'Qalyub',
                'Smadun',
                'Belbeis',
                'Sadat',
                'SirsAlliyan',
                'Banha',
                'MinyaAlqamh',
                'Zagzig',
                'Alsharqia',
                'Menouf',
                'ShbeenElkoom',
                'AbuKabir',
                'Alshuada',
                'Tala',
                'Mtgmer',
                'Tanta',
                'KafrElzayat',
                'Shabrakhit',
                'Damanhour',
                'Desouq',
                'KafrElsheikh',
                'AlmahallaAlkubra',
                'Mansoura',
                'Sinbillawain',
                'Abushaqq'
                ).grid(row=3, column=1, columnspan=3, sticky='snew')

# -----------------------
def Bstart():
    if seartech.get() == 'BFS':
        tryimg = my_Bridth.Bridth_1(clicked_1.get(), clicked_2.get())

    elif seartech.get() == 'DFS':
        tryimg = my_Depth.Depth_1(clicked_1.get(), clicked_2.get())
        
    elif seartech.get() == 'A*':
        tryimg = my_Asearch.search_1(clicked_1.get(), clicked_2.get())
    else:
        print("errror")
# ---------------------------
# buttonToShow
b2 = Button(root, text='Gooo!',background='#476b6b', command=Bstart)
b2.grid(row=8, column=0, columnspan=4, sticky='snew')

# buttonToExit
b1 = Button(root, text='Exit',background="#476b6b", command=root.quit)
b1.grid(row=9, column=0, columnspan=4, sticky='snew')

root.mainloop()
