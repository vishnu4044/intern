from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from googletrans import Translator
import speech_recognition as sr
from kivy.core.window import Window
Window.size = (300, 500)
import playsound  # to play saved mp3 file
from gtts import gTTS
import os
import cv2
import pytesseract

tpio="gcjgcjc"
x="en"
y="hi"
num = 1
screen_helper = """
ScreenManager:
    id: screen_manager
    MenuScreen:
    ProfileScreen:
    ProfileScreen2:
    UploadScreen:
<MenuScreen>:
    id: scr_io
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Aknio'
            elevation:5

        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    MDFillRoundFlatIconButton:
        text: "FROM"
        icon:'microphone'
        pos_hint: {'center_x':0.3,'center_y':0.7}
        on_press: root.manager.current = 'profile'
    MDFillRoundFlatIconButton:
        text: "to"
        icon:'speaker'
        pos_hint: {'center_x':0.7,'center_y':0.7}
        on_press:root.manager.current = 'profile2'
    MDTextFieldRect:
        size_hint:.8,.24
        hint_text: "text"
        id:my_input
        pos_hint: {'center_x':0.5,'center_y':0.45}
        normal_color: app.theme_cls.accent_color
    MDLabel:
        text: ''
        id:mylabel
        pos_hint: {'x':0.5,'y':0.1}
    MDFloatingActionButton:
        icon:"text-to-speech"
        pos_hint: {'center_x':0.9,'center_y':0.375}
        on_press: root.git()
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                title: ''
                id:button
                on_action_button:root.navigation_draw()
                icon: 'voice'
                type: 'bottom'
                MDFloatingActionButton:
                    icon:"text-recognition"
                    pos_hint: {'x': .5, 'y':0.2}
                    on_press: root.manager.current = 'upload'



<ProfileScreen>:
    name: 'profile'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Aknio'
            elevation:5
    
        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    MDList:
        OneLineAvatarIconListItem:
            text:'english'
            on_press:root.first()
            on_press: root.manager.current = 'menu'
        OneLineAvatarIconListItem:
            text:'telugu'
            on_press: root.first2()
            on_press: root.manager.current = 'menu'
        OneLineAvatarIconListItem:
            text:'hindi'
            on_press: root.first3()
            on_press: root.manager.current = 'menu'
        OneLineAvatarIconListItem:
            text:'tamil'
            on_press: root.first4()
            on_press: root.manager.current = 'menu'
<ProfileScreen2>:
    name: 'profile2'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Aknio'
            elevation:5

        MDLabel:
            text: ''
            id:mylabel
            pos_hint: {'x':0.5,'y':0.1}
    MDList:
        OneLineAvatarIconListItem:
            text:'english'
            on_press:root.first()
            on_press: root.manager.current = 'menu'
        OneLineAvatarIconListItem:
            text:'telugu'
            on_press: root.first2()
            on_press: root.manager.current = 'menu'
        OneLineAvatarIconListItem:
            text:'hindi'
            on_press: root.first3()
            on_press: root.manager.current = 'menu'
        OneLineAvatarIconListItem:
            text:'tamil'
            on_press: root.first4()
            on_press: root.manager.current = 'menu'
    
<UploadScreen>:
    name: 'upload'
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
    MDFloatingActionButton:
        icon:"camera-iris"
        pos_hint: {'x': .45, 'y':0.2}
        on_press: root.capture()
    MDLabel:
        id:myid
        text:''

    MDToolbar:
    MDFloatingActionButton:
        icon:"home"
        pos_hint: {'x': .45, 'y':0}
        on_press: root.manager.current = 'menu'

"""
def assistant_speaks(output):
    global num
    num += 1
    print("PerSon : ", output)
    toSpeak = gTTS(text=output, lang=y, slow=False)
    file = str(num) + ".mp3"
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)



class MenuScreen(Screen):
    def navigation_draw(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            assistant_speaks("start speaking sir")
            print("Speak1...")
            audio = r.listen(source,phrase_time_limit=10)
        try:
            text = r.recognize_google(audio, language=x)
            print("You : ", text)
            trans = Translator()
            t = trans.translate(text, src=x, dest=y)
            global tpio
            tpio = f'{t.text}'
            print(f'Source: {t.src}')
            print(f'Destination: {t.dest}')
            print(f'{t.origin} -> {t.text}')
            print()
            assistant_speaks(f'{t.text}')
        except:
            return print("not able to reconice")

    def git(self):
        tec=self.ids['my_input'].text
        print(tec)
        trans = Translator()
        t = trans.translate(tec, src=x, dest=y)
        print(f'Source: {t.src}')
        print(f'Destination: {t.dest}')
        print(f'{t.origin} -> {t.text}')
        print()
        assistant_speaks(f'{t.text}')

class ProfileScreen(Screen):
    def first(self):
        global x
        x = "en"
    def first2(self):
        global x
        x = "te"
    def first3(self):
        global x
        x = "hi"
    def first4(self):
        global x
        x = "ta"
    def first5(self):
           assistant_speaks(x)
    pass
class ProfileScreen2(Screen):
    def first(self):
        global y
        y = "en"
    def first2(self):
        global y
        y = "te"
    def first3(self):
        global y
        y = "hi"
    def first4(self):
        global y
        y = "ta"
    def first5(self):
           assistant_speaks(x)
    pass


class UploadScreen(Screen):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        camera.export_to_png("lg.png")
        print("Captured")
        assistant_speaks("captue")
        im = cv2.imread('lg.png')
        # configurations
        config = ('-l eng --oem 1 --psm 3')
        # pytessercat
        text = pytesseract.image_to_string(im, config=config)
        # print text
        text = text.split('\n')
        text
        print(str(text))
        loi="['']"
        if str(text)==loi:
            assistant_speaks("not reconised")
        else:
            assistant_speaks(str(text))


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(ProfileScreen(name='profile2'))
sm.add_widget(UploadScreen(name='upload'))


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        screen = Builder.load_string(screen_helper)
        return screen

DemoApp().run()