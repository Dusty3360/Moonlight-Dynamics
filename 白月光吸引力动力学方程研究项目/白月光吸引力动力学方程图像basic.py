import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置支持中文的字体（根据系统调整，这里使用黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 设定参数基准
D = 10      # 意念综合强度 (F * B - E_近期)
alpha = 2   # 情绪敏感系数 (alpha > 1)

# 2. 创建画布
fig = plt.figure(figsize=(18, 5))

# --- 子图 1: K 随 空闲度 S 的变化 (固定自控力 C=2) ---
ax1 = fig.add_subplot(131)
S_line = np.linspace(0, 1, 100)
C_fixed = 2
K_of_S = D * (S_line**alpha) / C_fixed

ax1.plot(S_line, K_of_S, color='#ff6b6b', linewidth=2.5, label=f'C = {C_fixed}')
ax1.set_title('空闲度 $S$ 对杀伤力 $K$ 的影响\n(高强度学习 vs 躺平瞎想)', fontsize=12)
ax1.set_xlabel('空闲度 $S$ (0=完全没空, 1=完全空闲)')
ax1.set_ylabel('杀伤力 $K$')
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend()

# --- 子图 2: K 随 自控力 C 的变化 (固定空闲度 S=0.8) ---
ax2 = fig.add_subplot(132)
C_line = np.linspace(0.2, 5, 100) # 避开 C=0 爆炸点
S_fixed = 0.8
K_of_C = D * (S_fixed**alpha) / C_line

ax2.plot(C_line, K_of_C, color='#4dadf7', linewidth=2.5, label=f'S = {S_fixed}')
ax2.set_title('自控力 $C$ 对杀伤力 $K$ 的影响\n(C→0 情感完全失控爆炸)', fontsize=12)
ax2.set_xlabel('自控力 $C$ ($C > 0$)')
ax2.set_ylabel('杀伤力 $K$')
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend()

# --- 子图 3: S 和 C 共同作用的 3D 动力学表面 ---
ax3 = fig.add_subplot(133, projection='3d')
S_mesh, C_mesh = np.meshgrid(np.linspace(0, 1, 50), np.linspace(0.4, 5, 50))
K_mesh = D * (S_mesh**alpha) / C_mesh

# 绘制曲面
surf = ax3.plot_surface(S_mesh, C_mesh, K_mesh, cmap='coolwarm', edgecolor='none', alpha=0.9)
ax3.set_title('白月光吸引力整体动力学空间', fontsize=12)
ax3.set_xlabel('空闲度 $S$')
ax3.set_ylabel('自控力 $C$')
ax3.set_zlabel('杀伤力 $K$')
fig.colorbar(surf, ax=ax3, shrink=0.5, aspect=10, label='杀伤力强度')

# 调整布局并展示
plt.tight_layout()
plt.show()
