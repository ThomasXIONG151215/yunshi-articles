# VFED 论文图件规格文档
# VFED Paper Figures Specification

> 本文档定义6张图的中英文版本规格，用于微信公众号学术推文
> Specified for 6 figures in both Chinese and English for WeChat blog

**风格标准**: Swiss Pulse (Academic/Technical)
- 背景色: `#faf9f5` (暖白)
- 主文字: `#141413` (近黑)
- 强调色: `#d97757` (暖橙)
- 数据蓝: `#4285f4`
- 网格线: `#e8e6dc`

**字体**: Arial / Microsoft YaHei，字号20pt起
**输出**: PNG (宽800px, 200dpi) + HTML交互版
**要求**: 标题必须说明清楚限制条件，让未读论文的人也能看懂

---

## 图1: VFED框架架构图 (Fig1_VFED_Framework)
**文件夹**: `conceptual/`
**类型**: Draw.io 概念图 (手绘)

### 视觉背景
四层级框架，从下到上：
1. **Climate Data** - 气象数据输入（温度、太阳辐射、湿度）
2. **Hybrid Modeling** - 光伏单二极管模型 + 储能充放电模型 + 负荷模型耦合
3. **Optimization** - 441种PVBES配置 × 24种光周期 = 10584种组合，逐小时能量平衡仿真
4. **Economic Eval** - LCOE最小化、PBP分析，输出最优设计

### 精确数据
- 基准单元: 20ft集装箱, 16m²种植面积
- 仿真组合: 441 × 24 = 10584
- 验证数据: 2024上海全年，小时分辨率
- 5个气候城市: 上海、拉萨、海口、哈尔滨、乌鲁木齐

### 布局要求
- 垂直堆叠的4个层级，用箭头连接
- 每层用不同颜色区分（蓝→橙→深橙→绿）
- 中心统一基准单元（集装箱示意图）
- 简洁学术风格，无多余装饰

### 中文字体
使用微软雅黑，标题18px，说明文字14px

---

## 图2: 五城市光伏资源与储能配置对比 (Fig2_5Cities_Climate)
**文件夹**: `data_charts/`
**类型**: 分组柱状图

### 数据 (来自论文实测+仿真)
| 城市 | 年均光伏 (kWh/m²/天) | 近能源自主储能 (kWh) |
|------|---------------------|---------------------|
| 拉萨 | 5.88 | 40 |
| 海口 | 4.72 | 45 |
| 上海 | 4.0-4.5 | 50 |
| 乌鲁木齐 | 4.21 | 45 |
| 哈尔滨 | 3.81 | 50 |

> 储能容量为实现TGD<5%所需的配置，光伏资源为TMY典型气象年数据

### 双Y轴设计
- 左Y轴: 年均光伏辐射 (kWh/m²/天), 蓝色柱
- 右Y轴: 储能容量需求 (kWh), 橙色折线+数值标注

### 标题 (必须包含条件)
- CN: **五城市光伏资源与近能源自主储能需求**（20尺集装箱·16m²·TGD<5%）
- EN: **5-City PV Resource & Storage for Near Autonomy** (20ft Container, 16m², TGD<5%)

---

## 图3: 全年能耗季节性分解 (Fig3_Energy_Seasonality)
**文件夹**: `data_charts/`
**类型**: 堆叠面积图

### 数据 (上海20尺集装箱植物工厂，基于2024全年实测)
| 月份 | LED照明 | 空调 | 风机/其他 |
|------|---------|------|----------|
| 1月 | ~15 | <5 | ~5 |
| 4月 | ~15 | 8 | ~5 |
| 7月 | ~18 | 25 | ~5 |
| 10月 | ~15 | 18 | ~5 |
| 12月 | ~14 | <5 | ~5 |

> 数据基于2024年上海实测值取典型月近似，详细小时数据见论文开源数据

### 标注
- 冬季典型日总能耗: ~20 kWh/天
- 夏季峰值日总能耗: >45 kWh/天

### 标题 (必须包含条件)
- CN: **上海20尺集装箱植物工厂全年能耗分解**（2024全年实测数据，典型月近似）
- EN: **Annual Energy Breakdown, Shanghai 20ft PFAL** (2024 Measured Data, Typical Months)

---

## 图4: 光周期起始时间对储能容量需求的影响 (Fig4_Photoperiod_Storage) ⭐核心发现
**文件夹**: `data_charts/`
**类型**: 折线图

### 核心数据 (上海，TGD<5%，20ft集装箱，16m²)
论文原文明确给出：
- **凌晨2-6点光周期**：储能需求仅需 50-60 kWh
- **下午1-7点光周期**：储能需求高达 80-90 kWh
- **凌晨4点**：最优点，储能约50 kWh
- **储能差异**：凌晨策略比下午策略减少约40%储能需求

> 注：0-23时连续曲线由论文关键区间数据点+线性插值得出

### 图表要素
- X轴: 光周期起始时刻 (0-24时)
- Y轴: 储能容量需求 (kWh)
- 绿色阴影: 最优区间 (凌晨2-5点)
- 橙色阴影: 高位区间 (下午1-5点)
- ★标记: 最优点 (凌晨4点，~50 kWh)

### 标题 (必须包含条件)
- CN: **光周期起始时间对储能需求的影响**（上海·20尺集装箱·16m²·TGD<5%·光伏86.5±4.9 m²固定）
- EN: **Photoperiod Start Time vs. Battery Storage** (Shanghai, 20ft, 16m², TGD<5%, PV 86.5±4.9 m²)

