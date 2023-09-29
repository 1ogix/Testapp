from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):

    def build(self):
        self.operations = ""
        self.last_was_operator = None
        self.result = TextInput(
            multiline=False, readonly=True, halign='right', font_size=55
        )
        layout = GridLayout(cols=4)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        for button in buttons:
            layout.add_widget(Button(text=button, on_press=self.on_button_press))

        clear_button = Button(text="C")
        clear_button.bind(on_press=self.clear)
        layout.add_widget(clear_button)

        equals_button = Button(text="=")
        equals_button.bind(on_press=self.on_solution)
        layout.add_widget(equals_button)

        layout.add_widget(self.result)
        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        # Handle special cases
        if button_text == 'C':
            self.result.text = ""
        else:
            new_text = current + button_text
            self.result.text = new_text

    def clear(self, instance):
        self.result.text = ""

    def on_solution(self, instance):
        text = self.result.text
        try:
            # Use eval to perform the calculation (unsafe for production use)
            self.result.text = str(eval(self.result.text))
        except Exception:
            self.result.text = "Error"


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
