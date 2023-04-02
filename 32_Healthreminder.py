from tkinter import *
import customtkinter
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# base = Tk()
base1 = customtkinter.CTk()
base1.geometry("420x520")
base1.title("CustomTkinter Test")


def set_timer():
    get_hour = int(Time.get())
    get_min = int(Time2.get())

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


# base1.title("Health reminder")
# base1.geometry('400x400')

# img2 = Image.open("label2.png")
# resized_img2 = img2.resize((390, 100))
# tkimg2 = ImageTk.PhotoImage(resized_img2)

# customtkinter.CTkLabel(master=base1, image=tkimg2).grid(row=1, column=2)

# base_label = customtkinter.CTkLabel(master=base1, text="Set time duration", font=("Papyrus", 12))
# base_label.place(x=10, y=240)
img = PhotoImage(file="label2.png")

button1 = customtkinter.CTkButton(master=base1, image=img, text="", width=390, height=100, hover=True)
button1.place(relx=0.0, rely=0.0)

label = customtkinter.CTkLabel(master=base1,
                               text="Welcome to Heath reminder app.",
                               width=120, height=25, corner_radius=8, text_font=('Garamond', 15))
label.place(relx=0.15, rely=0.4)

label4 = customtkinter.CTkLabel(master=base1, text="_______________________________________________",
                                width=120, height=25, corner_radius=8, text_font=('Helvetica', 12))
label4.place(relx=0.0, rely=0.45)

label2 = customtkinter.CTkLabel(master=base1,
                                text="Your total number of working hours in a Day!!",
                                width=120, height=25, corner_radius=8, text_font=('Helvetica', 12))
label2.place(relx=0.1, rely=0.6)

label3 = customtkinter.CTkLabel(master=base1, text="Set Hours: ",
                                width=120, height=25, corner_radius=8, text_font=('Helvetica', 12))
label3.place(relx=0.1, rely=0.66)

Time = customtkinter.CTkEntry(master=base1,
                              width=120,
                              height=25,
                              corner_radius=10)

Time.place(relx=0.4, rely=0.66)
hint = customtkinter.CTkLabel(master=base1, text="(In Hours)",
                              width=120, height=25, corner_radius=8, text_font=('Helvetica', 12))
hint.place(relx=0.685, rely=0.66)

label5 = customtkinter.CTkLabel(master=base1,
                                text="Duration between breaks",
                                width=120, height=25, corner_radius=8, text_font=('Helvetica', 12))
label5.place(relx=0.1, rely=0.75)

label3 = customtkinter.CTkLabel(master=base1, text="Set Duration: ",
                                width=120, height=25, corner_radius=8, text_font=('Helvetica', 12))
label3.place(relx=0.1, rely=0.81)

Time2 = customtkinter.CTkEntry(master=base1,
                               width=120,
                               height=25,
                               corner_radius=10, )
Time2.place(relx=0.4, rely=0.81)
hint = customtkinter.CTkLabel(master=base1, text="(In Minutes)",
                              width=120, height=25, corner_radius=8, text_font=('Helvetica', 12))
hint.place(relx=0.685, rely=0.81)

button1 = customtkinter.CTkButton(master=base1, text='SET', hover=True, border_width=1, text_color='black',
                                  fg_color='#5FF478',
                                  hover_color='#90DFEF', command=set_timer)
button1.place(relx=0.3, rely=0.9)

# duration = Entry(base, width="20", font=("poppins", 15))
# duration.place(x=150, y=240)

# base_dis = Label(base, text="Welcome to Heath reminder app.", font=("Garamond", 15))
# base_dis2 = Label(base, text=" Your total number of working hours in a Day!!", font=("Papyrus", 12))
# base_dis.place(x=50, y=150)
# base_dis2.place(x=10, y=200)
#
# butt = Button(base,text="SET", fg='black', bg='green', width='10', relief="raised")
# butt.place(x=150, y=300)


base1.mainloop()
