import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 设置支持中文的字体
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
fig = plt.figure(figsize=(16, 9))

# 顶部诊断框
info_text = fig.text(0.5, 0.94, "正在初始化动力学控制台...", ha="center", va="center", fontsize=15, fontweight='bold',
                     bbox=dict(facecolor='#fff3cd', alpha=0.9, edgecolor='#ffeeba', boxstyle='round,pad=0.6'))

# 核心公式展示
formula_str = r"核心基准: $K = \frac{\max(F_{eff} \cdot B - E_{近期}, 0) \cdot S^\alpha}{C}$"
fig.text(0.02, 0.94, formula_str, fontsize=12, color='#333', 
         bbox=dict(facecolor='#f8f9fa', edgecolor='#dee2e6', boxstyle='round,pad=0.4'))

# 左右图表
ax1 = plt.axes([0.06, 0.55, 0.40, 0.32])
ax2 = plt.axes([0.55, 0.55, 0.40, 0.32])

# ================= 3. 标定手册与 K 值阈值说明 =================
reference_text = (
    "【游戏参数标定参考】(清醒时间16h)：\n"
    "• 时间吞噬度 α：欧卡2(跑长途)=1.2(极杀时间)；休闲=0.4\n"
    "• 大脑占据度 β：ACC(抠细节) / 尖塔(算牌)=1.2；挂机=0.2\n"
    "• 即时爽快度 β_R：2077(秒怪)=1.0；硬核受苦=-0.2\n"
    "• 固有杀伤力 B：普通前任=0.5；极度意难平=2.5"
)
fig.text(0.25, 0.43, reference_text, ha="center", va="center", fontsize=10, color='#333',
         bbox=dict(facecolor='#e9ecef', edgecolor='#ced4da', boxstyle='round,pad=0.5'))

threshold_text = (
    "【杀伤力 K 战损等级阈值】：\n"
    "• [K = 0]：绝对防御 (No Pain)，心无旁骛。\n"
    "• [0 < K ≤ 0.3]：轻微波动 (正常状态)，不影响现实。\n"
    "• [0.3 < K ≤ 0.8]：精神内耗 (危险边缘)，操作变形。\n"
    "• [K > 0.8]：彻底破防 (理智崩塌)，情绪失控。"
)
fig.text(0.75, 0.43, threshold_text, ha="center", va="center", fontsize=10, color='#333',
         bbox=dict(facecolor='#e0e7ff', edgecolor='#a5b4fc', boxstyle='round,pad=0.5'))

# ================= 4. 滑块 UI =================
axcolor_self = '#e3f2fd'
axcolor_game = '#fbe9e7'
slider_h = 0.02
slider_w = 0.32

ax_L  = plt.axes([0.12, 0.32, slider_w, slider_h], facecolor=axcolor_self)
ax_H0 = plt.axes([0.12, 0.25, slider_w, slider_h], facecolor=axcolor_self)
ax_C0 = plt.axes([0.12, 0.18, slider_w, slider_h], facecolor=axcolor_self)
ax_B  = plt.axes([0.12, 0.11, slider_w, slider_h], facecolor=axcolor_self)

ax_alpha = plt.axes([0.60, 0.32, slider_w, slider_h], facecolor=axcolor_game)
ax_beta  = plt.axes([0.60, 0.25, slider_w, slider_h], facecolor=axcolor_game)
ax_gamma = plt.axes([0.60, 0.18, slider_w, slider_h], facecolor=axcolor_game)
ax_betaR = plt.axes([0.60, 0.11, slider_w, slider_h], facecolor=axcolor_game)

s_L  = Slider(ax_L, '正事时间比例 L', 0.0, 0.9, valinit=init_L, valstep=0.05, valfmt='%1.2f')
s_H0 = Slider(ax_H0, '想她本能频率 H0', 0.0, 1.0, valinit=init_H0, valstep=0.05, valfmt='%1.2f')
s_C0 = Slider(ax_C0, '你的理智基础 C0', 0.1, 1.0, valinit=init_C0, valstep=0.05, valfmt='%1.2f')
s_B  = Slider(ax_B, '她固有杀伤力 B', 0.5, 3.0, valinit=init_B, valstep=0.1, valfmt='%1.1f')

