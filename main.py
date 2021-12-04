import kivy
from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
#from kivy.uix.floatlayout import FloatLayout
import datetime
import ast
import json

kivy.require('1.9.0')

"""
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        
        self.cols = 1
        #2 Grids one with fields and other with button
        self.sub_gride = GridLayout()
        self.sub_gride.cols = 2

        self.sub_gride.add_widget(Label(text="Date: "))
        self.date = TextInput(multiline = False)
        self.sub_gride.add_widget(self.date)

        self.sub_gride.add_widget(Label(text="BreakFast: "))
        self.breakfast = TextInput(multiline = False)
        self.sub_gride.add_widget(self.breakfast)

        self.sub_gride.add_widget(Label(text="Lunch: "))
        self.lunch = TextInput(multiline = False)
        self.sub_gride.add_widget(self.lunch)

        self.sub_gride.add_widget(Label(text="Dinner: "))
        self.dinner = TextInput(multiline = False)
        self.sub_gride.add_widget(self.dinner)

        self.sub_gride.add_widget(Label(text="Others: "))
        self.others = TextInput(multiline = False)
        self.sub_gride.add_widget(self.others)

        self.add_widget(self.sub_gride)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press = self.button_click)
        self.add_widget(self.submit)

    def button_click(self, instance):
        date = self.date.text
        breakfast = self.breakfast.text
        lunch = self.lunch.text
        dinner = self.dinner.text
        others = self.others.text

        print(f'{date}{breakfast}{lunch}{dinner}{others}')
        #reset fields
        self.date.text = ''
        self.breakfast.text = ''
        self.lunch.text = ''
        self.dinner.text = ''
        self.others.text = ''
"""

class MyGrid(Widget):
    date = ObjectProperty(None)
    break_fast = ObjectProperty(None)
    lunch = ObjectProperty(None)
    dinner = ObjectProperty(None)
    others = ObjectProperty(None)

    def btn(self):
        write_to_json(self.date.text,
            self.break_fast.text,
            self.lunch.text,
            self.dinner.text,
            self.others.text
            )
        self.date.text = ''
        self.break_fast.text = ''
        self.lunch.text = ''
        self.dinner.text = ''
        self.others.text = ''
    
def write_to_json(date, breakfast=0, lunch=0, dinner=0, others=0):
    if date == '':
        date = datetime.date.today()
    data = {
        'date': str(date),
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'others': others
    }

    # with open("expenses.txt", 'r+') as file:
    #     list_data = ast.literal_eval(file.read())
    #     print(list_data)
        
    with open("expenses.json",'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["expenses"].append(data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

class ExpenseTracker(App):
    def build(self):
        return MyGrid()

ExpenseTracker().run()
