import gradio as gr
from transformers import pipeline

# Text Generation Demo
# https://gradio.app/demos/

# GPT-2の訓練済みモデルをロード
generator = pipeline("text-generation", model="gpt2")


def generate(prompt):
    # GPT-2による文章生成
    result = generator(prompt, max_length=30, num_return_sequences=1)
    return result[0]["generated_text"]


# 入力に与える例を準備できる
examples = [
    ["The Moon's orbit around Earth has"],
    ["The smooth Borealis basin in the Northern Hemisphere covers 40%"],
]

demo = gr.Interface(
    fn=generate,
    inputs=gr.inputs.Textbox(lines=5, label="Input Text"),
    outputs=gr.outputs.Textbox(label="Generated Text"),
    examples=examples,
)

demo.launch()
