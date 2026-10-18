-- 农作物病虫害识别系统数据库建表脚本
CREATE DATABASE IF NOT EXISTS crop_disease DEFAULT CHARACTER SET utf8mb4;
USE crop_disease;

CREATE TABLE IF NOT EXISTS user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL,
    email VARCHAR(100),
    role VARCHAR(20) DEFAULT 'user',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS record (
    id INT PRIMARY KEY AUTO_INCREMENT,
    img_path VARCHAR(255),
    result VARCHAR(100),
    username VARCHAR(50),
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS disease_knowledge (
    id INT PRIMARY KEY AUTO_INCREMENT,
    disease_name VARCHAR(100) NOT NULL,
    description TEXT,
    solution TEXT,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO disease_knowledge (disease_name, description, solution) VALUES
('番茄早疫病', '叶片出现圆形褐色病斑，有同心轮纹', '喷施百菌清或代森锰锌可湿性粉剂'),
('番茄晚疫病', '叶片边缘水浸状暗绿色病斑，后变褐色', '加强通风降湿，喷施甲霜灵锰锌'),
('苹果黑星病', '叶片正面淡黄绿色圆形病斑，后变黑', '萌芽前喷石硫合剂，发病期喷苯醚甲环唑'),
('玉米锈病', '叶片背面黄褐色隆起小斑点', '合理施肥，喷施三唑酮或烯唑醇');
