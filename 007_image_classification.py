import gradio as gr
import requests
import torch
import torch.nn.functional as F
from torchvision import transforms
from torchvision.models import ResNet18_Weights, resnet18

# 画像分類モデルをロード
model = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
model.eval()

# ImageNetの分類ラベルをロード
response = requests.get(
    "https://raw.githubusercontent.com/gradio-app/mobilenet-example/master/labels.txt"
)
labels = response.text.split("\n")


def predict(image):
    # (1, channels, height, width)
    image = transforms.ToTensor()(image).unsqueeze(0)
    with torch.no_grad():
        prediction = F.softmax(model(image)[0], dim=0)
        confidences = {labels[i]: float(prediction[i]) for i in range(1000)}
        return confidences


demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=5),
    examples=[["data/cheetah.jpg"]],
)
demo.launch()
