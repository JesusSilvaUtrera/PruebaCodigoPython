import gradio as gr


class CustomBlocks(gr.Blocks):
    def __init__(self):
        super().__init__()
        self.name = gr.Textbox(label="Name")
        self.output = gr.Textbox(label="Output Box")
        self.greet_btn = gr.Button("Greet")
        self.greet_btn.click(self.greet_action, self.name, self.output)

    def greet_action(self, button):
        self.output.text = "Hello " + self.name.value + "!"


demo = CustomBlocks()

demo.launch()
