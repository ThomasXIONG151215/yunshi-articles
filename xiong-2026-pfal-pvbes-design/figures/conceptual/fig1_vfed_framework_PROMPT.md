# Fig1: VFED框架架构图 AI生成提示词
# Fig1: VFED Framework Architecture - AI Generation Prompts

> 本文档提供Fig1的AI图像生成提示词，可用于Midjourney、DALL-E、Stable Diffusion等工具

---

## 图件规格

- **尺寸**: 1200×800px (3:2比例)
- **风格**: Swiss Pulse学术技术风格，极简、数据驱动
- **背景**: #faf9f5 (暖白)
- **主文字**: #141413 (近黑)
- **强调色**: #d97757 (暖橙), #4285f4 (蓝), #059669 (绿)
- **字体**: Arial / Microsoft YaHei

---

## 视觉背景

VFED (Vertical Farm Energy Designer) 仿真优化框架，服务于**同一个基准单元**：20英尺海运集装箱植物工厂（波纹金属箱体，16m²种植面积，内部多层紫色LED栽培架）。

四层级从下到上：
1. **Climate Data** - 气象数据与EnergyPlus热模型集成（温度、太阳辐射、湿度）
2. **Hybrid Modeling** - 光伏单二极管模型 + 储能充放电模型 + 植物工厂负荷模型耦合
3. **Optimization** - 441种PVBES配置 × 24种光周期 = 10584种组合，逐小时能量平衡仿真
4. **Economic Eval** - LCOE最小化、PBP分析，输出最优设计

---

## 中文提示词 (Chinese)

```
科技信息图风格，学术技术文档排版设计。

[VISUAL CONTEXT]
画面中央是VFED仿真优化框架的四层级垂直堆叠结构，服务于同一个基准单元：一个20英尺海运集装箱改造的垂直植物工厂（波纹金属箱体，16m²种植面积，内部紫色LED灯照射的多层栽培架）。

FOUR HORIZONTAL LAYERS从下到上用箭头连接，每层用不同颜色区分：

BOTTOM BAR (蓝色 #4285f4，高度中等)：标注"实测数据" — 将当地气象数据（温度、太阳辐射、湿度）通过EnergyPlus建筑能耗模型输入

SECOND BAR (橙色 #d97757，高度中等)：标注"混合建模" — 光伏单二极管模型、储能充放电模型、植物工厂负荷模型三者耦合

THIRD BAR (深橙色 #c75b39，最高最醒目，高度是其他层的2倍)：中心只显示一个数字"10584"，用超大字号 — 代表441种PVBES配置 × 24种光周期起始时刻，逐小时能量平衡仿真

TOP BAR (绿色 #059669，高度中等)：标注"经济评估" — 以LCOE最小化和投资回收期(PBP)为目标，输出最优设计

[STYLE]
背景：#faf9f5 暖白色
主文字：#141413 近黑色
整体风格：瑞士极简主义数据图表，网格布局，精确干净，无多余装饰
每层之间用细箭头连接，表示数据流向
底部中央放置一个简化集装箱示意图，暗示所有层级都服务于这个基准单元

[LAYOUT]
四层横向色带从左到右贯穿画面，每层高度不同但宽度相同
第三层(10584)最突出，字体最大
层与层之间有清晰的分隔线
整体比例3:2，宽度1200px
```

---

## English Prompt (英文)

```
A bold infographic poster (1200×800px, 3:2 ratio) in Swiss minimalist academic style.

[VISUAL CONTEXT]
At center: the VFED (Vertical Farm Energy Designer) simulation-optimization framework — four horizontal layers stacked vertically, all serving ONE baseline unit: a 20-foot shipping container vertical plant factory (corrugated metal exterior, 16m² growing area, purple LED-lit multi-tier cultivation racks inside).

FOUR HORIZONTAL COLOR BARS spanning edge-to-edge, connected by upward arrows:

BOTTOM BAR (blue #4285f4, medium height): Label "Climate Data" — meteorological data (temperature, solar radiation, humidity) integrated with EnergyPlus building energy model

SECOND BAR (orange #d97757, medium height): Label "Hybrid Modeling" — PV single-diode model + BES charge/discharge model + PFAL load model coupled

THIRD BAR (deep orange #c75b39, TALLEST — 2x height of others): ONLY ONE MASSIVE NUMBER "10584" in bold white, dominating the bar — representing 441 PVBES configs × 24 photoperiod start times, hour-by-hour energy balance simulation

TOP BAR (green #059669, medium height): Label "Economic Eval" — LCOE minimization and PBP analysis output optimal system design

[STYLE]
Background: #faf9f5 warm off-white
Primary text: #141413 near-black
Style: Swiss minimalist data visualization, grid-based layout, precise and clean, zero decoration
Thin arrows connect each layer showing data flow direction
At bottom center: a simplified container silhouette suggesting all layers serve this baseline unit

[COMPOSITION]
Four horizontal color bars spanning full width, varying heights
Layer 3 (10584) is the hero element — dramatically larger font than all other text
Clear visual separation between layers
Aspect ratio 3:2
```

---

## 中文版提示词 (简化版)

```
[视觉背景]
四层级框架架构图，从下到上：
1. 蓝色底层 - "实测数据" (气象数据+EnergyPlus)
2. 橙色第二层 - "混合建模" (光伏+储能+负荷模型)
3. 深橙第三层(最高) - 仅一个数字 "10584" (441×24配置组合)
4. 绿色顶层 - "经济评估" (LCOE+PBP优化)

[风格]
瑞士极简学术风格，暖白背景(#faf9f5)，近黑文字(#141413)
每层用不同颜色，层间箭头连接
第三层10584是视觉焦点，字号远超其他文字
底部有简化集装箱轮廓，暗示框架服务于同一基准单元

[构图]
四层横向色带从左贯穿到右，高度不一但宽度一致
第三层最醒目
比例3:2，清晰干净无装饰
```

---

## 备选方案：垂直堆叠风格

如果横向构图不适合，改为垂直向下流动的布局：

```
[ALTERNATIVE - Vertical Flow]
科技信息图风格。

VFED框架四层级垂直向下流动，每层之间用粗箭头连接：

最上方(起点) - 蓝色方框："实测数据" + 气象数据图标
↓ 箭头
第二层 - 橙色方框："混合建模" + 光伏板/电池/负荷图标
↓ 箭头
第三层(最大) - 深橙背景 + 超大白色数字"10584"
↓ 箭头
最下方(终点) - 绿色方框："最优设计" + LCOE数值

底部中央：简化20ft集装箱侧视图，暗示这是所有计算的基准

背景#faf9f5，Swiss简约风格。
```

---

## 输出要求

1. **文件格式**: PNG透明背景或#faf9f5背景
2. **尺寸**: 1200×800px
3. **文字**: 确保所有数字和标签清晰可读
4. **中文版**: 中文标签 (实测数据/混合建模/经济评估)
5. **英文版**: 英文标签 (Climate Data / Hybrid Modeling / Economic Eval)
