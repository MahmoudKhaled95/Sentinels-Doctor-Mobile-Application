'''
***********************************************************************************************
* [File Name]:      main.py
*
* [Description]:    Doctor Mobile application
*
* [Authors]:        Mahmoud Khaled
                    Mohamed Ragab
                    Mahmoud Talal
                    
***********************************************************************************************
'''


import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.core.window import Window
from kivy.config import Config



Config.set('graphics', 'resizable', '0')
 
# fix the width of the window
Config.set('graphics', 'width', '1080')
 
# fix the height of the window
Config.set('graphics', 'height', '2340')
#change window color
Window.clearcolor = (225/255,225/255,225/255,1)

#Automatically Scroll Text Fields Above Mobile Keyboard
Window.keyboard_anim_args = {'d':0.2, 't': 'linear'}
Window.softinput_mode = 'below_target'

#Size of window (Width, height)
#Window.size = (400,630)





class CreateAccountWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text)
                CreateAccount()
                self.reset()
                
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"
    def go_to_patient(self):
        sm.current = "ID"
    pass


class WindowManager(ScreenManager):
    pass


class ID_Window(Screen):
    patientid = ObjectProperty(None)
    def go_to_main(self):
        sm.current = "main"
    def go_to_patient(self):
        sm.current = 'patient'
    def reset(self):
        text1= self.patientid.text
        #print(text1)
    def retrieve_data(self):
    #connect or create database
        self.reset()
        con = sqlite3.connect('patients_db.db')
        cr = con.cursor()
        cr.execute(f'SELECT * from patient')
        all_records=cr.fetchall()
        #print(record1)
        #print(record1[0][0])
        l = []
        for i in range (len(all_records)):
            l.append(all_records[i][0])
        
        if self.patientid.text in l:
            cr.execute(f'SELECT * from patient where user_id = {self.patientid.text}')
            record = cr.fetchall()
            global temp,heart_rate,spo2,covid,pnemoia
            temp = record[0][1]
            heart_rate = record[0][2]
            spo2 = record[0][3]
            covid= record[0][4]
            pnemoia = record[0][5]
            print(record)
            print(temp,heart_rate)
            sm.current = 'patient'
        else:
            WrongID()

    
    pass
class PatientDetails(Screen):
    def write (self):
        self.temp_id.text = temp
        self.heartrate_id.text = heart_rate
        self.spo2_id.text = spo2
        self.covid_id.text = covid
        self.penomia_id.text = pnemoia
    def go_to_id_page(self):
        sm.current = 'ID'
    pass

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(800, 800))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with\n        valid information.'),
                  size_hint=(None, None), size=(800, 800))
    pop.open()

def CreateAccount():
    pop = Popup(title='Account Successfully created',
                  content=Label(text='Your account is Successfully created'),
                  size_hint=(None, None), size=(800, 800))
    pop.open()

def WrongID():
    pop = Popup(title='Wrong ID',
                  content=Label(text='Please enter the correct ID of the Patient'),
                  size_hint=(None, None), size=(800, 800))
    pop.open()

kv = Builder.load_file("senapp.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main"),ID_Window(name='ID'),PatientDetails(name='patient')]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        self.title = 'Sentinel Medical Application'
        return sm


if __name__ == "__main__":
    MyMainApp().run()