s_alpha = Slider(ax_alpha, '时间吞噬度 α', 0.1, 1.5, valinit=init_alpha_g, valstep=0.1, valfmt='%1.1f')
s_beta  = Slider(ax_beta, '大脑占据度 β', 0.1, 1.5, valinit=init_beta_g, valstep=0.1, valfmt='%1.1f')
s_gamma = Slider(ax_gamma, '理智腐蚀度 γ', 0.0, 1.0, valinit=init_gamma_g, valstep=0.1, valfmt='%1.1f')
s_betaR = Slider(ax_betaR, '即时爽快度 β_R', -0.5, 1.5, valinit=init_beta_R, valstep=0.1, valfmt='%1.1f')

# ================= 5. 核心物理计算逻辑 =================
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

line1, = ax1.plot(R * 16, F_t, color='#2ec4b6', linewidth=2.5)
line2, = ax2.plot(R * 16, K, color='#e63946', linewidth=2.5)
vline2 = ax2.axvline(x=R[np.argmin(K)] * 16, color='#9b5de5', linestyle=':')

ax1.set_title('空闲状态下的幻想频率', fontsize=12)
ax1.set_xlabel('每天游戏时间 (小时)')
ax1.grid(True, linestyle='--', alpha=0.5)

ax2.set_title('白月光终极杀伤力 $K$', fontsize=12)
ax2.set_xlabel('每天游戏时间 (小时)')
ax2.grid(True, linestyle='--', alpha=0.5)

# ================= 6. 动态判定反馈逻辑 =================
def get_k_label(k):
    if k == 0: return "绝对防御"
    elif k <= 0.3: return "轻微波动"
    elif k <= 0.8: return "精神内耗"
    else: return "彻底破防"

def update(val):
    L_val = s_L.val
    R_vals, F_total, K_vals = calculate_system(
        L_val, s_H0.val, s_C0.val, s_B.val, init_F_int, init_E0,
        s_alpha.val, s_beta.val, s_gamma.val, s_betaR.val
    )
    
    line1.set_data(R_vals * 16, F_total)
    line2.set_data(R_vals * 16, K_vals)
    
    min_idx = np.argmin(K_vals)
    best_R = R_vals[min_idx]
    best_K = K_vals[min_idx]
    base_K = K_vals[0]
    vline2.set_xdata([best_R * 16, best_R * 16])
    
    total_awake = 16.0
    free_hours = (1.0 - L_val) * total_awake
    game_hours = best_R * total_awake
    
    base_label = get_k_label(base_K)
    min_label = get_k_label(best_K)
    
    if game_hours >= free_hours - 0.5 and free_hours > 0:
        advice = f"🚨 现实逃避：全拿来打游戏麻痹自己。已被破防！【当前: {min_label} K={best_K:.2f}】"
        info_text.set_color('#dc3545') 
    elif game_hours <= 0.1:
        if base_K <= 0.3:
            advice = f"🛡️ 状态极佳：无需游戏干预，她也无法破防！【当前: {base_label} K={base_K:.2f}】"
            info_text.set_color('#198754') 
        else:
            advice = f"⚠️ 绝对禁止！游戏只会加速崩塌！最优解是【禁游去干正事】。【当前: {base_label} K={base_K:.2f}】"
            info_text.set_color('#dc3545') 
    elif best_K < base_K:
        if best_K == 0:
            advice = f"✅ 完美转移：每天适度打 {game_hours:.1f}h 游戏，即可将杀伤力清零。【达成: {min_label}】"
            info_text.set_color('#0d6efd') 
        else:
            advice = f"💡 战损压制：每天打 {game_hours:.1f}h，能将杀伤力从 {base_K:.2f} 压制到 {best_K:.2f}。【改善至: {min_label}】"
            info_text.set_color('#212529') 
    else:
        advice = f"⚠️ 饮鸩止渴：越玩越崩！产出比极低，请立即退出游戏！"
        info_text.set_color('#d97706') 
        
    info_text.set_text(advice)
    
    ax1.set_xlim(0, max(0.1, max(R_vals) * 16))
    ax1.set_ylim(0, 1.0)
    ax2.set_xlim(0, max(0.1, max(R_vals) * 16))
    max_k_plot = max(K_vals)
    ax2.set_ylim(0, max(1.5, max_k_plot * 1.1 if max_k_plot > 0 else 1.5))
    
    fig.canvas.draw_idle()

sliders = [s_L, s_H0, s_C0, s_B, s_alpha, s_beta, s_gamma, s_betaR]
for s in sliders:
    s.on_changed(update)

update(None)
plt.show()