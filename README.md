# 白月光吸引力动力学方程研究项目（Moonlight Dynamics）

> 让情绪进入坐标系，让幻想拥有可计算的轨迹。  
> Let emotions enter the coordinate system, and let imagination become a computable trajectory.

---

## 一、项目背景 / Project Background

**白月光吸引力动力学方程研究项目（Moonlight Dynamics）** 是一个带有心理动力学色彩的 Python 项目，旨在用数学模型模拟“白月光”对个体幻想频率、自控力与情绪稳定性的影响。

**Moonlight Dynamics** is a Python project with a psychodynamic modeling style. It aims to simulate how a “moonlight figure” influences fantasy frequency, self-control, and emotional stability.

项目基于知乎网友 **Michael Jackson** 提出的原始公式：

```text
白月光的杀伤力 = （白月光给你的峰值体验 − 你最近几天的平均体验） × 当前的空闲度
```

```text
Attraction Impact of Moonlight Figure = (Peak Experience Given by the Moonlight Figure − Recent Average Experience) × Current Idle Degree
```

在此基础上，**DustyYu** 与 **墨鱼小丸子** 共同优化模型，引入空闲程度、自控程度、幻想强度、现实修正项与情绪基线等变量，构建了一个用于模拟幻想频率、自控力与情绪稳定性之间关系的心理动力学模型。

Based on this original formula, **DustyYu (Jiahao)** and **Moyu Xiaowanzi (Wang Zimo)** jointly optimized the model by introducing variables such as idle degree, self-control degree, fantasy intensity, reality correction, and emotional baseline. The result is a psychodynamic model for simulating the relationship among fantasy frequency, self-control, and emotional stability.

---

## 二、核心定义 / Core Definitions

本项目中的核心变量定义如下：

The core definitions used in this project are listed below:

### 1. 空闲程度 / Idle Degree

```text
空闲程度 = 1 − 学习或其他爱好对时间的占用率
```

```text
Idle Degree = 1 − Time Occupation Rate of Study or Other Hobbies
```

### 2. 自控程度 / Self-Control Degree

```text
自控程度 = 1 − 在空闲时间自动开始幻想白月光的频率
```

```text
Self-Control Degree = 1 − Frequency of Automatically Fantasizing About the Moonlight Figure During Idle Time
```

### 3. 幻想总频率 / Total Fantasy Frequency

```text
幻想总频率 = 空闲程度 × (1 − 自控程度)
```

```text
Total Fantasy Frequency = Idle Degree × (1 − Self-Control Degree)
```

---

## 三、主方程 / Main Equation

最终模型公式如下：

The final model equation is shown below:

```text
K = ((1 - L - αR)(H₀ - βR)F_intensity · B - (E₀ + β_R R)) · ((1 - L - αR)^α) / (C₀ - γR)
```

其中，`K` 表示白月光吸引力或情绪驱引力的综合强度。

Here, `K` represents the integrated intensity of moonlight attraction or emotional driving force.

### 变量说明 / Variable Notes

| 符号 / Symbol | 中文含义 | English Meaning |
|---|---|---|
| `K` | 白月光吸引力 / 情绪驱引力强度 | Moonlight attraction / emotional driving force intensity |
| `L` | 学习或其他爱好对时间的占用率 | Time occupation rate of study or other hobbies |
| `R` | 现实修正项 | Reality correction term |
| `α` | 空闲程度对幻想放大的非线性指数 | Nonlinear exponent of idle-degree amplification |
| `H₀` | 白月光带来的峰值体验 | Peak experience brought by the moonlight figure |
| `β` | 现实修正对峰值体验的削弱系数 | Weakening coefficient of reality correction on peak experience |
| `F_intensity` | 幻想强度 | Fantasy intensity |
| `B` | 白月光基础吸引因子 | Basic attraction factor of the moonlight figure |
| `E₀` | 最近几天的平均体验 / 情绪基线 | Recent average experience / emotional baseline |
| `β_R` | 现实修正对情绪基线的影响系数 | Influence coefficient of reality correction on emotional baseline |
| `C₀` | 初始自控力 | Initial self-control capacity |
| `γ` | 现实修正对自控力的消耗系数 | Consumption coefficient of reality correction on self-control |

---

## 四、项目结构说明 / Project Structure

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

## 五、模块说明 / Module Description

