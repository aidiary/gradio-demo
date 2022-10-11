import gradio as gr
import torch
import whisper

# openai/whisper
# https://huggingface.co/spaces/openai/whisper


device = torch.device("cuda:0")

# whisperモデルをロード
# pip install git+https://github.com/openai/whisper.git
model = whisper.load_model("small").to(device)


def transcribe(audio):
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio).to(device)

    # 言語を認識
    _, probs = model.detect_language(mel)
    lang = max(probs, key=probs.get)
    print(f"Detected language: {lang}")

    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)

    print(result.text)

    return result.text, lang


block = gr.Blocks()

with block:
    with gr.Row():
        audio = gr.Audio(
            label="Input Audio", show_label=False, source="microphone", type="filepath"
        )
        btn = gr.Button("Transcribe")

    text = gr.Textbox(show_label=False)
    lang = gr.Textbox(show_label=False)
    btn.click(transcribe, inputs=[audio], outputs=[text, lang])

block.launch()
