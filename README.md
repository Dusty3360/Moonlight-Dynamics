# 白月光吸引力动力学方程研究项目
# Moonlight Dynamics

> 让情绪进入坐标系，让幻想拥有可计算的轨迹。  
> Let emotions enter the coordinate system, and let imagination become a computable trajectory.

---

## 一、项目背景 / Project Background

**白月光吸引力动力学方程研究项目（Moonlight Dynamics）** 是一个使用 Python 构建的情绪动力学模拟项目。

本项目试图用数学模型描述“白月光”这一复杂心理变量对个体幻想频率、自控力、注意力分配与情绪稳定性的影响。它不是严肃心理学诊断工具，而是一种介于数学建模、情绪表达、交互式可视化与 vibe coding 之间的实验性项目。

**Moonlight Dynamics** is an experimental emotional dynamics simulation project built with Python.

It attempts to describe how a “moonlight figure” affects fantasy frequency, self-control, attention allocation, and emotional stability through a mathematical model. This project is not intended as a formal psychological diagnostic tool, but rather as an experimental work combining mathematical modeling, emotional expression, interactive visualization, and vibe coding.

项目最初基于知乎网友 **Michael Jackson** 提出的公式：

```text
白月光的杀伤力 = （白月光给你的峰值体验 − 你最近几天的平均体验） × 当前的空闲度
```

```text
Attraction Impact of Moonlight Figure = (Peak Experience Given by the Moonlight Figure − Recent Average Experience) × Current Idle Degree
```

在此基础上，**DustyYu** 与 **墨鱼小丸子** 对原始公式进行了扩展与优化，引入了空闲程度、自控程度、幻想强度、现实修正项、近期体验基线、替代活动占据度等变量，构建出一个可交互调参、可视化观察的心理动力学模型。

Based on this original formula, **DustyYu** and **墨鱼小丸子** expanded and optimized the model by introducing variables such as idle degree, self-control degree, fantasy intensity, reality correction, recent emotional baseline, and replacement-activity occupation. The result is an interactive and visualizable psychodynamic model.

---

## 二、核心定义 / Core Definitions

本项目中的核心定义如下：

The core definitions used in this project are listed below:

### 1. 空闲程度 / Idle Degree

```text
空闲程度 = 1 − 学习或其他爱好对时间的占用率
```

```text
Idle Degree = 1 − Time Occupation Rate of Study or Other Hobbies
```

空闲程度越高，个体越容易进入无目标思维状态，也越容易被回忆、幻想或情绪惯性重新捕获。

The higher the idle degree, the more likely a person is to enter an undirected mental state, making them more vulnerable to memories, fantasies, or emotional inertia.

---

### 2. 自控程度 / Self-Control Degree

```text
自控程度 = 1 − 在空闲时间自动开始幻想白月光的频率
```

```text
Self-Control Degree = 1 − Frequency of Automatically Fantasizing About the Moonlight Figure During Idle Time
```

自控程度越高，说明个体越能在空闲时间中维持注意力边界，不轻易被白月光变量牵引。

The higher the self-control degree, the better the individual can maintain attentional boundaries during idle time without being easily pulled by the moonlight variable.

---

### 3. 幻想总频率 / Total Fantasy Frequency

```text
幻想总频率 = 空闲程度 × (1 − 自控程度)
```

```text
Total Fantasy Frequency = Idle Degree × (1 − Self-Control Degree)
```

幻想总频率可以理解为：在当前空闲程度与自控程度共同作用下，白月光相关幻想被自动触发的总体概率或强度。

Total fantasy frequency can be understood as the overall probability or intensity of automatically triggered moonlight-related fantasies under the combined influence of idle degree and self-control degree.

---

## 三、主方程 / Main Equation

最终模型公式如下：

The final model equation is shown below:

```text
K = ((1 - L - αR)(H₀ - βR)F_intensity · B - (E₀ + β_R R)) · ((1 - L - αR)^α) / (C₀ - γR)
```