| 文件 / File | 中文功能说明 | English Description |
|---|---|---|
| `LICENSE` | 项目许可证文件，声明本项目使用 MIT License。 | License file declaring that this project uses the MIT License. |
| `README.md` | 项目的主要说明文档，包含背景、模型公式、运行方式、作者与致谢。 | Main project documentation, including background, model equation, usage, authors, and acknowledgements. |
| `readme.md` | 备用或早期版本说明文件，可用于记录草稿、旧版本说明或实验性描述。 | Backup or earlier README file for drafts, legacy notes, or experimental documentation. |
| `白月光驱引动力力学方程像basic.py` | 基础版本脚本，用于初步实现白月光驱引动力方程与基础图像绘制。 | Basic script for initial implementation of the moonlight driving-force equation and simple visualization. |
| `白月光驱引动力力学方程像-净定义域.py` | 引入净定义域约束，避免模型在无效参数区域内产生不可解释结果。 | Adds clean-domain constraints to prevent uninterpretable results in invalid parameter regions. |
| `白月光驱引动力力学方程像-图像优化-代码优化.py` | 对图像输出与代码结构进行优化，提高可读性与运行稳定性。 | Optimizes visualization output and code structure for readability and runtime stability. |
| `白月光驱引动力力学方程像-图像优化-代码优化-说明优化.py` | 在图像与代码优化基础上进一步增强注释、说明与变量解释。 | Further improves comments, explanations, and variable descriptions based on visualization and code optimization. |
| `白月光驱引动力力学方程像-图像优化-代码优化-说明优化-参考标准.py` | 加入参考标准与参数规范，使模型结果更便于对照与解释。 | Adds reference standards and parameter conventions to make model outputs easier to compare and interpret. |
| `白月光驱引动力力学方程像-图像优化-代码优化-说明优化-参考标准-Final Edition.py` | 最终版脚本，整合图像优化、代码优化、说明优化与参考标准，是推荐运行入口。 | Final edition script integrating visualization optimization, code optimization, documentation refinement, and reference standards; recommended entry point. |

---

## 六、运行方式 / How to Run

请确保本地已经安装 Python，并在项目根目录下运行最终版脚本：

Make sure Python is installed locally, then run the final edition script in the project root directory:

```bash
python "白月光驱引动力力学方程像-图像优化-代码优化-说明优化-参考标准-Final Edition.py"
```

如果脚本中使用了第三方库，例如 `numpy`、`matplotlib` 等，请根据实际代码提前安装依赖：

If the script uses third-party libraries such as `numpy` or `matplotlib`, install the required dependencies according to the actual code:

```bash
pip install numpy matplotlib
```

---

## 七、作者与贡献者 / Authors and Contributors

1. **DustyYu** — 模型构建与代码实现  
   **DustyYu** — Model construction and code implementation

2. **墨鱼小丸子** — 理论优化与变量定义  
   **Moyu Xiaowanzi ** — Theoretical optimization and variable definition

3. **灵感来源：知乎网友 Michael Jackson 的原始公式**  
   **Inspired by:** the original formula proposed by Zhihu user Michael Jackson

4. **Vibe Coding — Gemini 3.5 Flash/Copilot/Gemini 3.1 Pro/ChatGPT 5.5-Thinking**

---

## 八、许可证与致谢 / License and Acknowledgements

本项目使用 **MIT License**。

This project is licensed under the **MIT License**.

致谢所有在深夜讨论公式的人类，他们让情绪成为了可计算的变量。

Special thanks to all the humans who discussed equations late at night; they made emotions become computable variables.

```text
情绪不是误差项，
而是另一种尚未被完全建模的动力。
```

```text
Emotion is not an error term;
it is another force that has not yet been fully modeled.
```

---

## 九、项目气质 / Project Vibe

这是一个介于科研、心理建模与 vibe coding 之间的项目。

This project lives somewhere between research, psychological modeling, and vibe coding.

它试图用变量表达不可言说的情绪，用方程追踪反复出现的幻想，用图像描绘自控力与心动之间的拉扯。

It tries to express unspeakable emotions through variables, track recurring fantasies through equations, and visualize the tension between self-control and emotional attraction.

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

---

## 十、免责声明 / Disclaimer

本项目仅用于数学建模、代码实验、情绪表达与娱乐性研究，不构成心理咨询、医学建议或现实关系决策依据。

This project is intended only for mathematical modeling, coding experiments, emotional expression, and entertainment-oriented research. It does not constitute psychological counseling, medical advice, or a basis for real-life relationship decisions.

---

## Eleven. Final Note / 最终注记

```text
Moonlight Dynamics is not only a formula.
It is a small attempt to turn longing into a graph,
turn emotional gravity into code,
and turn late-night thoughts into something that can finally be run.
```

```text
Moonlight Dynamics 不只是一个公式。
它是一次把想念变成图像、
把情绪引力写成代码、
把深夜念头保存为可运行文件的小型尝试。
```
