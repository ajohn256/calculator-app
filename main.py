from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

# Window.size = (350,550)




class Calculator(MDApp):
    def __init__(self, **kwargs):
        super(Calculator,self).__init__(**kwargs)
        self.theme_cls.theme_style = 'Dark'
        pass 

    def insert_text(self,text):
        self.manager.get_screen("main").ids.input.text += text
    
    def clear_input(self):
        self.manager.get_screen("main").ids.input.text = ""

    def compute_input(self):
        self.input = self.manager.get_screen("main").ids.input.text
        self.inputx = self.input

        
        try:
            self.ans = eval(self.input)
            if len(str(self.input)) >= 1:
                self.input = ""

            else:pass
            self.clear_input()
            self.manager.get_screen("main").ids.input.text = f"{self.input}\n{self.ans}" 
            self.manager.get_screen("main").ids.input.font_size = 30

            


                 
        
        except Exception as e:
            self.manager.get_screen("main").ids.input.text = "Syntax Error"
            print(e)
        
        
        

       
    def del_char(self):
        self.manager.get_screen("main").ids.input.text = self.manager.get_screen("main").ids.input.text[:-1]
    
    def revert(self):
        # hist = self.manager.get_screen("main").ids.input.text
        try:
            self.manager.get_screen("main").ids.input.text = self.inputx
        except:pass
            # self.manager.get_screen("main").ids.input.text = hist
        
            


    def build(self):
        self.manager = ScreenManager()
        self.manager.add_widget(Builder.load_file("calc.kv"))

        return self.manager


Calculator().run()