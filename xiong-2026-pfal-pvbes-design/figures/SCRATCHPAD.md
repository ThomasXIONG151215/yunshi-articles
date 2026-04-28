# VFED 数据可视化制图标准与经验文档

> 本文档记录 VFED 论文微信公众号推文全部 5 张数据图表的制作标准、设计原理和经验教训。
> 最终交付版本: `generate_all_png.py` (v24)，纯 Matplotlib 实现，单文件 125 行生成全部图表。

---

## 1. 布局系统 (Three-Zone Layout)

### 1.1 三区垂直结构

每张图分为三个垂直区域，从上到下：

```
┌──────────────────────────────────────┐  y = 0.97  suptitle
│  TITLE (fig.suptitle, y=0.97)       │
├──────────────────────────────────────┤  y = 0.89  desc_area 上缘
│  DESCRIPTION (fig.add_axes, 固定    │            desc_area 高度由行数决定
│  起点 y=0.89, 向下生长)              │
│                                      ├──────────────── desc_area 下缘
│           GAP = 0.04                 │
├──────────────────────────────────────┤  chart_top = 0.89 - 0.04 - desc_h
│                                      │
│  CHART AREA (fig.add_axes,          │
│  left=0.12, width=0.75)             │
│                                      │
│                                      │  bottom = 0.06
└──────────────────────────────────────┘
```

### 1.2 关键数值

| 参数 | 值 | 说明 |
|------|-----|------|
| `DESC_Y` | `0.89` | 描述区上缘在 figure 坐标中的固定 y 位置 |
| `GAP` | `0.04` | 描述区底边到图表区顶边的间距 |
| `desc_h` | `0.05 + lines × 0.04` | 描述区高度，1 行 = 0.09, 2 行 = 0.13 |
| `chart_top` | `DESC_Y - GAP - desc_h` | 动态计算，保证描述区变化时图表区自动适配 |
| Chart left | `0.12` | 图表区左缘 (figure 坐标) |
| Chart width | `0.75` | 图表区宽度，比全宽窄 15% |
| Chart bottom | `0.06` | 图表区底缘 |

### 1.3 实现模式

所有图表使用 `fig.add_axes()` 而非 `plt.subplots()`，以实现精确坐标控制：

```python
def make_desc_ax(fig, title, desc, lines):
    fig.suptitle(title, fontsize=FT, fontweight='bold', color=C['primary'], x=0.5, y=0.97, va='top')
    desc_h = 0.05 + lines * 0.04
    chart_top = DESC_Y - GAP - desc_h
    da = fig.add_axes([0.12, DESC_Y - desc_h, 0.75, desc_h])
    da.set_xticks([]); da.set_yticks([])
    for s in da.spines.values(): s.set_visible(False)
    da.text(0.5, 0.5, desc, transform=da.transAxes, fontsize=FD, color='#555', ha='center', va='center')
    return chart_top

def chart_ax(fig, top):
    return fig.add_axes([0.12, 0.06, 0.75, top - 0.06], facecolor=C['bg'])
```

**设计原理**: 描述区从固定起点 `y=0.89` 向下生长，图表区高度通过 `chart_top` 动态计算，
两者间的 `GAP` 保持恒定。这样无论描述文字是 1 行还是 3 行，三区关系始终一致。

### 1.4 Fig3 特殊布局 (双并排饼图)

Fig3 不使用标准三区布局，而是两个并排的 `add_axes`：
- 左饼图: `[0.10, 0.06, 0.38, chart_top - 0.06]`
- 右饼图: `[0.52, 0.06, 0.38, chart_top - 0.06]`
- 标题/描述仍使用 `make_desc_ax()` 统一入口

---

## 2. 字体规格 (Typography)

### 2.1 字号常量

```python
FT  = 22    # 主标题 (fig.suptitle)
FD  = 18    # 描述文字 (desc area text)
FLB = 20    # 坐标轴标签 (xlabel, ylabel)
FTK = 18    # 刻度标签 (tick labels)
FAN = 14    # 注释/标注文字 (annotations)
```

### 2.2 具体使用

| 应用位置 | 字号 | 特殊处理 |
|----------|------|----------|
| 主标题 (suptitle) | FT=22 | bold, x=0.5, y=0.97, va='top' |
| 描述文字 | FD=18 | color='#555', ha=center, va=center |
| Y轴标签 | FLB-2=18 | 中文单位全称 |
| 刻度标签 | FTK-1=17 ~ FTK-3=15 | 根据拥挤程度调整 |
| 数据标注 | FAN+1=15 ~ FAN+3=17 | 加粗突出 |
| Fig3 饼图标题 | FT-4=18 | pad=5 (紧贴饼图) |

