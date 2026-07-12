import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ================= 0. 环境与样式设置 =================
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 初始参数设定
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

# ================= 1. 重新规划全局布局 =================
fig = plt.figure(figsize=(16, 9)) # 增大画布比例，适应不同 DPI

# 顶部诊断框 (绝对居中，留出充足上边距防止遮挡)
info_text = fig.text(0.5, 0.94, "", ha="center", va="center", fontsize=15, fontweight='bold',
                     bbox=dict(facecolor='#fff3cd', alpha=0.9, edgecolor='#ffeeba', boxstyle='round,pad=0.6'))

# 左上角基准公式展示
formula_str = r"核心基准: $K = \frac{\max(F_{eff} \cdot B - E_{近期}, 0) \cdot S^\alpha}{C}$"
fig.text(0.02, 0.94, formula_str, fontsize=12, color='#333', 
         bbox=dict(facecolor='#f8f9fa', edgecolor='#dee2e6', boxstyle='round,pad=0.4'))

# 左右图表 (调整高度和 Y 轴起点，给下方文字和滑块让位)
ax1 = plt.axes([0.06, 0.55, 0.40, 0.32])
ax2 = plt.axes([0.55, 0.55, 0.40, 0.32])

# ================= 2. 参数标定参考手册 (具体例子) =================
reference_text = (
    "【参数标定锚点参考】（假设每天清醒16小时）：\n"
    "▶ 游戏时间吞噬度 α：欧卡2(ETS2)跑长途=1.2 (极杀时间)；休闲小游戏=0.4\n"
    "▶ 游戏大脑占据度 β：神力科莎(ACC)跑蒙扎扣细节/杀戮尖塔算牌=1.2 (脑子占满)；挂机放置=0.2\n"
    "▶ 游戏即时爽快度 β_R：赛博朋克2077黑客流秒怪=1.0 (多巴胺狂飙)；硬核受苦游戏=-0.2\n"
    "▶ 白月光固有杀伤力 B：普通前任=0.5；极度意难平=2.5"
)
fig.text(0.5, 0.43, reference_text, ha="center", va="center", fontsize=11, color='#444',
         bbox=dict(facecolor='#e9ecef', edgecolor='#ced4da', boxstyle='round,pad=0.5'))

# ================= 3. 带单位的滑块 UI =================
axcolor_self = '#e3f2fd'
axcolor_game = '#fbe9e7'
slider_h = 0.02
slider_w = 0.32
left_x = 0.12
right_x = 0.60

ax_L  = plt.axes([left_x, 0.32, slider_w, slider_h], facecolor=axcolor_self)
ax_H0 = plt.axes([left_x, 0.25, slider_w, slider_h], facecolor=axcolor_self)
ax_C0 = plt.axes([left_x, 0.18, slider_w, slider_h], facecolor=axcolor_self)
ax_B  = plt.axes([left_x, 0.11, slider_w, slider_h], facecolor=axcolor_self)

ax_alpha = plt.axes([right_x, 0.32, slider_w, slider_h], facecolor=axcolor_game)
ax_beta  = plt.axes([right_x, 0.25, slider_w, slider_h], facecolor=axcolor_game)
ax_gamma = plt.axes([right_x, 0.18, slider_w, slider_h], facecolor=axcolor_game)
ax_betaR = plt.axes([right_x, 0.11, slider_w, slider_h], facecolor=axcolor_game)

# 增加 valstep 让滑动有刻度感，增加 valfmt 显示明确单位
s_L  = Slider(ax_L, '正事时间 (占清醒时间%)', 0.0, 0.9, valinit=init_L, valstep=0.05, valfmt='%1.2f')
s_H0 = Slider(ax_H0, '想她本能 (0无~1频)', 0.0, 1.0, valinit=init_H0, valstep=0.05, valfmt='%1.2f 级')
s_C0 = Slider(ax_C0, '你的理智 (0崩~1强)', 0.1, 1.0, valinit=init_C0, valstep=0.05, valfmt='%1.2f 级')
s_B  = Slider(ax_B, '她的杀伤力 (0.5~3)', 0.5, 3.0, valinit=init_B, valstep=0.1, valfmt='%1.1f 级')

s_alpha = Slider(ax_alpha, '时间吞噬度 (α)', 0.1, 1.5, valinit=init_alpha_g, valstep=0.1, valfmt='%1.1f 级')
s_beta  = Slider(ax_beta, '大脑占据度 (β)', 0.1, 1.5, valinit=init_beta_g, valstep=0.1, valfmt='%1.1f 级')
s_gamma = Slider(ax_gamma, '理智腐蚀度 (γ)', 0.0, 1.0, valinit=init_gamma_g, valstep=0.1, valfmt='%1.1f 级')
s_betaR = Slider(ax_betaR, '即时爽快度 (β_R)', -0.5, 1.5, valinit=init_beta_R, valstep=0.1, valfmt='%1.1f 级')

# ================= 4. 核心物理计算逻辑 =================
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

ax1.set_title('空闲状态下的幻想频率', fontsize=12)
ax1.set_xlabel('每天游戏时间占比 (0=不玩, 0.5=占清醒时间一半)')
ax1.grid(True, linestyle='--', alpha=0.5)

ax2.set_title('白月光终极杀伤力 $K$', fontsize=12)
ax2.set_xlabel('每天游戏时间占比')
ax2.grid(True, linestyle='--', alpha=0.5)

# ================= 5. 动态反馈与防越界逻辑 =================
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
    
    # 将时间转化为具体的小时数 (按16小时清醒时间计)
    total_awake = 16.0
    busy_hours = L_val * total_awake
    free_hours = total_awake - busy_hours
    optimal_game_hours = best_R * total_awake
    
    if optimal_game_hours >= free_hours - 0.5 and free_hours > 0:
        advice = f"🚨 现实崩塌：每天剩 {free_hours:.1f}h，需打 {optimal_game_hours:.1f}h 游戏麻痹自己。已被破防！"
        info_text.set_color('#dc3545') 
    elif optimal_game_hours <= 0.1:
        advice = f"🛡️ 绝对防线：状态极佳！只需打 0 小时游戏，她也完全无法破防。"
        info_text.set_color('#198754') 
    elif best_K == 0:
        advice = f"✅ 防守成功：干完正事，每天打 {optimal_game_hours:.1f} 小时该游戏，注意力完美转移。"
        info_text.set_color('#0d6efd') 
    else:
        advice = f"💡 战损压制：每天打 {optimal_game_hours:.1f} 小时，将她的杀伤力强行压制在低谷 {best_K:.2f}。"
        info_text.set_color('#212529') 
        
    info_text.set_text(advice)
    
    # 锁定轴距，直观展示绝对值的暴涨暴跌
    ax1.set_xlim(0, 0.5)
    ax1.set_ylim(0, 1.0)
    ax2.set_xlim(0, 0.5)
    ax2.set_ylim(0, max(1.5, np.max(K_vals) * 1.1 if np.max(K_vals) > 0 else 1.5))
    
    fig.canvas.draw_idle()

sliders = [s_L, s_H0, s_C0, s_B, s_alpha, s_beta, s_gamma, s_betaR]
for s in sliders:
    s.on_changed(update)

update(None)
plt.show()
