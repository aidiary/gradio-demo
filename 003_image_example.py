import gradio as gr
import numpy as np


# 画像はndarrayの形で受け取る
def sepia(input_img):
    sepia_filter = np.array(
        [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    )
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img


# 入力は200x200の画像
# 出力は画像
demo = gr.Interface(sepia, gr.Image(shape=(200, 200)), "image")
demo.launch()
