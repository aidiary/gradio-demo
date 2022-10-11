import subprocess

import gradio as gr


# pip install TTS
# TTSモジュールで合成
def tts(text):
    model_name = "tts_models/en/ljspeech/glow-tts"
    out_path = "data/output.wav"
    command = f'tts --text "{text}" --model_name {model_name} --out_path {out_path}'
    subprocess.call(command, shell=True)
    # 音声ファイルを返すとgr.Audioで再生UIが表示される
    return "data/output.wav"


inputs = gr.Textbox(label="Input", max_lines=3)
outputs = gr.Audio(label="Output")

demo = gr.Interface(fn=tts, inputs=inputs, outputs=outputs)
demo.launch()
