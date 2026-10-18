"""
数据集工具函数
加载 PlantVillage 数据集，进行划分和预处理
"""
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split


def get_transforms():
    """获取训练和验证数据预处理流程"""
    train_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(20),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    val_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    return train_transform, val_transform


def load_dataset(data_dir, batch_size=32, val_split=0.2):
    """加载数据集并划分训练集/验证集"""
    train_transform, val_transform = get_transforms()
    full_dataset = datasets.ImageFolder(data_dir)
    class_names = full_dataset.classes
    val_size = int(len(full_dataset) * val_split)
    train_size = len(full_dataset) - val_size
    train_dataset, val_dataset = random_split(full_dataset, [train_size, val_size])
    train_dataset.dataset.transform = train_transform
    val_dataset.dataset.transform = val_transform
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=4)
    return train_loader, val_loader, class_names
