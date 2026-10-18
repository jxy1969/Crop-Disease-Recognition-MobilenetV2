"""
农作物病虫害模型推理脚本
加载训练好的 MobileNetV2 模型，对单张图片进行预测
"""
import torch
from torchvision import transforms
from PIL import Image

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

CLASS_NAMES = [
    "Apple___Apple_scab", "Apple___Black_rot", "Apple___Cedar_apple_rust",
    "Apple___healthy", "Blueberry___healthy", "Cherry___Powdery_mildew",
    "Cherry___healthy", "Corn___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn___Common_rust", "Corn___Northern_Leaf_Blight", "Corn___healthy",
    "Grape___Black_rot", "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)", "Peach___Bacterial_spot",
    "Peach___healthy", "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy", "Potato___Early_blight", "Potato___Late_blight",
    "Potato___healthy", "Raspberry___healthy", "Soybean___healthy",
    "Squash___Powdery_mildew", "Strawberry___Leaf_scorch",
    "Strawberry___healthy", "Tomato___Bacterial_spot", "Tomato___Early_blight",
    "Tomato___Late_blight", "Tomato___Leaf_Mold", "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite", "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus", "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])


def load_model(model_path="mobilenetv2_crop_disease.pth"):
    """加载训练好的模型"""
    from torchvision.models import mobilenet_v2
    model = mobilenet_v2()
    model.classifier[1] = torch.nn.Linear(model.last_channel, len(CLASS_NAMES))
    model.load_state_dict(torch.load(model_path, map_location=device))
    model = model.to(device)
    model.eval()
    return model


def predict_image(model, image_path):
    """对单张图片进行预测，返回类别名称和置信度"""
    image = Image.open(image_path).convert("RGB")
    tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(tensor)
        probs = torch.nn.functional.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probs, 1)
    class_name = CLASS_NAMES[predicted.item()]
    return class_name, confidence.item()


if __name__ == "__main__":
    model = load_model()
    result, conf = predict_image(model, "test_leaf.jpg")
    print(f"Prediction: {result} (confidence: {conf:.2%})")
