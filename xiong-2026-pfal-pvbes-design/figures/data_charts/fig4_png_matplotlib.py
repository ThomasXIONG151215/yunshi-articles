"""
使用matplotlib生成Fig4核心发现图的PNG
Fig4: 光周期起始时间对储能容量需求的影响
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 数据
photoperiod_start = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
storage_demand = np.array([75, 70, 60, 52, 50, 55, 62, 68, 72, 76, 78, 80, 82, 85, 87, 88, 88, 87, 85, 82, 78, 75, 72, 73])

# 配色
COLORS = {
    'background': '#faf9f5',
    'primary_text': '#141413',
    'accent': '#d97757',
    'data_blue': '#4285f4',
    'grid': '#e8e6dc',
    'green': '#059669'
}

fig, ax = plt.subplots(figsize=(12, 6), facecolor=COLORS['background'])
ax.set_facecolor(COLORS['background'])

# 主曲线
ax.fill_between(photoperiod_start, storage_demand, alpha=0.2, color=COLORS['data_blue'])
ax.plot(photoperiod_start, storage_demand, 'o-', color=COLORS['data_blue'], linewidth=2.5, markersize=6, label='储能需求 (kWh)')

# 最优区间标注
ax.axvspan(2, 5, alpha=0.15, color=COLORS['green'], label='最优区间 (凌晨2-5点)')

# 高位区间标注
ax.axvspan(13, 17, alpha=0.15, color=COLORS['accent'], label='高位区间 (下午1-5点)')

# 最优标记点
ax.annotate('★ 最优点\n凌晨4点\n50 kWh', xy=(4, 50), xytext=(6, 45),
            fontsize=11, color=COLORS['green'], fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=COLORS['green']),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLORS['green']))

# 40%差异标注
ax.annotate('40%差异', xy=(10, 70), fontsize=12, color=COLORS['accent'], fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLORS['accent']))

# 标题
ax.set_title('光周期起始时间对储能容量需求的影响\n凌晨3-5点启动光周期可减少40%储能需求',
             fontsize=16, fontweight='bold', color=COLORS['primary_text'], pad=15)

# 轴标签
ax.set_xlabel('光周期起始时刻', fontsize=13, color=COLORS['primary_text'])
ax.set_ylabel('储能容量需求 (kWh)', fontsize=13, color=COLORS['primary_text'])

# 刻度
ax.set_xlim(-0.5, 23.5)
ax.set_ylim(40, 100)
ax.set_xticks(range(0, 24, 2))
ax.grid(True, alpha=0.3, color=COLORS['grid'])

# 图例
ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

plt.tight_layout()
plt.savefig('fig4_photoperiod_storage_cn.png', dpi=150, bbox_inches='tight',
            facecolor=COLORS['background'])
print('PNG saved: fig4_photoperiod_storage_cn.png')
plt.close()
