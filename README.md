# Crop Disease Recognition System

基于 MobileNetV2 的农作物病虫害图像识别系统，采用前后端分离架构。

> 技术栈：PyTorch · MobileNetV2 · FastAPI · Streamlit · MySQL · PlantVillage Dataset

## 项目简介

本项目实现农作物叶片病虫害的自动识别，使用轻量级 MobileNetV2 卷积神经网络对 PlantVillage 数据集进行迁移学习训练。后端通过 FastAPI 提供模型推理接口，前端使用 Streamlit 构建可视化交互页面，MySQL 存储用户信息、识别记录与病虫害知识库，支持普通用户与管理员权限区分。

## 核心功能

- 图像分类：识别农作物 38 类常见病虫害，输出分类结果与置信度
- 用户鉴权：JWT 实现登录验证，区分普通用户与管理员角色
- 图片推理：支持单张叶片图片上传识别，自动保存历史记录
- 病害知识库：内置各类病虫害症状描述与防治方案
- 模型评估：训练过程损失曲线、准确率曲线、混淆矩阵可视化

## 项目结构

```
Crop-Disease-Recognition-MobilenetV2/
├── model/                  # 模型相关
│   ├── train.py            # MobileNetV2 模型训练脚本
│   └── predict.py          # 模型推理脚本
├── api/                    # FastAPI 后端接口
│   └── main.py             # 主应用，包含登录、推理、知识库接口
├── web/                    # Streamlit 前端页面
│   └── app.py              # 前端交互页面
├── mysql/                  # 数据库脚本
│   └── schema.sql          # 建库建表 SQL
├── utils/                  # 工具函数
│   └── dataset.py          # 数据集加载与预处理
├── requirements.txt        # Python 依赖
└── README.md
```

## 环境依赖

```bash
pip install -r requirements.txt
```

主要依赖：
- torch >= 2.0.0
- torchvision
- fastapi
- uvicorn
- streamlit
- PyJWT
- pymysql
- pandas
- Pillow
- scikit-learn
- matplotlib

## 快速开始

### 1. 启动 MySQL 数据库

```bash
mysql -u root -p < mysql/schema.sql
```

### 2. 启动后端 API

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. 启动前端页面

```bash
streamlit run web/app.py
```

### 4. 训练模型（可选）

```bash
python model/train.py
```

## 数据集

使用 [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)，包含 38 类农作物叶片图像，涵盖健康与患病状态。

## 作者

姜向阳 · 信阳学院 · 人工智能专业
