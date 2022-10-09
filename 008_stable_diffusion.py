import os
import re

import gradio as gr
import torch
from datasets import load_dataset
from diffusers import StableDiffusionPipeline
from PIL import Image

# HuggingFaceのsettingsで発行する
auth_token = os.getenv("auth_token")

# モデルをロード
model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda:0"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id, use_auth_token=auth_token, revision="fp16", torch_dtype=torch.float16
)
pipe = pipe.to(device)


def infer(prompt):
    images_list = pipe([prompt] * 4, num_inference_steps=50)
    return images_list["sample"]


block = gr.Blocks()

with block:
    with gr.Row():
        text = gr.Textbox(
            label="Enter your prompt",
            show_label=False,
            max_lines=1,
            placeholder="Enter your prompt",
        )
        btn = gr.Button("Generate image")

    # 生成した画像をギャラリー配置
    gallery = gr.Gallery(
        label="Generated images", show_label=False, elem_id="gallery"
    ).style(grid=[2], height="auto")
    btn.click(infer, inputs=text, outputs=gallery)

    # 例を追加
    gr.Examples(
        examples=[
            "the living room of a cozy wooden house with a fireplace, at night, interior design, d & d concept art, d & d wallpaper, warm, digital art. art by james gurney and larry elmore.",
        ],
        fn=infer,
        inputs=text,
        outputs=gallery,
    )

block.launch()
