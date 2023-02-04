from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage, Image
import requests
from kivymd.uix.toolbar import MDTopAppBar

input_helper = """
MDTextField:
    hint_text: "Enter chat..."
    helper_text: "make sure to add details..."
    helper_text_mode: "on_focus"
    pos_hint:{'center_x': 0.5, 'center_y': 0.3}
    size_hint_x:None
    width: 500
"""

def sendRequest(user_input):
    response_raw = requests.get(BASE + f"get/?text={user_input}")

    response = str(response_raw.json())
    return response

#web API url
BASE = 'http://aummali.pythonanywhere.com/'

class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'BlueGray'
        screen = Screen()

        #Initialize widgets
        self.outputText = MDRectangleFlatButton(text="", font_size ='11sp', text_color = '#3D3D3D', pos_hint={'center_x': .5, 'center_y': .45}, opacity = 0, md_bg_color = '#EDECEC')

        self.img = Image(source='LOGO.png', allow_stretch=True, keep_ratio=True, size_hint_x=0.55, size_hint_y=.305, pos_hint={'center_x': .5, 'center_y': .74})

        self.mic = Image(source='mic.png', allow_stretch=True, keep_ratio=True, size_hint = (.2, 0.06), pos_hint={'center_x': .35, 'center_y': .48})

        self.micText = Label(text = "Enter text to start ...", font_size = '15sp', color = '#3D3D3D', pos_hint={'center_x': .6, 'center_y': .48})

        self.buttonSend = MDRectangleFlatButton(text='Submit', pos_hint={'center_x': .36, 'center_y': .2}, on_release=self.send_data, size_hint = (.25, .06))

        self.buttonClear = MDRectangleFlatButton(text='Clear', pos_hint={'center_x': .64, 'center_y': .2}, on_release=self.clear_data, size_hint=(.25, .06))

        self.input = Builder.load_string(input_helper)

        self.toolbar = MDTopAppBar(title="Corta.AI", id = 'toolbar',  md_bg_color = '#00003f', elevation = 5, specific_text_color = '#dcdcff', pos_hint = {'top':1.01})

        #Add widgets to screen
        screen.add_widget(self.toolbar)
        screen.add_widget(self.outputText)
        screen.add_widget(self.img)
        screen.add_widget(self.mic)
        screen.add_widget(self.micText)
        screen.add_widget(self.input)
        screen.add_widget(self.buttonSend)
        screen.add_widget(self.buttonClear)

        return screen

    def send_data(self, obj):

        user_input = self.input.text.lower()

        resp = sendRequest(user_input + " Answer this briefly. If this is a math problem then show your work. Answer should be written in paragraph form with no new line.")

        resp = resp.replace("^2", "²")

        word_count = 0
        count = 0

        for i in resp.split():
            word_count += 1
            count += 1
            if count == 11:
                resp = resp.replace(i, f"\n{i}")
                count = 0


        #Hide mic and text
        self.mic.opacity = 0
        self.micText.opacity = 0

        response = resp

        if user_input == "":
            self.mic.opacity = 1
            self.micText.opacity = 1
        else:
            self.outputText.opacity = 1
            self.outputText.text = response

        # empty textbox user input
        self.input.text = ""

    #clears data
    def clear_data(self, obj):
        #Show mic and text
        self.mic.opacity = 1
        self.micText.opacity = 1

        self.outputText.opacity = 0
        self.outputText.text = ""

App().run()