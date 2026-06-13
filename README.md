# 🌊 SINOSFT-Core-Math

> **SINOSFT 悬浮隧道数学内核 — L1 形式化公理 + L2 鲁棒数值仿真**
>
> 18m巨浪 → 300m防波堤(Kt<0.055) → 1m港内波 → 虚拟水锚 → 轨道平顺度 < 5mm

---

## 五维技术征服矩阵

| 维度 | 技术命题 | 核心指标 | 状态 |
|:---|:---|:---|:---|
| 第一维 | 潮汐虹吸能量自持与高度自适应 | 能量自持、垂直位移 < 5cm | ✅ |
| 第二维 | 防波堤透射系数与线性消波 | Kt < 0.055，港内波高 < 1m | ✅ |
| 第三维 | 600km/h高速列车动态零位移 | 轨道不平顺度 < 5mm | ✅ |
| 第四维 | 扁椭圆壳体全维安全 | 模态避频、屈曲因子 > 3.0 | ✅ |
| 第五维 | 气动-水动耦合安全 | 活塞压力 < 5kPa | ✅ |

---

## 快速开始

git clone https://github.com/SINOSFT/SINOSFT-Core-Math.git
cd SINOSFT-Core-Math
pip install z3-solver pyyaml numpy scipy matplotlib
python spec/verify_static.py
python coupling/wave_train_interaction.py

---

## 许可证

MIT — 保留RWA技术自由
