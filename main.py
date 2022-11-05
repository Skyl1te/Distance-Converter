from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Converter"


class MyApp(App):
	
	def __init__(self):
		super().__init__()
		self.label = Label(text='Converter')
		self.miles = Label(text='Miles')
		self.metres = Label(text='Metres')
		self.santimetres = Label(text='Cantimetres')
		self.input_data = TextInput(hint_text='Enter the value (km)', multiline=False)
		self.input_data.bind(text=self.on_text)

	def on_text(self, *args):
		data = self.input_data.text
		if data.isnumeric():
			self.miles.text = 'Miles: ' + str(float(data) * 0.62)
			self.metres.text = 'Metres: ' + str(float(data) * 1000)
			self.santimetres.text = 'Cantimetres: ' + str(float(data) * 100000)
		else:
			self.input_data.text = ''

			
	def build(self):
		box = BoxLayout(orientation='vertical')
		box.add_widget(self.label)
		box.add_widget(self.input_data)
		box.add_widget(self.miles)
		box.add_widget(self.metres)
		box.add_widget(self.santimetres)

		return box


if __name__ == "__main__":
	MyApp().run()
