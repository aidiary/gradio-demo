import gradio as gr


def greet(name):
    return "Hello " + name + "!"


# Blocksを使うとより柔軟なGUIが作れる
with gr.Blocks() as demo:
    # GUIを記述した順に縦（vertical）に並ぶ
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")

    # ボタンとイベントハンドラの定義
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output)

demo.launch()