其中，`K` 表示白月光吸引力、情绪驱引力或心理杀伤力的综合强度。

Here, `K` represents the integrated intensity of moonlight attraction, emotional driving force, or psychological impact.

---

## 四、变量说明 / Variable Description

| 符号 / Symbol | 中文含义 | English Meaning |
|---|---|---|
| `K` | 白月光吸引力 / 情绪驱引力强度 | Moonlight attraction / emotional driving force intensity |
| `L` | 学习、工作或其他正事对时间的占用率 | Time occupation rate of study, work, or other serious tasks |
| `R` | 替代活动占用率，例如游戏、运动、兴趣爱好等 | Replacement activity occupation rate, such as gaming, sports, or hobbies |
| `α` | 替代活动对空闲时间的压缩系数 / 空闲放大指数 | Compression coefficient of replacement activities / idle amplification exponent |
| `H₀` | 白月光带来的峰值体验或本能幻想倾向 | Peak experience or instinctive fantasy tendency caused by the moonlight figure |
| `β` | 替代活动对幻想倾向的削弱系数 | Weakening coefficient of replacement activities on fantasy tendency |
| `F_intensity` | 幻想强度修正项 | Fantasy intensity correction term |
| `B` | 白月光固有吸引力 / 固有杀伤力 | Intrinsic attraction / impact factor of the moonlight figure |
| `E₀` | 最近几天的平均体验 / 情绪基线 | Recent average experience / emotional baseline |
| `β_R` | 替代活动带来的即时情绪补偿系数 | Immediate emotional compensation coefficient of replacement activities |
| `C₀` | 初始自控力 / 初始理智水平 | Initial self-control / rational stability level |
| `γ` | 替代活动对自控力的消耗系数 | Consumption coefficient of replacement activities on self-control |

---

## 五、模型直觉 / Model Intuition

这个模型背后的直觉是：

The intuition behind this model is:

```text
当空闲时间增加，而自控力不足时，幻想更容易被触发。
```

```text
When idle time increases and self-control is insufficient, fantasy is more likely to be triggered.
```

```text
当替代活动足够占据时间与注意力时，白月光变量的影响会被削弱。
```

```text
When replacement activities sufficiently occupy time and attention, the influence of the moonlight variable is weakened.
```

```text
当替代活动本身过度消耗理智或带来反向挫败感时，它也可能失去防御效果。
```

```text
When replacement activities themselves consume too much rational stability or create frustration, they may lose their defensive effect.
```

因此，`K` 并不是单纯由“她有多重要”决定，而是由以下因素共同决定：

Therefore, `K` is not determined only by “how important she is,” but by the combined effect of:

```text
白月光峰值体验
近期现实体验
当前空闲程度
自控力水平
替代活动强度
情绪补偿效果
注意力占用程度
```

```text
Peak moonlight experience
Recent real-life experience
Current idle degree
Self-control level
Replacement activity intensity
Emotional compensation effect
Attention occupation level
```

---

## 六、项目结构说明 / Project Structure

```text
白月光吸引力动力学方程研究项目/
│
├── LICENSE
├── README.md
├── readme.md
├── 白月光驱引动力力学方程像basic.py
├── 白月光驱引动力力学方程像-净定义域.py
├── 白月光驱引动力力学方程像-图像优化-代码优化.py
├── 白月光驱引动力力学方程像-图像优化-代码优化-说明优化.py
├── 白月光驱引动力力学方程像-图像优化-代码优化-说明优化-参考标准.py
└── 白月光驱引动力力学方程像-图像优化-代码优化-说明优化-参考标准-Final Edition.py
```

---

## 七、模块说明 / Module Description

