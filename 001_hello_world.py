import gradio as gr


# この引数名がGUIのラベルとして表示される
def greet(name):
    return "Hello " + name + "!"


# 入力がtext、出力がtextのGUIを作成
# 出力を得る関数にgreetを指定
demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()
