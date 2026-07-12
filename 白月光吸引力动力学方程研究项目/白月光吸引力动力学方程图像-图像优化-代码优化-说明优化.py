import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ================= 1. 初始参数 =================
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

# ================= 2. 创建画布布局 =================
fig = plt.figure(figsize=(16, 8))
# 划分区域：上面画图，下面放滑块，中间留给文字说明
ax1 = plt.axes([0.05, 0.55, 0.4, 0.35])
ax2 = plt.axes([0.55, 0.55, 0.4, 0.35])

# ================= 3. 核心计算模型 =================
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
    
    numerator = np.maximum(F_eff * B - E_recent, 0) 
    K_vals = numerator * (S ** alpha_emotion) / C
    return R_vals, F_total, K_vals

R, F_t, K = calculate_system(init_L, init_H0, init_C0, init_B, init_F_int, init_E0, 
                             init_alpha_g, init_beta_g, init_gamma_g, init_beta_R)

line1, = ax1.plot(R, F_t, color='#2ec4b6', linewidth=2.5)
line2, = ax2.plot(R, K, color='#e63946', linewidth=2.5)
vline2 = ax2.axvline(x=R[np.argmin(K)], color='#9b5de5', linestyle=':')

ax1.set_title('空闲状态下对她的总幻想频率', fontsize=12)
ax1.set_xlabel('每天游戏时间占比 (0=不玩, 0.5=玩8小时)')
ax1.grid(True, linestyle='--', alpha=0.5)

ax2.set_title('白月光终极杀伤力 $K$ (Y轴越高越破防)', fontsize=12)
ax2.set_xlabel('每天游戏时间占比')
ax2.grid(True, linestyle='--', alpha=0.5)

# 顶部诊断结论框
info_text = fig.text(0.5, 0.93, "", ha="center", va="center", fontsize=14, fontweight='bold',
                     bbox=dict(facecolor='#fff3cd', alpha=0.9, edgecolor='#ffeeba', boxstyle='round,pad=0.5'))

# ================= 4. 硬核图例与说明 (占据中间偏下位置) =================
legend_text = (
    "【系统基准假设】一天24小时，睡眠8小时，清醒时间=16小时。横坐标 0.1 代表每天玩 1.6 小时。\n"
    "【左侧滑块】：你自身的现实处境（比如你每天花多少时间上课/刷题，你原本的理智程度）。\n"
    "【右侧滑块】：你想玩的这款游戏的属性（比如它是高度烧脑的硬核游戏，还是杀时间的无脑刷子）。"
)
fig.text(0.5, 0.43, legend_text, ha="center", va="center", fontsize=10, color='#555',
         bbox=dict(facecolor='#f8f9fa', edgecolor='#dee2e6', boxstyle='round,pad=0.5'))

# ================= 5. 滑块 UI (重新命名并分类) =================
axcolor_self = '#e3f2fd'  # 自身条件用蓝色底
axcolor_game = '#fbe9e7'  # 游戏条件用红色底

# 自身条件滑块
ax_L = plt.axes([0.1, 0.30, 0.3, 0.02], facecolor=axcolor_self)
ax_H0 = plt.axes([0.1, 0.24, 0.3, 0.02], facecolor=axcolor_self)
ax_C0 = plt.axes([0.1, 0.18, 0.3, 0.02], facecolor=axcolor_self)
ax_B = plt.axes([0.1, 0.12, 0.3, 0.02], facecolor=axcolor_self)

s_L = Slider(ax_L, '自身: 正事占用率(如上课/刷题)', 0.0, 0.9, valinit=init_L)
s_H0 = Slider(ax_H0, '自身: 闲下来想她的本能概率', 0.0, 1.0, valinit=init_H0)
s_C0 = Slider(ax_C0, '自身: 你的基础自控力', 0.1, 1.0, valinit=init_C0)
s_B = Slider(ax_B, '白月光: 她对你的固有杀伤力', 0.5, 3.0, valinit=init_B)

# 游戏属性滑块
ax_alpha = plt.axes([0.58, 0.30, 0.3, 0.02], facecolor=axcolor_game)
ax_beta = plt.axes([0.58, 0.24, 0.3, 0.02], facecolor=axcolor_game)
ax_gamma = plt.axes([0.58, 0.18, 0.3, 0.02], facecolor=axcolor_game)
ax_betaR = plt.axes([0.58, 0.12, 0.3, 0.02], facecolor=axcolor_game)

s_alpha = Slider(ax_alpha, '游戏: 时间吞噬度(过得有多快)', 0.1, 1.5, valinit=init_alpha_g)
s_beta = Slider(ax_beta, '游戏: 大脑占据度(有多烧脑费神)', 0.1, 1.5, valinit=init_beta_g)
s_gamma = Slider(ax_gamma, '游戏: 理智腐蚀度(玩完多颓废)', 0.0, 1.0, valinit=init_gamma_g)
s_betaR = Slider(ax_betaR, '游戏: 即时爽快度(多巴胺分泌)', 0.0, 1.5, valinit=init_beta_R)

# ================= 6. 核心更新逻辑 =================
def update(val):
    L_val = s_L.val
    R_vals, F_total, K_vals = calculate_system(
        L_val, s_H0.val, s_C0.val, s_B.val, init_F_int, init_E0,
        s_alpha.val, s_beta.val, s_gamma.val, s_betaR.val
    )
    
    line1.set_data(R_vals, F_total)
    line2.set_data(R_vals, K_vals)
    
    min_idx = np.argmin(K_vals)
    best_R = R_vals[min_idx]
    best_K = K_vals[min_idx]
    vline2.set_xdata([best_R, best_R])
    
    # 现实基准转换 (一天清醒 16 小时)
    total_awake = 16
    busy_hours = L_val * total_awake
    free_hours = total_awake - busy_hours
    optimal_game_hours = best_R * total_awake
    
    # 诊断逻辑优化：识别逃避现实的极端情况
    if optimal_game_hours >= free_hours - 0.5 and free_hours > 0:
        advice = f"🚨 现实崩塌：你每天剩 {free_hours:.1f} 小时空闲，全拿来打游戏才能麻痹自己。这不是防守，是逃避！已被破防！"
        info_text.set_color('#dc3545') # 红色警告
    elif optimal_game_hours == 0:
        advice = f"🛡️ 绝对理智：你现在的状态极佳，每天 0 小时游戏她也无法破防。"
        info_text.set_color('#198754') # 绿色安全
    elif best_K == 0:
        advice = f"✅ 防守成功：干完正事后，每天打 {optimal_game_hours:.1f} 小时该游戏，注意力完美转移。"
        info_text.set_color('#0d6efd') # 蓝色正常
    else:
        advice = f"💡 最优策略：每天打 {optimal_game_hours:.1f} 小时该游戏，能把她的杀伤力强行压制在 {best_K:.3f}。"
        info_text.set_color('#212529') # 黑色默认
        
    info_text.set_text(advice)
    
    ax1.set_xlim(0, 0.5)
    ax1.set_ylim(0, 1.0)
    ax2.set_xlim(0, 0.5)
    ax2.set_ylim(0, max(1.5, np.max(K_vals) * 1.1 if np.max(K_vals) > 0 else 1.5))
    
    fig.canvas.draw_idle()

# 绑定监听
sliders = [s_L, s_H0, s_C0, s_B, s_alpha, s_beta, s_gamma, s_betaR]
for s in sliders:
    s.on_changed(update)

update(None)
plt.show()