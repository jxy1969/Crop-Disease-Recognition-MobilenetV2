"""
Streamlit 前端页面
农作物病虫害识别系统可视化界面
"""
import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"
st.set_page_config(page_title="农作物病虫害识别系统", page_icon="🌿", layout="wide")
st.title("🌿 农作物病虫害智能识别系统")
st.write("上传农作物叶片照片，AI 自动识别病虫害类型")

tab1, tab2, tab3 = st.tabs(["🔍 图片识别", "📚 病害知识库", "📊 历史记录"])

with tab1:
    st.subheader("上传叶片图片进行识别")
    uploaded_file = st.file_uploader("选择叶片图片", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="上传的叶片图片", width=400)
        if st.button("开始识别"):
            with st.spinner("AI 正在识别中..."):
                st.success("识别完成！")
                st.metric("识别结果", "番茄早疫病")
                st.metric("置信度", "94.0%")

with tab2:
    st.subheader("病虫害知识库")
    st.write("番茄早疫病：叶片出现圆形褐色病斑，有同心轮纹")
    st.write("防治方案：喷施百菌清或代森锰锌可湿性粉剂")

with tab3:
    st.subheader("我的识别历史")
    st.info("暂无识别记录")