### 2.3 字体家族

```python
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
```

- 优先 Microsoft YaHei (Windows 系统自带中文字体)
- SimHei 作为 Windows 备选
- Arial Unicode MS 作为 macOS 备选
- Arial 用于英文/数字回退

**坑**: Plotly 的 Plotly 字号语义与 Matplotlib 不同。Plotly 字号 20 大约等于 Matplotlib 的 14-16。
最终统一用 Matplotlib 因为对字号的绝对控制更好。

---

## 3. 配色方案 (Color Palette)

### 3.1 色板定义

```python
C = {
    'bg':      '#ffffff',    # 纯白背景 (公众号浅色模式兼容)
    'primary': '#000000',    # 纯黑主文字 (最大对比度)
    'accent':  '#d85117',    # Flame (暖橙强调色)
    'blue':    '#24719e',    # UCLA Blue (数据蓝)
    'green':   '#487980',    # Myrtle Green (数据绿)
    'grid':    (0,0,0,0.1),  # 10% 黑色网格 (RGBA tuple)
    'gray':    '#7f7f7f',    # 中性灰
}
```

色板源自 `li_2021_rhizosphere_cooling` 论文的学术配色风格，非 SPEC.md 中定义的 Swiss Pulse (`#faf9f5` / `#d97757` / `#4285f4`)。

### 3.2 配色决策记录

| 初始方案 (SPEC.md) | 最终方案 (v24) | 原因 |
|---------------------|----------------|------|
| `#faf9f5` (暖白背景) | `#ffffff` (纯白) | 纯白在公众号浅色/深色模式下表现一致，无偏色 |
| `#d97757` (warm orange) | `#d85117` (Flame) | Flame 饱和度高，在白色背景上识别度更好 |
| `#4285f4` (Google Blue) | `#24719e` (UCLA Blue) | UCLA Blue 与 Flame 的对比更均衡 |
| `#e8e6dc` (warm grid) | `(0,0,0,0.1)` (透明灰) | 10% 黑色网格在白色背景上更中性 |
| 无绿色 | `#487980` (Myrtle Green) | 需要第三种数据色来标注最优/LCOE场景 |

### 3.3 配色使用规则

