import tkinter
from tkinter import *

top = tkinter.Tk()

root = Tk()
root.title('This is program built by Python!')
root.iconbitmap('favicon.ico')
root.geometry('600x600')

Label(root, text='Hello world').place({'x': 100,  'y': 100})
root.mainloop()
#menu_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#clicked = StringVar()
#clicked.set('Monday')
#dropdown = OptionMenu(root, clicked, *menu_list)
#dropdown.pack()

#Label(root, textvariable=clicked).pack()



#btn = Button(root, text='Click', command=slide)
#btn.pack()


#vertical = Scale(root, from_=0, to=100)
#vertical.pack()

#horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
#horizontal.pack()

#vert_var = StringVar()
#hor_var = StringVar()

#def slide():
 #   vert_var.set(vertical.get())
  #  hor_var.set(horizontal.get())

#vert_label =Label(root, textvariable=vert_var)
#vert_label.pack()
#hor_label = Label(root, textvariable=hor_var)
#hor_label.pack()
#x = 'Shamil'
#new_label = Label(root, text=f'{x}')


#btn = Button(root, text='Click', command=slide)
#btn.pack()

#def show_check_status():
 #   Label(root, text=var.get()).pack()
 #   if var.get() == 'OFF':
#        print('OFF is check')
#    else:
 #       print('ON is check')

#var = StringVar()
#chk = Checkbutton(root, text='Check me', variable=var, onvalue='On', offvalue='Off')
#chk.pack()

#btn = Button(root, text='Click', command=show_check_status)
#btn.pack()
#root.mainloop()

#def clicked():
#    messagebox.askyesno('Title', 'Message')
 #   Label(root, text=response).pack()
 #   if response == 1
 #       Label(root, text='Clicked YES').pack()
 #   elif response == 0:
#        Label(root, text='Clicked YES').pack()

#btn = Button(root, text='Click Me', command=clicked)
#btn.pack()



#def choice_done(value):
#        Label(root, text=value).pack()

#Radiobutton(root, text='Choice1', value='one', variable=choice, command=lambda: choice_done(choice.get())).pack()
#Radiobutton(root, text='Choice2', value='two', variable=choice, command=lambda: choice_done(choice.get())).pack()
#Radiobutton(root, text='Choice3', value='three', variable=choice, command=lambda: choice_done(choice.get())).pack()

#btn = Button(root, text='Click Me', command=lambda: choice_done(choice.get()))
#btn.pack()



#frame = LabelFrame(root, text='I am Label Frame', padx=50, pady=50, bd=0)
#frame.grid(row=0, column=0)

#btn1 = Button(frame, text='Click me')
#btn1.pack()




#image = PhotoImage(file='01d.png')

#mylabel = Label(root, image=image)
#mylabel.pack()

#quit_btn = Button(root, text='Exit', command=root.quit)
#quit_btn.pack()






#user_entry = Entry(root, width=50, bd=5)
#user_entry.pack()
#user_entry.insert(0, 'Please enter your name: ')

#def my_click(number):
#    user_entry.insert(0, int(number) ** 2)

#mybtn = Button(root, text='Click mE', bg='red', fg='white', height=3, command=my_click,
                       #   command=lambda:  my_click(user_entry.get()))
#mybtn.pack()







#root = Tk()
#root.title('This is program built by Python!')


#user_entry = Entry(root, width=50, bd=5)
#user_entry.pack()
#user_entry.insert(0, 'Please enter your name: ')

#def my_click():
#    Label(root, text=f'Hello {user_entry.get}').pack()

#ybtn = Button(root, text='Click mE, bg='red', fg='white', height=3, command=my_click)
#mybtn.pack()







#mylabel1 = Label(root, text='first!')
#mylabel2 = Label(root, text='Second!')
#mylabel3 = Label(root, text='Third!')


#mylabel1.grid(row=0, column=0)
#mylabel2.grid(row=5, column=0)
#mylabel3.pack()

