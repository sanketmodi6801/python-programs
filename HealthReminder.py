from tkinter import *
import customtkinter
from plyer import notification
from tkinter import messagebox
import time

base1 = customtkinter.CTk()
base1.geometry("420x520")
base1.title('Health reminder')


def set_timer():
    get_hour = int(time1.get())
    get_min = int(time2.get())

    if get_hour == "" or get_min == "":
        messagebox.showwarning('Error', 'Time not entered...')

    else:
        mins = get_hour * 60
        loops = int(mins / get_min)
        print(loops)
        messagebox.showinfo('Notification', 'Notification set.')
        base1.destroy()

        for i in range(loops):
            notification.notify(title='Healthy reminder', message="Take Break, Drink Water and Relax ",
                                app_icon='bell_icon.ico', toast=True, timeout=15)
            time.sleep(int(get_min))


img = PhotoImage(file='label2.png')
button1 = customtkinter.CTkButton(master=base1, image=img, text='', width=390, height=100)
button1.place(relx=0.0,rely=0.0)

label1 = customtkinter.CTkLabel(master=base1, text='Welcome to Health Reminder app', width=120, height=25,
                                corner_radius=8, text_font=('Garamond', 15))
label1.place(relx=.15, rely=0.4)

label2 = customtkinter.CTkLabel(master=base1, text='_______________________________________________', width=120, height=25,
                                corner_radius=8, text_font=('Helvetica', 15))
label2.place(relx=0.0, rely=0.45)

label3 = customtkinter.CTkLabel(master=base1, text='Your total number of working hours in a day', width=120, height=25,
                                corner_radius=8, text_font=('Helvetica', 15))
label3.place(relx=0.1, rely=0.6)

label4 = customtkinter.CTkLabel(master=base1, text='Set Hours', width=120, height=25,
                                corner_radius=8, text_font=('Helvetica', 15))
label4.place(relx=0.1, rely=0.66)

time1 = customtkinter.CTkEntry(master=base1, width=120, height=25, corner_radius=10)
time1.place(relx=0.4,rely=0.66)

hint1 =customtkinter.CTkLabel(master=base1, width=120, height=25, text='In Hours')
hint1.place(relx=0.685, rely=0.66)

label5= customtkinter.CTkLabel(master=base1, text='Duration Between breaks', width=120, height=25,
                                corner_radius=8, text_font=('Helvetica', 15))
label5.place(relx=0.1, rely=0.75)

label4 = customtkinter.CTkLabel(master=base1, text='Set Duration', width=120, height=25,
                                corner_radius=8, text_font=('Helvetica', 15))
label4.place(relx=0.1, rely=0.81)

time2 = customtkinter.CTkEntry(master=base1, width=120, height=25, corner_radius=10)
time2.place(relx=0.4,rely=0.81)

hint2 =customtkinter.CTkLabel(master=base1, width=120, height=25, text='In Minutes')
hint2.place(relx=0.685, rely=0.81)

button2 =customtkinter.CTkButton(master=base1, text='SET', hover=True, hover_color='#90DFEF', text_color='black',
                                 fg_color='#5FF478',
                                 command=set_timer)
button2.place(relx=0.3,rely=0.9)

base1.mainloop()