| 文件 / File | 中文功能说明 | English Description |
|---|---|---|
| `LICENSE` | 项目许可证文件，声明本项目的开源许可协议。 | License file declaring the open-source license of this project. |
| `README.md` | 项目的主要说明文档，用于介绍项目背景、模型公式、变量定义、运行方式与贡献者信息。 | Main project documentation introducing the background, model equation, variable definitions, usage, and contributors. |
| `readme.md` | 早期说明文档或备用说明文件，可用于保留旧版项目描述。 | Earlier or backup README file that may preserve previous project descriptions. |
| `白月光驱引动力力学方程像basic.py` | 基础版本脚本，可能用于实现最初的方程计算与简单图像展示。 | Basic script, likely used for the initial equation calculation and simple visualization. |
| `白月光驱引动力力学方程像-净定义域.py` | 引入定义域限制的版本，用于减少无效参数组合造成的异常结果。 | Version with domain constraints to reduce invalid results caused by unreasonable parameter combinations. |
| `白月光驱引动力力学方程像-图像优化-代码优化.py` | 对图像展示与代码结构进行优化的版本。 | Version optimized for visualization and code structure. |
| `白月光驱引动力力学方程像-图像优化-代码优化-说明优化.py` | 在图像与代码优化基础上，进一步增强说明文字、注释或交互提示。 | Version that further improves explanations, comments, or interactive guidance based on visualization and code optimization. |
| `白月光驱引动力力学方程像-图像优化-代码优化-说明优化-参考标准.py` | 加入参数参考标准或标定锚点的版本，便于理解不同参数的现实含义。 | Version with parameter references or calibration anchors to help interpret the real-world meaning of different parameters. |
| `白月光驱引动力力学方程像-图像优化-代码优化-说明优化-参考标准-Final Edition.py` | 当前推荐运行的最终版脚本，整合了图像优化、代码优化、说明优化与参考标准。 | Recommended final script integrating visualization optimization, code optimization, explanatory refinement, and reference standards. |

---

## 八、运行方式 / How to Run

### 1. 安装 Python / Install Python

请确保本地已经安装 Python 3。

Make sure Python 3 is installed on your local machine.

---

### 2. 安装依赖 / Install Dependencies

如果脚本使用了 `numpy` 和 `matplotlib`，可以通过以下命令安装依赖：

If the script uses `numpy` and `matplotlib`, install the dependencies with:

```bash
pip install numpy matplotlib
```

---

### 3. 运行最终版脚本 / Run the Final Edition

在项目根目录下运行：

Run the following command in the project root directory:

```bash
python "白月光驱引动力力学方程像-图像优化-代码优化-说明优化-参考标准-Final Edition.py"
```

运行后，程序会打开一个可交互图像窗口。你可以通过滑块调整不同参数，观察幻想频率与白月光吸引力 `K` 的变化趋势。

After running the script, an interactive visualization window will open. You can adjust different parameters using sliders and observe how fantasy frequency and moonlight attraction `K` change.

---

## 九、交互参数说明 / Interactive Parameters

| 参数 / Parameter | 中文说明 | English Description |
|---|---|---|
| `正事时间 L` | 学习、工作或其他正事占据清醒时间的比例。 | Proportion of waking time occupied by study, work, or serious tasks. |
| `想她本能 H₀` | 白月光带来的本能幻想倾向或峰值体验强度。 | Instinctive fantasy tendency or peak experience intensity caused by the moonlight figure. |
| `初始理智 C₀` | 个体初始自控力或理智稳定程度。 | Initial self-control or rational stability level. |
| `她的杀伤力 B` | 白月光变量本身的固有吸引力。 | Intrinsic attraction factor of the moonlight variable. |
| `时间吞噬度 α` | 替代活动占用时间、压缩空闲空间的能力。 | Ability of replacement activities to occupy time and compress idle space. |
| `大脑占据度 β` | 替代活动占据注意力、削弱幻想倾向的能力。 | Ability of replacement activities to occupy attention and weaken fantasy tendency. |
| `理智腐蚀度 γ` | 替代活动对自控力或理智稳定性的消耗程度。 | Degree to which replacement activities consume self-control or rational stability. |
| `即时爽快度 β_R` | 替代活动带来的即时情绪补偿或现实体验提升。 | Immediate emotional compensation or real-life experience improvement brought by replacement activities. |