### 副标题 (中/英)
- CN: 凌晨3-5点启动 vs 下午1-7点启动 —— 储能需求减少40%
- EN: Starting at 3-5 AM vs 1-7 PM → 40% storage reduction

---

## 图5: 五城市近能源自主系统配置 (Fig5_5Cities_NearEnergyAutonomy)
**文件夹**: `data_charts/`
**类型**: 分组柱状图

### 数据 (TGD<5%, 20ft集装箱, 16m²，5城市仿真优化结果)
| 城市 | 光伏面积 (m²) | 储能容量 (kWh) |
|------|--------------|----------------|
| 拉萨 | 40 | 40 |
| 海口 | 50 | 45 |
| 上海 | 80 | 50 |
| 乌鲁木齐 | 110 | 45 |
| 哈尔滨 | 120 | 50 |

> 目标：基于时间的电网依赖率 <5%（定义为"近能源自主"），光伏固定86.5±4.9 m²（上海基准）

### 双柱设计
- 蓝色柱: 光伏面积 (m²)
- 橙色柱: 储能容量 (kWh)

### 标注
- 最小配置: 拉萨 40m²+40kWh（高原高辐射+低冷却需求）
- 最大配置: 哈尔滨 120m²+50kWh（高纬度低辐射+供暖需求）
- ×3标注: 拉萨 vs 哈尔滨光伏面积相差3倍

### 标题 (必须包含条件)
- CN: **五城市近能源自主系统配置**（20尺集装箱·16m²·TGD<5%·10584种仿真优化）
- EN: **Near-Autonomy PV+BES Configurations** (20ft Container, 16m², TGD<5%, 10,584 Sims)

---

## 图6: 平准化能源成本与电网电价对比 (Fig6_LCOE_Comparison)
**文件夹**: `data_charts/`
**类型**: 柱状图

### 数据 (上海20尺集装箱植物工厂，16m²)
| 场景 | LCOE ($/kWh) | 相对电网节省 |
|------|--------------|-------------|
| 电网电价 (上海参考) | 0.096 | — (基准) |
| 3年投资回收期最优 | 0.034-0.042 | 57%-61% |
| 5年投资回收期最优 | 0.032-0.039 | 59%-67% |

> LCOE范围对应不同光周期策略；5年PBP最优值0.032$/kWh对应最大67%节省

### 标注
- 灰色柱: 电网电价 0.096 $/kWh
- 蓝色柱: 3年PBP LCOE ~0.038（中值）
- 绿色柱: 5年PBP LCOE ~0.036（中值）
- 箭头标注: 最高可节省63-67%

### 标题 (必须包含条件)
- CN: **光伏储能系统平准化能源成本 (LCOE)**（上海·20尺集装箱·16m²·5城市对比）
- EN: **Levelized Cost of Energy (LCOE)** (Shanghai, 20ft Container, 16m², 5 Cities)

---

## 交付物清单

### 文件夹结构
```
figures/
├── data_charts/          # Plotly数据图表
│   ├── fig2_5cities_climate.py
│   ├── fig3_energy_seasonality.py
│   ├── fig4_photoperiod_storage.py
│   ├── fig5_5cities_config.py
│   └── fig6_lcoe_comparison.py
├── conceptual/            # Draw.io/AI概念图
│   ├── fig1_vfed_framework.drawio
│   └── fig1_vfed_framework.png
└── SPEC.md               # 本文档
```

### 中英文命名
| 图号 | 中文名 | 英文名 |
|-----|--------|--------|
| Fig1 | VFED框架架构图 | VFED Framework Architecture |
| Fig2 | 五城市光伏资源对比 | 5-City PV Resource Comparison |
| Fig3 | 全年能耗季节性分解 | Annual Energy Seasonality |
| Fig4 | 光周期与储能需求关系 | Photoperiod vs Storage |
| Fig5 | 五城市系统配置对比 | 5-City System Configuration |
| Fig6 | LCOE经济性对比 | LCOE Comparison |

### 输出格式
- PNG: 1200px宽, 300dpi
- HTML: Plotly交互版
- 命名: `{FigX}_{中文标题}_cn.png` / `{FigX}_{English_title}_en.png`

---

## 绘图代码模板

```python
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# 统一配色方案
COLORS = {
    'background': '#faf9f5',
    'primary_text': '#141413',
    'accent': '#d97757',
    'data_blue': '#4285f4',
    'grid': '#e8e6dc',
    'green': '#059669'
}

def create_chart():
    fig = go.Figure()
    # 添加图表元素...
    fig.update_layout(
        template='plotly_white',
        paper_bgcolor=COLORS['background'],
        plot_bgcolor=COLORS['background'],
        font=dict(family='Arial, Microsoft YaHei', size=14, color=COLORS['primary_text']),
        title=dict(x=0.5, font=dict(size=18))
    )
    return fig
```

---

## 注意事项

1. **数据精确性**: 所有数值必须与论文原文完全一致
2. **字体渲染**: 中文必须使用 Microsoft YaHei，避免 Arial 渲染中文
3. **手机可读**: 文字大小在手机上缩放50%后仍清晰可读
4. **中英双语**: 每张图必须有中文版和英文版两个版本
5. **风格统一**: 6张图使用统一的配色方案和排版风格
