import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 2. 初始参数
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

# 3. 创建画布布局
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
plt.subplots_adjust(bottom=0.45, wspace=0.25)

# 4. 核心计算模型（已修复负数逻辑 Bug）
def calculate_system(L, H0, C0, B, F_int, E0, alpha_g, beta_g, gamma_g, beta_R):
    max_R_by_S = (1.0 - L) / alpha_g if alpha_g > 0 else 1.0
    max_R_by_C = (C0 - 0.05) / gamma_g if gamma_g > 0 else 1.0
    max_R = min(max_R_by_S, max_R_by_C, 1.0)
    if max_R <= 0: max_R = 0.01
    
    R_vals = np.linspace(0, max_R * 0.98, 300)
    
    F_total = np.maximum((1.0 - L - alpha_g * R_vals) * (H0 - beta_g * R_vals), 0)
    F_eff = F_total * F_int
    S = np.maximum(1.0 - L - alpha_g * R_vals, 0)
    E_recent = E0 + beta_R * R_vals
    C = C0 - gamma_g * R_vals
    
    # 修复项：杀伤力分子不可能为负，最低就是不破防(0)
    numerator = np.maximum(F_eff * B - E_recent, 0) 
    K_vals = numerator * (S ** alpha_emotion) / C
    
    return R_vals, F_total, K_vals

# 5. 初始化图像
R, F_t, K = calculate_system(init_L, init_H0, init_C0, init_B, init_F_int, init_E0, 
                             init_alpha_g, init_beta_g, init_gamma_g, init_beta_R)

line1, = ax1.plot(R, F_t, color='#2ec4b6', linewidth=2.5)
line2, = ax2.plot(R, K, color='#e63946', linewidth=2.5)
vline2 = ax2.axvline(x=R[np.argmin(K)], color='#9b5de5', linestyle=':')

ax1.set_title('空闲状态下对她的总幻想频率', fontsize=12)
ax1.set_xlabel('游戏时间占比 $R$ (0=不玩, 0.5=全天清醒一半时间都在玩)')
ax1.grid(True, linestyle='--', alpha=0.5)

ax2.set_title('白月光终极杀伤力 $K$ (Y轴越高越破防)', fontsize=12)
ax2.set_xlabel('游戏时间占比 $R$')
ax2.grid(True, linestyle='--', alpha=0.5)

# 动态文本框：直观显示结论
info_text = ax2.text(0.05, 0.85, "", transform=ax2.transAxes, fontsize=11, 
                     bbox=dict(facecolor='white', alpha=0.8, edgecolor='#ccc', boxstyle='round,pad=0.5'))

# 6. 滑块 UI
axcolor = '#f0f4f8'
ax_L = plt.axes([0.1, 0.30, 0.3, 0.02], facecolor=axcolor)
ax_H0 = plt.axes([0.1, 0.24, 0.3, 0.02], facecolor=axcolor)
ax_C0 = plt.axes([0.1, 0.18, 0.3, 0.02], facecolor=axcolor)
ax_B = plt.axes([0.1, 0.12, 0.3, 0.02], facecolor=axcolor)

ax_alpha = plt.axes([0.58, 0.30, 0.3, 0.02], facecolor=axcolor)
ax_beta = plt.axes([0.58, 0.24, 0.3, 0.02], facecolor=axcolor)
ax_gamma = plt.axes([0.58, 0.18, 0.3, 0.02], facecolor=axcolor)
ax_betaR = plt.axes([0.58, 0.12, 0.3, 0.02], facecolor=axcolor)

s_L = Slider(ax_L, '正事时间比例 L', 0.0, 0.9, valinit=init_L)
s_H0 = Slider(ax_H0, '空闲瞎想概率 H0', 0.0, 1.0, valinit=init_H0)
s_C0 = Slider(ax_C0, '你的基础理智 C0', 0.1, 1.0, valinit=init_C0)
s_B = Slider(ax_B, '她固有吸引力 B', 0.5, 3.0, valinit=init_B)

s_alpha = Slider(ax_alpha, '游戏吸时率 \u03B1', 0.1, 1.5, valinit=init_alpha_g)
s_beta = Slider(ax_beta, '游戏分心率 \u03B2', 0.1, 1.5, valinit=init_beta_g)
s_gamma = Slider(ax_gamma, '游戏蚀控率 \u03B3', 0.0, 1.0, valinit=init_gamma_g)
s_betaR = Slider(ax_betaR, '游戏快乐率 \u03B2_R', 0.0, 1.5, valinit=init_beta_R)

# 7. 更新逻辑
def update(val):
    R_vals, F_total, K_vals = calculate_system(
        s_L.val, s_H0.val, s_C0.val, s_B.val, init_F_int, init_E0,
        s_alpha.val, s_beta.val, s_gamma.val, s_betaR.val
    )
    
    line1.set_data(R_vals, F_total)
    line2.set_data(R_vals, K_vals)
    
    # 寻找最佳防守点（最低伤害）
    min_idx = np.argmin(K_vals)
    best_R = R_vals[min_idx]
    best_K = K_vals[min_idx]
    
    vline2.set_xdata([best_R, best_R])
    
    # 将 R 转化为按一天 16 个小时清醒时间计算的小时数
    hours = best_R * 16 
    if best_K == 0:
        advice = f"防守成功！每天打 {hours:.1f} 小时游戏，能让她无法破防 (K=0)"
    else:
        advice = f"最优解：每天打 {hours:.1f} 小时游戏，杀伤力压制在 {best_K:.3f}"
        
    info_text.set_text(f"💡 AI 诊断结论：\n当前参数下，{advice}")
    
    # 锁定 Y 轴视图逻辑：展现真正的绝对值变化！
    ax1.set_xlim(0, 0.5)
    ax1.set_ylim(0, 1.0) # 幻想频率固定为 0~1 的绝对概率
    
    ax2.set_xlim(0, 0.5)
    # 给杀伤力设定一个比较高的固定天花板，防止被自动缩放隐藏绝对值
    ax2.set_ylim(0, 1.5) 
    
    # 如果曲线真的冲破天际了，再临时提高天花板
    if np.max(K_vals) > 1.5:
        ax2.set_ylim(0, np.max(K_vals) * 1.1)
        
    fig.canvas.draw_idle()

s_L.on_changed(update)
s_H0.on_changed(update)
s_C0.on_changed(update)
s_B.on_changed(update)
s_alpha.on_changed(update)
s_beta.on_changed(update)
s_gamma.on_changed(update)
s_betaR.on_changed(update)

update(None) # 初始化触发一次
plt.show()