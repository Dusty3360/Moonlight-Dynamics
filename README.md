# Moonlight-Dynamics
A psychological dynamics model exploring fantasy frequency and emotional stability.
🌙 白月光吸引力动力学方程研究项目

Moonlight Dynamics Project

📖 项目简介 | Overview

本项目基于知乎网友 Michael Jackson 提出的原始公式：

白月光的杀伤力 = （白月光给你的峰值体验 − 你最近几天的平均体验） × 当前的空闲度

在此基础上，由 DustyYu 与 墨鱼小丸子 同学共同优化，构建了一个完整的心理动力学模型，用以模拟“幻想频率”与“情绪稳定性”的动态变化。This project extends a public formula proposed on Zhihu, formalizing it into a computational model of emotional dynamics — exploring how fantasy frequency and self‑control interact over time.

🧩 理论基础 | Theoretical Basis

我们定义了两个核心变量：

空闲程度 (S) = 1 − 学习或其他爱好对时间的占用率

自控程度 (C) = 1 − 在空闲时间自动开始幻想白月光的频率

于是总幻想频率为：[F_{\text{total}} = S \times (1 - C)]

并将其带入主方程：[K = (F_{\text{eff}} \cdot B - E_{\text{近期}}) \cdot \frac{S^{\alpha}}{C}]

其中：

( F_{\text{eff}} )：幻想频率 × 幻想强度

( B )：白月光吸引力基准值

( E_{\text{近期}} )：近期情感体验

( \alpha )：情绪敏感系数

( C )：自控力系数

🧠 模型优化 | Model Optimization

墨鱼小丸子同学提出的关键改进：

“空闲程度不是乘的，是幂的。”因此我们引入幂次放大项 ( S^{\alpha} )，并加入娱乐变量 ( R )（游戏、音乐、社交），用于模拟注意力转移的正向作用。

最终模型：[K = ((1 - L - \alpha R)(H_0 - \beta R)F_{\text{intensity}} \cdot B - (E_0 + \beta_R R)) \cdot \frac{(1 - L - \alpha R)^{\alpha}}{C_0 - \gamma R}]

💻 项目结构 | Project Structure

Moonlight-Dynamics/
│
├── src/
│   ├── basic.py
│   ├── 参数优化.py
│   ├── 说明优化.py
│   └── visualization.py
│
├── docs/
│   ├── 方程推导.md
│   ├── 模型说明.md
│   └── 截图/
│
├── examples/
│   └── demo.ipynb
│
├── README.md
├── LICENSE (MIT)
└── requirements.txt

🎮 可视化界面 | Visualization

项目提供交互式滑块界面，可实时调整变量：

正事时间占比

想她本能

理智稳定度

她的杀伤力

游戏时间占比

并生成两张图：

空闲状态下的幻想频率曲线

白月光终极杀伤力 ( K ) 曲线

🧑‍💻 作者与贡献者 | Authors & Contributors

家浩 — 模型构建与代码实现

墨鱼小丸子（王梓墨） — 理论优化与变量定义

灵感来源：知乎网友 Michael Jackson 的原始公式

📜 许可证 | License

本项目采用 MIT License，允许自由使用、修改与分发。This project is released under the MIT License.

🌌 致谢 | Acknowledgements

感谢所有在深夜讨论公式的人类，他们让情绪成为了可计算的变量。Special thanks to everyone who turned late‑night emotions into math.
