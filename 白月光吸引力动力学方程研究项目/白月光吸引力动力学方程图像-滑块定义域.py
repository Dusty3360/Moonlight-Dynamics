import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ================= 1. 设定初始基准值 =================
init_L = 0.6
init_H0 = 0.5
init_C0 = 0.8
init_B = 1.2
init_F_int = 1.0
init_E0 = 0.2

init_alpha_g = 0.8
init_beta_g = 0.7
init_gamma_g = 0.3
init_beta_R = 0.5
alpha_emotion = 2.0

# ================= 2. 创建画布与布局 =================
# 留出底部和左侧的空间给滑块
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
plt.subplots_adjust(bottom=0.42, wspace=0.25)

# ================= 3. 核心计算函数 =================
def calculate_system(L, H0, C0, B, F_int, E0, alpha_g, beta_g, gamma_g, beta_R):
    # 动态计算 R 的安全定义域上限
    max_R_by_S = (1.0 - L) / alpha_g if alpha_g > 0 else 1.0
    max_R_by_C = (C0 - 0.01) / gamma_g if gamma_g > 0 else 1.0
    max_R = min(max_R_by_S, max_R_by_C, 1.0)
    if max_R <= 0: max_R = 0.01
    
    # 生成自变量 R 的数组
    R_vals = np.linspace(0, max_R * 0.99, 200)
    
    # 耦合方程计算
    F_total = (1.0 - L - alpha_g * R_vals) * (H0 - beta_g * R_vals)
    # 幻想频率不能为负数
    F_total = np.maximum(F_total, 0)
    F_eff = F_total * F_int
    
    S = 1.0 - L - alpha_g * R_vals
    S = np.maximum(S, 0)
    
    E_recent = E0 + beta_R * R_vals
    C = C0 - gamma_g * R_vals
    
    # 终极 K 方程
    K_vals = (F_eff * B - E_recent) * (S ** alpha_emotion) / C
    return R_vals, F_total, K_vals

# 初始绘图
R, F_t, K = calculate_system(init_L, init_H0, init_C0, init_B, init_F_int, init_E0, 
                             init_alpha_g, init_beta_g, init_gamma_g, init_beta_R)

line1, = ax1.plot(R, F_t, color='#2ec4b6', linewidth=2.5)
line2, = ax2.plot(R, K, color='#e63946', linewidth=2.5)
vline2 = ax2.axvline(x=R[np.argmin(K)], color='#9b5de5', linestyle=':')

# 初始化图表装饰
ax1.set_title('游戏时间 $R$ 对总幻想频率 $F_{total}$ 的抑制', fontsize=11)
ax1.set_xlabel('游戏时间比例 $R$')
ax1.set_ylabel('总幻想频率')
ax1.grid(True, linestyle='--', alpha=0.5)

ax2.set_title('白月光终极杀伤力 $K$ 随游戏投入的演变', fontsize=11)
ax2.set_xlabel('游戏时间比例 $R$')
ax2.set_ylabel('终极杀伤力 $K$')
ax2.grid(True, linestyle='--', alpha=0.5)

# ================= 4. 创建滑块组件 (放置在画布下方) =================
slider_color = '#dfebd8'
# 这里的坐标对应: [左, 下, 宽, 高]
ax_L      = plt.axes([0.1, 0.28, 0.3, 0.025], facecolor=slider_color)
ax_H0     = plt.axes([0.1, 0.22, 0.3, 0.025], facecolor=slider_color)
ax_C0     = plt.axes([0.1, 0.16, 0.3, 0.025], facecolor=slider_color)
ax_B      = plt.axes([0.1, 0.10, 0.3, 0.025], facecolor=slider_color)

ax_alpha  = plt.axes([0.58, 0.28, 0.3, 0.025], facecolor=slider_color)
ax_beta   = plt.axes([0.58, 0.22, 0.3, 0.025], facecolor=slider_color)
ax_gamma  = plt.axes([0.58, 0.16, 0.3, 0.025], facecolor=slider_color)
ax_betaR  = plt.axes([0.58, 0.10, 0.3, 0.025], facecolor=slider_color)

s_L      = Slider(ax_L, '正事时间比例 L', 0.0, 0.9, valinit=init_L, valfmt='%.2f')
s_H0     = Slider(ax_H0, '初始幻想频率 H0', 0.0, 1.0, valinit=init_H0, valfmt='%.2f')
s_C0     = Slider(ax_C0, '初始自控力 C0', 0.1, 1.0, valinit=init_C0, valfmt='%.2f')
s_B      = Slider(ax_B, '她固有吸引力 B', 0.5, 2.5, valinit=init_B, valfmt='%.2f')

s_alpha  = Slider(ax_alpha, '游戏吸时率 alpha', 0.1, 1.5, valinit=init_alpha_g, valfmt='%.2f')
s_beta   = Slider(ax_beta, '游戏分心率 beta', 0.1, 1.5, valinit=init_beta_g, valfmt='%.2f')
s_gamma  = Slider(ax_gamma, '游戏蚀控率 gamma', 0.0, 1.0, valinit=init_gamma_g, valfmt='%.2f')
s_betaR  = Slider(ax_betaR, '游戏快乐率 beta_R', 0.0, 1.5, valinit=init_beta_R, valfmt='%.2f')

# ================= 5. 实时更新回调函数 =================
def update(val):
    # 提取滑块当前值
    R_vals, F_total, K_vals = calculate_system(
        s_L.val, s_H0.val, s_C0.val, s_B.val, init_F_int, init_E0,
        s_alpha.val, s_beta.val, s_gamma.val, s_betaR.val
    )
    
    # 更新数据线
    line1.set_data(R_vals, F_total)
    line2.set_data(R_vals, K_vals)
    
    # 更新垂直黄金平衡线
    min_idx = np.argmin(K_vals)
    vline2.set_xdata([R_vals[min_idx], R_vals[min_idx]])
    
    # 动态调整坐标轴刻度以防画面出界
    ax1.set_xlim(0, max(R_vals))
    ax1.set_ylim(0, max(F_total) * 1.1 if max(F_total) > 0 else 1)
    ax2.set_xlim(0, max(R_vals))
    ax2.set_ylim(min(K_vals) * 1.1 if min(K_vals) < 0 else 0, max(K_vals) * 1.1 if max(K_vals) > 0 else 1)
    
    fig.canvas.draw_idle()

# 绑定动态监听
s_L.on_changed(update)
s_H0.on_changed(update)
s_C0.on_changed(update)
s_B.on_changed(update)
s_alpha.on_changed(update)
s_beta.on_changed(update)
s_gamma.on_changed(update)
s_betaR.on_changed(update)

plt.show()