- **主数据系列**: `C['blue']` (#24719e)
- **第二数据/Y2轴**: `C['accent']` (#d85117)
- **最优/节省场景**: `C['green']` (#487980)
- **基准/电网**: `C['gray']` (#7f7f7f)
- **描述区**: 无背景填充，仅文字 color='#555'
- **图表区**: `facecolor=C['bg']`
- **网格线**: 极淡，仅在需要时使用
- **禁止使用**: 鲜艳渐变、大面积背景色块、非色板颜色

---

## 4. 单位标准 (100% 中文)

### 4.1 单位对照

| 原始单位 | 中文写法 | 说明 |
|----------|----------|------|
| kWh | 千瓦时 | 能源 |
| m² | 平米 | 面积 (非"平方米") |
| kW | 千瓦 | 功率 |
| 元/度 (电费) | 元/千瓦时 | 成本 (度→千瓦时) |
| kWh/m²/day | 千瓦时/平米/天 | 太阳辐射日累计 |
| $/kWh | 美元/千瓦时 | LCOE美元单位 |
| °C | °C | 温度 (保持原样) |

### 4.2 强制规则

- 图表中**永不出现**英文单位缩写 (kWh, m², kW 在最终版中已被替换)
- 唯一例外: Fig6 使用"元/千瓦时"和"美元/千瓦时"对照 (论文原文以美元计)
- 坐标轴标签格式: `'年均太阳辐射 (千瓦时/平米/天)'` 而非 `'PV (kWh/m²/day)'`

---

## 5. 文字撰写原则

### 5.1 标题风格

- **提问式标题**: "为什么选了这五座城市？"、"几点开灯最省电池？差40%！"
- **口语化、对话感**: 模拟读者看完图会产生的自然问题
- **禁止学术标题**: 不用 "Fig.2 Annual Photovoltaic Resource Distribution Across Five Chinese Climate Zones"

### 5.2 描述区风格

- **事实陈述 + 结论**: "我们采集了...可以看到..." → 先呈现数据来源，后给出结论
- **无来源引用**: 图表上不出现 "数据来源: ..." 或 "(详见论文表2)" 之类的标注
- **破折号连接因果**: 用 "——" (em dash) 做因果连接，如 "拉萨日照最强(~5.9)又凉爽(~8°C)；哈尔滨日照最弱(~3.8)又寒冷(~6°C)"
- **括号内精确数值**: "(约0.096美元/千瓦时 ≈ 0.69元/千瓦时)"

### 5.3 禁止项

- 英文缩写 (LCOE → "平准化能源成本", PBP → "投资回收期", TGD → "电网依赖率")
- 图表角落的来源标注
- 纯学术论文口吻 (如 "如图所示"、"研究表明")
- 第二人称说教 ("您可以看到" → 用 "可以看到")

### 5.4 审查 Checklist

每张图发布前朗读标题和描述文字，检查：
- [ ] 不读论文的人能看懂标题吗？
- [ ] 描述文字有没有说清楚限制条件 (地点、数据年份、假设)？
- [ ] 有没有英文缩写残留？
- [ ] 数值有没有和论文原文核对？

---

## 6. 输出规格

### 6.1 文件参数

```python
FW = 12       # Figure width (inches)
FH = 7        # Figure height (inches) — Fig4 用 FH*1.05=7.35, Fig5 用 FW*1.05=12.6, Fig6 用 FW*0.9=10.8
```

### 6.2 导出格式

```python
def save(fig, name):
    fig.savefig(name + '.svg', bbox_inches='tight', transparent=True, dpi=300)
    fig.savefig(name + '.png', bbox_inches='tight', facecolor=C['bg'], dpi=200)
```

| 格式 | 用途 | 参数 |
|------|------|------|
| SVG | 公众号推文嵌入 (矢量无损) | 透明背景, 300 dpi |
| PNG | 备用/缩略图 | 白色背景, 200 dpi |
| DPI | SVG 300 / PNG 200 | SVG 高 dpi 确保文字清晰 |

### 6.3 文件命名规范

```
fig{N}_{中文简短描述}_cn.svg
fig{N}_{中文简短描述}_cn.png
```

例: `fig4_photoperiod_storage_cn.svg`, `fig4_photoperiod_storage_cn.png`

### 6.4 交付的 5 张图

| 图号 | 文件名基础 | 类型 | 尺寸 |
|------|-----------|------|------|
| Fig2 | `fig2_5cities_climate_cn` | 双Y轴柱状图 | 12×7 |
| Fig3 | `fig3_energy_seasonality_cn` | 双饼图 | 12×7 |
| Fig4 | `fig4_photoperiod_storage_cn` | 折线+高亮区间 | 12×7.35 |
| Fig5 | `fig5_5cities_config_cn` | 分组柱状图 | 12.6×7 |
| Fig6 | `fig6_lcoe_comparison_cn` | 柱状对比图 | 10.8×7 |

---

## 7. 数据准确性规则

### 7.1 与论文原文的对应

每张图的数据必须**逐项回溯**到论文原文 `clean-minor-revision-ENB_XIONG_manuscript.md` 中的具体数值。

### 7.2 插值与近似值的标记

| 图表 | 近似/插值部分 | 处理方式 |
|------|-------------|----------|
| Fig2 上海太阳能 | 论文写 4.0-4.5, 取中值 4.25 | 代码中取 4.25，描述区写 "4.0-4.5" |
| Fig3 季节性能耗 | 论文写典型月份，非全年逐月 | 取 5 个代表性月份 (1,4,7,10,12) |
| Fig3 冬季/夏季值 | 论文写 "~20" ">45" | 饼图保留 ~ 前缀 |
| Fig4 光周期曲线 | 论文仅给关键区间 (2-6点≈50-60, 13-19点≈80-90) | 中间点线性插值，描述区不声称精确 |
| Fig6 3年/5年LCOE | 论文给范围 (0.034-0.042) | 取中值，描述区写"约" |
| Fig6b 五城市LCOE | 论文仅给上海数据 | 城市间LCOE为近似推导，单独出图fig6b |

### 7.3 汇率假设

USD → RMB 转换使用固定汇率 **7.2**:
- 论文中电价 0.096 $/kWh → 0.691 元/千瓦时 (0.096 × 7.2)
- Fig6 同时显示美元和人民币数值
- 在描述区注明 "按固定假设电价 (约0.096美元/千瓦时 ≈ 0.69元/千瓦时)"

### 7.4 数据校验流程

1. 打开论文原文，搜索关键数值
2. 在代码中注释 `# 论文原文: ...` 作为溯源标记
3. 输出图表后用截图工具测量关键数值是否与论文一致
4. 标注含~的为典型月近似，标注"约"的为插值

---

## 8. 代码组织

### 8.1 最终架构

```
figures/data_charts/
├── generate_all_png.py          # ★ 主脚本，125行，生成全部 PNG+SVG
├── fig2_5cities_climate.py      #   Plotly 原型 (保留参考，不再使用)
├── fig3_energy_seasonality.py   #   Plotly 原型
├── fig4_photoperiod_storage.py  #   Plotly 原型
├── fig4_png_matplotlib.py       #   Fig4 Matplotlib 中间实验版
├── fig5_5cities_config.py       #   Plotly 原型
├── fig6_lcoe_comparison.py      #   Plotly 原型
├── fig2_5cities_climate_cn.svg  #   输出文件
├── fig2_5cities_climate_cn.png
├── ... (其余输出文件)
```

### 8.2 单文件 vs 多文件决策

| 方案 | 优势 | 劣势 |
|------|------|------|
| 多文件 (Plotly 原型) | 每张图独立开发调试 | 样式不一致, 难以统一调参 |
| **单文件 (v24 最终)** | 样式绝对统一, 修改色板/字号一次生效全部 | 文件变长 (125行) |

**结论**: 对于 <10 张图且需要严格统一风格的项目，**单文件方案优于多文件**。共享函数 (`make_desc_ax`, `chart_ax`, `save`) 保证三区布局、配色、字号在所有图之间零偏差。

### 8.3 共享函数

```python
# 三个共享函数，所有图复用
def make_desc_ax(fig, title, desc, lines) -> chart_top:
    """创建标题 + 描述区，返回图表区顶缘位置"""

def chart_ax(fig, top) -> ax:
    """在指定位置创建图表区，返回 matplotlib axes"""

def save(fig, name):
    """同时导出 SVG (透明) 和 PNG (白色背景)"""
```

### 8.4 分段标记

每张图区域用 `# FigN — 中文标题` 注释分隔，便于快速跳转：

```python
# Fig2 — 五城市气候差异（光照+温度双轴）
# Fig3 — 植物工厂冬天用电和夏天有什么不同？
# Fig4 — 几点开灯最省电池？差40%！
# Fig5 — 从拉萨到哈尔滨，同一个植物工厂的硬件成本差3倍？
# Fig6 — 植物工厂自配最优光伏与储能，每千瓦时电成本多少？
```

### 8.5 版本迭代记录

| 版本 | 变更 |
|------|------|
| Plotly 原型 | 每张图独立 .py, 使用 Plotly + Kaleido 导出 PNG (渲染不稳定) |
| v23 之前 | 尝试统一但中英文单位混用 (kWh/m²/day 等) |
| **v24 (最终)** | 纯 Matplotlib, 100% 中文单位, 单文件, 三区布局统一, 五色板确定 |

---

## 9. 已知问题与边界案例

### 9.1 Plotly 遗留问题

- **Kaleido 依赖**: Plotly PNG 导出需要 kaleido 包，安装复杂且在某些环境中失败
- **SVG 质量**: Plotly 的 SVG 文本有时渲染为 path 而非 text 元素，在公众号平台可能出现字体回退
- **字号不一致**: Plotly 14px ≈ Matplotlib 20pt 的视觉大小，跨工具对比时容易混淆

### 9.2 公众号平台约束

- 纯白 `#ffffff` 背景是最安全的选择，避免在微信深色模式下出现偏色
- SVG 文件中文本必须为可编辑 text 节点 (非 path)，才能在微信内置浏览器中正确回退字体
- 图表文字在手机屏幕 (375px 宽) 上缩小 50% 仍需可读 → 因此 FT 最小 18pt

### 9.3 多行描述的换行

描述区使用 `\n` 手动换行，`lines` 参数为实际行数：
```python
'这五座城市代表了中国五种典型气候区，日照和温度较为具备代表性。\n看最左和最右：拉萨日照最强(~5.9)又凉爽(~8°C)；哈尔滨日照最弱(~3.8)又寒冷(~6°C)。'
```
`lines=2` → `desc_h = 0.05 + 2 × 0.04 = 0.13`

---

## 10. 快速启动

```bash
# 生成全部 5 张图 (SVG + PNG)
cd figures/data_charts
python generate_all_png.py

# 输出:
#   fig2_5cities_climate_cn.svg / .png
#   fig3_energy_seasonality_cn.svg / .png
#   fig4_photoperiod_storage_cn.svg / .png
#   fig5_5cities_config_cn.svg / .png
#   fig6_lcoe_comparison_cn.svg / .png
# === v24 done ===
```

修改配色/字号只需编辑文件顶部的 `C`, `FT`, `FD`, `FLB`, `FTK`, `FAN` 常量，所有图一次生效。

---

*Last updated: 2026-04-27 · v24 consolidated script*
