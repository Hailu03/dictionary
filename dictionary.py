
from tkinter import *
import tkinter 
from PIL import Image,ImageTk
from googletrans import Translator
from playsound import playsound
import os
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from datetime import date
import wikipedia
import time

def exit_time():
    exit()

class Example(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        # new frame
        self.menu = Menu(self.parent,tearoff=0)

        self.menu.add_command(label="Exit",command= exit_time)
        # show small button
        self.parent.bind("<Button-3>", self.showMenu)

        self.pack()

    def showMenu(self,event):
        self.menu.post(event.x_root,event.y_root)

screen_en_vi = Tk()
screen_en_vi.title("Hai Translator")
screen_en_vi.geometry("1400x740")
screen_en_vi.iconbitmap("logo.ico")

background = Image.open("background.png")
background_load = ImageTk.PhotoImage(background)
backgroud_screen = Label(screen_en_vi,image = background_load)
backgroud_screen.place(x = 0, y = 100)

tren = Image.open("tren.png")
tren = tren.resize((1590,112))
tren_load = ImageTk.PhotoImage(tren)
tren_screen = Label(screen_en_vi,image = tren_load)
tren_screen.place(x = -10, y = 0)

hai = Image.open("hai.jpg")
hai = hai.resize((250,333))
hai_load = ImageTk.PhotoImage(hai)
hai_screen = Label(screen_en_vi,image = hai_load)
hai_screen.pack(anchor=CENTER,side=BOTTOM)
hai_screen.place(x=550,y = 400)

hai2 = Image.open("hai2.jpg")
hai2 = hai2.resize((270,327))
hai_load2 = ImageTk.PhotoImage(hai2)
hai_screen2 = Label(screen_en_vi,image = hai_load2)
hai_screen2.pack(side=LEFT)
hai_screen2.place(x=10,y = 400)

hai3 = Image.open("hai3.jpg")
hai3 = hai3.resize((250,333))
hai_load3 = ImageTk.PhotoImage(hai3)
hai_screen3 = Label(screen_en_vi,image = hai_load3)
hai_screen3.pack(anchor=CENTER,side=RIGHT)
hai_screen3.place(x=1150,y = 400)

hai4 = Image.open("hai4.jpg")
hai4 = hai4.resize((230,327))
hai_load4 = ImageTk.PhotoImage(hai4)
hai_screen4 = Label(screen_en_vi,image = hai_load4)
hai_screen4.pack(anchor=CENTER,side=RIGHT)
hai_screen4.place(x=300,y = 400)

hai5 = Image.open("hai1.jpg")
hai5 = hai5.resize((315,324))
hai_load5 = ImageTk.PhotoImage(hai5)
hai_screen5 = Label(screen_en_vi,image = hai_load5)
hai_screen5.pack(anchor=CENTER,side=RIGHT)
hai_screen5.place(x=820,y = 400)

exchange = Image.open("exchange.png")
exchange_load = ImageTk.PhotoImage(exchange)
sound = Image.open("sound.png")
sound_load = ImageTk.PhotoImage(sound)

trans = Translator()
engine = pyttsx3.init()


def new_screen():

    def speak_action():
        r= sr.Recognizer()

        def speak(text):
            tts =gTTS(text=text, lang='vi')
            filename = 'voice.mp3'
            tts.save(filename)
            playsound(filename)
            os.remove(filename)

        with sr.Microphone() as source:
            audio_data = r.record(source, duration =5)
        
        try:
            you = r.recognize_google(audio_data, language = "vi")
            ngan_box.insert("1.0",you)
        except:
            you=""

        if you == "":
            robot_brain = "Bạn có thể nói lại không tui chưa nghe rõ"
            hai_box.insert("1.0",robot_brain)
            speak(robot_brain)
        elif "chào" in you:
            robot_brain = "Chào bạn"
            hai_box.insert("1.0",robot_brain)
            speak(robot_brain)
        elif "ngày" in you:
            today = date.today()
            robot_brain = today.strftime("Hôm nay là ngày %d %m %Y")    
            hai_box.insert("1.0",str(robot_brain))
            speak(robot_brain)
        elif "giờ" in you:
            my_format = '%H:%M:%S'
            my_time  = time.localtime()             
            robot_brain = time.strftime(str(my_format), my_time)
            hai_box.insert("1.0",str(robot_brain))
            speak(robot_brain)
        elif you:
            wikipedia.set_lang("vi")
            robot_brain=wikipedia.summary(you,sentences =1)
            hai_box.insert("1.0",str(robot_brain))
            speak(robot_brain)
        elif "tạm" in you:
            robot_brain = "Tạm biệt bạn"
            hai_box.insert("1.0",robot_brain)
            speak(robot_brain)
        else:
            robot_brain = "Bạn có thể nói lại không tui chưa nghe rõ"
            hai_box.insert("1.0",robot_brain)
            speak(robot_brain) 

    newscreen = tkinter.Toplevel()
    newscreen.title("Siri")
    newscreen.geometry("380x480")
    newscreen.iconbitmap("logo.ico")

    ngan_screen21 = Label(newscreen,text = "you",font=(("Arial"),32))
    ngan_screen21.place(x = 10,y=70)

    hai11 = Image.open("hai1.jpg")
    hai11 = hai11.resize((130,134))
    hai11_load = ImageTk.PhotoImage(hai11)
    hai_screen21 = Label(newscreen,image = hai11_load)
    hai_screen21.place(x = 10,y=300)

    ngan_box = Text(newscreen, width=32, height=8, font=("Times", 10),bg="#FFFFFF", undo = True)
    ngan_box.place(x = 170,y= 39 )

    hai_box = Text(newscreen, width=32, height=8,font=("Times", 10),bg="#FFFFFF", undo = True)
    hai_box.place(x = 170,y =309)  

    space_divide = Label(newscreen,text="__________________________________",font= (("Arial"),22))
    space_divide.place(x= 0 ,y = 210)

    semi_colon1 = Label(newscreen,text=":",font= (("Arial"),32))
    semi_colon1.place(x= 147,y = 70)

    semi_colon2 = Label(newscreen,text=":",font= (("Arial"),32))
    semi_colon2.place(x= 147,y = 340)

    def clear():
        hai_box.delete("1.0",END)
        ngan_box.delete("1.0",END)

    speak_button = Button(newscreen,text="Speak",font=(("Arial"),16),command=speak_action)
    speak_button.place(x = 90, y = 200)
    speak_button = Button(newscreen,text="Clear",font=(("Arial"),16),command=clear)
    speak_button.place(x = 220, y = 200)
  
    newscreen.mainloop()

def en_vi(): 

    def vi_en():
        language_en_vi.destroy()
        change_button.destroy()
        title_en_vi.destroy()

        def back():
            language_vi_en.destroy()
            change_button_back.destroy()
            en_vi()

        def enter_button_new(event):
            translate_box.delete("1.0",END)
            text = input_box.get("1.0",END)
            translate_text = trans.translate(text,dest="en")
            translate_box.insert("1.0",translate_text.text)

        def translate_new():
            translate_box.delete("1.0",END)
            text = input_box.get("1.0",END)
            translate_text = trans.translate(text,dest="en")
            translate_box.insert("1.0",translate_text.text)

        def audio_en_new():
            try:
                text = translate_box.get("1.0", END)
            except TypeError:
                pass

            if text == "":
                pass
            else:
                converted_audio = gTTS(text, lang ="en")
                converted_audio.save("translate1.mp3")
                playsound("translate1.mp3")
                os.remove("translate1.mp3")

        def audio_vi_new():
            try:
                text = input_box.get("1.0", END)
            except TypeError:
                pass
            converted_audio = gTTS(text, lang ="vi")
            converted_audio.save("translate.mp3")
            playsound("translate.mp3")
            os.remove("translate.mp3")

        screen_en_vi.bind("<Return>",enter_button_new)

        title_vi_en = Label(text="Hai Translator",font=(("Arial"),55),bg="#F0F0F0",fg="#011128")
        title_vi_en.place(x=480,y = 10)

        language_vi_en = Label(text="V-E",font=(("Arial"),16),bg="#F0F0F0",fg="#011128")
        language_vi_en.place(x=685,y = 140)

        button = Frame(screen_en_vi).pack()
        translate_button = Button(button,text="Translate",font=(("Arial"),10, "bold"),bg="#303030", fg="#FFFFFF",command=translate_new)
        translate_button.place(x=670,y=243)

        sound_input_button1_1 = Button(button,image=sound_load,font=(("Arial"),10, "bold"),bg="#FFFFFF",command=audio_vi_new)
        sound_input_button1_1.place(x= 50,y =280)
        sound_input_button2_1 = Button(image=sound_load,font=(("Arial"),10, "bold"),bg="#FFFFFF",command=audio_en_new) 
        sound_input_button2_1.place(x=1330,y=274) 

        change_button_back = Button(button,image=exchange_load,font=(("Arial"),10, "bold"),bg="#FFFFFF",command=back)
        change_button_back.place(x=685,y=190)


    def clear_text():
        input_box.delete("1.0",END)
        translate_box.delete("1.0",END)

    def enter_button(event):
        translate_box.delete("1.0",END)
        text = input_box.get("1.0",END)
        translate_text = trans.translate(text,dest="vi")
        translate_box.insert("1.0",translate_text.text)

    def translate():
        translate_box.delete("1.0",END)
        text = input_box.get("1.0",END)
        translate_text = trans.translate(text,dest="vi")
        translate_box.insert("1.0",translate_text.text)



    def audio_vi():
        try:
            text = translate_box.get("1.0", END)
        except TypeError:
            pass

        if text == "":
            pass
        else:
            converted_audio = gTTS(text, lang ="vi")
            converted_audio.save("translate.mp3")
            playsound("translate.mp3")
            os.remove("translate.mp3")

    def audio_en():
        try:
            text = input_box.get("1.0", END)
        except TypeError:
            pass

        if text == "":
            pass
        else:
            converted_audio = gTTS(text, lang ="en")
            converted_audio.save("translate1.mp3")
            playsound("translate1.mp3")
            os.remove("translate1.mp3")

    screen_en_vi.bind("<Return>",enter_button)
 
    title_en_vi = Label(text="Hai Translator",font=(("Arial"),55),bg="#F0F0F0",fg="#011128")
    title_en_vi.place(x=480,y = 10)

    language_en_vi = Label(text="E-V",font=(("Arial"),16),bg="#F0F0F0",fg="#011128")
    language_en_vi.place(x=685,y = 140)

    input_box = Text(screen_en_vi, width=44, height=10, font=("Times", 16),bg="#FFFFFF", undo = True)
    input_box.place(x = 150,y= 152 )

    translate_box = Text(screen_en_vi, width=44, height=10,font=("Times", 16),bg="#FFFFFF", undo = True)
    translate_box.place(x = 770,y = 152)  

    button = Frame(screen_en_vi).pack()
    translate_button = Button(button,text="Translate",font=(("Arial"),10, "bold"),bg="#303030", fg="#FFFFFF",command=translate)
    translate_button.place(x=670,y=243)
    clear_button = Button(button,text="Clear",font=(("Arial"),10, "bold"),bg="#303030", fg="#FFFFFF",command=clear_text)
    clear_button.place(x=685,y=326)

    sound_input_button1_1 = Button(button,image=sound_load,font=(("Arial"),10, "bold"),bg="#FFFFFF",command=audio_en)
    sound_input_button1_1.place(x= 50,y =280)
    sound_input_button2_1 = Button(image=sound_load,font=(("Arial"),10, "bold"),bg="#FFFFFF",command=audio_vi) 
    sound_input_button2_1.place(x=1330,y=274) 

    change_button = Button(button,image=exchange_load,font=(("Arial"),10, "bold"),bg="#FFFFFF",command=vi_en,activebackground='blue')
    change_button.place(x=685,y=190)

    menu_bar = Menu(screen_en_vi,tearoff=0)
    file_menu = Menu(menu_bar,tearoff=0)
    file_menu.add_command(label="New",command=clear_text)
    file_menu.add_command(label="Translate",command = translate)

    file_menu.add_command(label="Redo",command=input_box.edit_redo)
    file_menu.add_command(label="Undo",command=input_box.edit_undo)
    menu_bar.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="Exit",command = exit_time)

    language_menu = Menu(menu_bar,tearoff=0)
    language_menu.add_command(label="English-Vietnamese",command=en_vi)
    language_menu.add_command(label="Vietnamese-English",command= vi_en)
    menu_bar.add_cascade(label="Language",menu=language_menu)

    siri_menu = Menu(menu_bar,tearoff=0)
    siri_menu.add_command(label="Siri",command=new_screen)
    menu_bar.add_cascade(label="Siri",menu=siri_menu)
    screen_en_vi.config(menu=menu_bar)

    Example(screen_en_vi)
    screen_en_vi.mainloop()

if __name__ == "__main__":
    en_vi()