---

## 十、输出图像说明 / Visualization Description

程序主要展示两条曲线：

The program mainly displays two curves:

### 1. 幻想总频率曲线 / Total Fantasy Frequency Curve

```text
F_total = 空闲程度 × 有效幻想倾向
```

```text
F_total = Idle Degree × Effective Fantasy Tendency
```

该曲线用于观察替代活动 `R` 增加时，幻想频率如何变化。

This curve shows how fantasy frequency changes as replacement activity `R` increases.

---

### 2. 白月光吸引力曲线 / Moonlight Attraction Curve

```text
K = 白月光吸引力 / 情绪驱引力综合强度
```

```text
K = Integrated intensity of moonlight attraction / emotional driving force
```

该曲线用于观察不同替代活动强度下，白月光变量对情绪系统的综合影响。

This curve shows the overall influence of the moonlight variable on the emotional system under different levels of replacement activity.

---

## 十一、作者与贡献者 / Authors and Contributors

1. **DustyYu** — 模型构建与代码实现  
   **DustyYu** — Model construction and code implementation

2. **墨鱼小丸子** — 理论优化与变量定义  
   **墨鱼小丸子** — Theoretical optimization and variable definition

3. **知乎网友 Michael Jackson** — 原始公式灵感来源  
   **Zhihu user Michael Jackson** — Inspiration source of the original formula
4. **LLMs — GPT-5.5 Thinking/Gemini 3.5 Flash/Gemini 3.1 Pro/Copilot**

---

## 十二、许可证 / License

本项目使用 **MIT License**。

This project is licensed under the **MIT License**.

你可以在遵守 MIT License 的前提下自由使用、修改与分发本项目。

You are free to use, modify, and distribute this project under the terms of the MIT License.

---

## 十三、致谢 / Acknowledgements

致谢所有在深夜讨论公式的人类。

Special thanks to all the humans who discussed equations late at night.

```text
他们让情绪成为了可计算的变量。
```

```text
They made emotions become computable variables.
```

也感谢那些曾经无法被命名、无法被归档、无法被关闭的念头。  
它们最终被写进了一个 Python 文件里。

Also thanks to the thoughts that once could not be named, archived, or closed.  
They eventually became part of a Python file.

---

## 十四、免责声明 / Disclaimer

本项目仅用于数学建模、代码实验、情绪表达与娱乐性研究。

This project is intended only for mathematical modeling, coding experiments, emotional expression, and entertainment-oriented research.

本项目不构成心理咨询、医学建议、情感建议或现实关系决策依据。

This project does not constitute psychological counseling, medical advice, relationship advice, or a basis for real-life relationship decisions.

如果你正经历持续的情绪困扰，请优先寻求现实中的朋友、家人或专业人士帮助。

If you are experiencing persistent emotional distress, please consider reaching out to friends, family, or qualified professionals in real life.

---

## 十五、Project Vibe

```text
当空闲度上升，幻想开始获得时间；
当自控力下降，白月光开始获得坐标；
当情绪被写进方程，人终于可以调试自己。
```

```text
When idle degree rises, fantasy gains time;
when self-control falls, the moonlight figure gains coordinates;
when emotion is written into equations, humans finally begin to debug themselves.
```

```text
Moonlight Dynamics 不只是一个公式。
它是一次把想念变成图像、
把情绪引力写成代码、
把深夜念头保存为可运行文件的小型尝试。
```

```text
Moonlight Dynamics is not only a formula.
It is a small attempt to turn longing into a graph,
turn emotional gravity into code,
and turn late-night thoughts into something that can finally be run.
```
