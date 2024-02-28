import gradio as gr


def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


# ! The Interface class allows you to
demo = gr.Interface(
    fn=greet,  # The function to wrap to an UI
    inputs=[
        "text",
        "slider",
    ],  # The components to use for inputs, should  match the order of arguments in 'fn'
    outputs=[
        "text"
    ],  # The components to use for outputs, should match the number of return values in 'fn'
)

demo.launch(
    share=True
)  # the share=True flag generates a public URL for everyone to join your app in their browser

# You can create Chatbots with gr.Chatbot, using simple tasks or even LLM models.

# ! And for more custom and complex solutions you need to use gr.Blocks
# See https://www.gradio.app/guides/blocks-and-event-listeners for more information

# ! Another example with automatic triggering every time we change the input
# import gradio as gr

# with gr.Blocks() as demo:
#     with gr.Row():
#         num1 = gr.Slider(1, 10)
#         num2 = gr.Slider(1, 10)
#         num3 = gr.Slider(1, 10)
#     output = gr.Number(label="Sum")

#     @gr.on(inputs=[num1, num2, num3], outputs=output)
#     def sum(a, b, c):
#         return a + b + c


# demo.launch()
