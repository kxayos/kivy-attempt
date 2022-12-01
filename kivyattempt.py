import kivy
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button





class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid,self).__init__(**kwargs)

        self.inside = GridLayout()
        self.cols = 1
        
        
        self.inside.cols = 2
        self.inside.add_widget(Label(text="Bot Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Context: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        
    def pressed(self,instance):
        name = self.name.text
        email = self.email.text
        
        




class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
