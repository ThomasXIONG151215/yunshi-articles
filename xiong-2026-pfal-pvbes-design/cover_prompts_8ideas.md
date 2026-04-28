# VFED 封面设计 Prompt（YouTube/B站视频封面标准 · 中文极简 · 含视觉背景描述）

## 视觉背景（每条Prompt的第一段，帮助AI理解画什么）

> **集装箱植物工厂**是一个标准20英尺(约6米长)的海运集装箱改造的农业设施。外部：金属波纹板箱体、灰/深灰色、顶部有通风口和光伏板支架、底部有车轮或支撑脚。内部（如果可见）：多层栽培架整齐排列，紫色/品红色LED植物生长灯照射，翠绿色生菜或叶菜成排生长，白色栽培槽，精密传感器和管道可见。**光伏板**：深蓝色或黑色矩形面板，呈阵列排列，有时带银色铝合金边框，可安装在集装箱屋顶或地面。**储能电池**：冰箱大小的长方体金属柜，绿色指示灯或显示屏，通过电缆与光伏板和集装箱连接。**整体场景**：通常位于城市屋顶、工业园区或开阔沙漠/戈壁地面，暗示分布式部署。

## 共性数据（每段Prompt的精确背景）
- 20ft集装箱，16m²种植面积，基准案例在上海
- VFED仿真框架优化了10584种PV-BES-光周期配置组合
- 5城市结果（光伏面积）：拉萨40m²、海口50m²、上海80m²、乌鲁木齐110m²、哈尔滨120m²
- 核心发现：凌晨光周期(3-5点启动)比传统晚间策略减少储能需求40%
- 全年实测数据验证(2024上海，小时分辨率)，目标近能源自主(TGD<5%)

## 封面通用规则
- 1280×720 (16:9)，YouTube/B站视频封面
- **每张封面最多1-2个中文大字**，无段落、无标签、无归属
- 字号≥画面高度1/5，手机50%缩放仍清晰
- 高对比度、强视觉焦点、一瞥即懂


## 方向1：前后对比型 —— 唯一文字："差40%"

**视觉背景**：集装箱植物工厂是一个标准20英尺海运集装箱改造的农业设施。外部有金属波纹板箱体、通风口、光伏板支架。内部多层栽培架上紫色LED灯光照下翠绿生菜成排生长。左侧画面展示低效配置——过多电池柜堆积，光伏板散乱，工厂显得压抑拥挤。右侧展示VFED优化后——光伏板整齐排列在屋顶与地面，与太阳轨迹完美对齐，一个紧凑电池柜安静置于工厂旁，画面开阔清爽。

**英文Prompt**：
```
A dramatic YouTube thumbnail (1280x720, 16:9) split vertically into two halves.

VISUAL CONTEXT: The subject is a 20-foot shipping container converted into a vertical plant factory — corrugated metal exterior, ventilation units on top, solar panel mounting rails. Inside (visible through cutaway or open doors): multiple tiers of cultivation racks, purple LED grow lights illuminating rows of vibrant green lettuce, white cultivation trays, precision irrigation tubes.

LEFT HALF: This container factory is buried under oversized battery cabinets (industrial gray metal boxes with green indicator lights, each the size of a refrigerator), scattered solar panels (dark blue rectangles with silver aluminum frames) placed haphazardly around it. The scene feels cluttered, oppressive, with reddish-brown industrial tones. The factory looks weighed down.

RIGHT HALF: The IDENTICAL container factory now has its solar panels arranged in a clean grid on its roof and on the ground beside it. A golden energy arc flows from the sun directly to the factory. A single compact battery cabinet sits quietly below — efficient, minimal. The scene is bright, blue-white, optimistic, with open space around the factory.

ONE LINE OF LARGE RED CHINESE TEXT "差40%" spans across the dividing line — "差" on the left, "40%" on the right. The number fills 1/5 of frame height. The vertical dividing line glows orange. NO other text, NO labels, NO attribution.

The visual contrast between the two halves must be DRAMATIC and immediately legible at mobile thumbnail size. Style: bold graphic design, not photorealistic. High contrast.
```


## 方向2：城市叠加型 —— 唯一文字："同一个基准"

**视觉背景**：每个城市上方的数字代表为该城市一个集装箱植物工厂（20ft，16m²种植）实现能源自主所需的光伏板面积。光伏板是深蓝色矩形阵列面板。每个城市的天际线用标志性建筑识别：拉萨-布达拉宫轮廓，海口-椰树，上海-东方明珠陆家嘴，乌鲁木齐-天山博格达峰，哈尔滨-冰雪大世界/索菲亚教堂。

**英文Prompt**：
```
A panoramic YouTube thumbnail (1280x720, 16:9).

VISUAL CONTEXT: The same baseline unit — a 20-foot shipping container plant factory (corrugated metal box, 16m² growing area inside, purple LED-lit vertical lettuce racks) — requires DRAMATICALLY different solar panel coverage in different Chinese cities. Solar panels are dark blue rectangular arrays with silver aluminum frames.

BACKGROUND: A faint outline of China's geography in warm beige.
FOREGROUND: Five city skyline silhouettes in a row, each distinct:
- LHASA: Potala Palace silhouette, crystalline blue sky tone. Above it floats a solar array with MASSIVE NUMBER "40m²"
- HAIKOU: Palm tree silhouette, tropical yellow. Floating solar array: "50m²"
- SHANGHAI: Oriental Pearl Tower + Lujiazui skyline, warm orange. Floating solar array: "80m²" — THIS ONE GLOWS subtly as the baseline case
- URUMQI: Bogda Peak mountain silhouette, continental purple. Floating solar array: "110m²" — visibly larger
- HARBIN: St. Sophia Cathedral + ice palace silhouette, slate gray. Floating solar array: "120m²" — LARGEST

ONE LINE at top: LARGE WHITE BOLD CHINESE TEXT "同一个基准" spanning the full width. NO other text. The five numbers (40→50→80→110→120) create a visible staircase from left to right — the numbers ARE the message. They must be MASSIVE and immediately communicate the 3x difference between the smallest and largest.
```


## 方向3：数据仪表盘型 —— 唯一文字："10584"

**视觉背景**：中央的3D线框模型展示的是一个20英尺海运集装箱改造的垂直植物工厂——波纹金属外壳，内部透过半透明线框可见多层栽培架上的紫色LED光和绿色作物。左上角的圆形仪表显示光伏板面积（80m²，对应上海基准案例）。右上角的电池图标显示储能容量（50kWh）。底部的5个小色点代表论文测试的5个气候带。这就是VFED仿真框架运行的10584种配置组合所针对的同一个基准系统。

**英文Prompt**：
```
A sleek YouTube thumbnail (1280x720, 16:9) styled as a tech dashboard.

VISUAL CONTEXT: The 3D wireframe hologram at center shows a 20-foot shipping container converted into a vertical plant factory — corrugated metal exterior visible as wireframe lines, inside the semi-transparent model you can see multiple tiers of cultivation racks, purple LED glow, and green crops. This is the baseline system for which VFED tested 10,584 configuration combinations across 5 climate zones. Upper-left gauge: circular dial showing "80 m²" PV area (Shanghai baseline). Upper-right: battery icon showing "50 kWh" storage. Five tiny colored dots at bottom represent the 5 climate zones tested.

DARK BACKGROUND (#0a0e14) with subtle grid lines. CENTER STAGE: ONE MASSIVE GLOWING NUMBER "10584" in luminous white with a subtle blue halo — this number DOMINATES at least 50% of the frame area. The wireframe container sits BEHIND and BELOW the number, visible but subordinate. The number is the hero.

NO other text. NO labels. NO explanations. Just the number 10584 as pure visual impact. Style: clean sci-fi dashboard, Bloomberg Terminal elegance, not dystopian. The number must feel like a mission-critical readout.
```


## 方向4：集装箱+太阳弧线 ⭐ —— 唯一文字："−40%"

**视觉背景**：画面主体是VFED的基准单元——一个20英尺海运集装箱改造的垂直植物工厂。波纹金属外壳、顶部光伏板支架、底部支撑脚。内部隐约透出暖黄LED光（如果设计让内部可见，则有多层栽培架上的紫色灯光和翠绿生菜）。屋顶整齐排列深蓝色矩形光伏面板。**核心隐喻**：太阳轨迹弧线代表光周期优化——传统方案将植物工厂LED照明放在晚间(18:00开始)，光伏发电高峰(正午)与LED需求高峰之间存在时间错配，被迫用大量电池储存。VFED通过将光周期调整到凌晨(03:00开始)，让太阳光伏在正午高峰时段直接驱动LED照明，电池仅作为补充——这就是"−40%"的来源：储能容量需求削减40%。

**英文Prompt**：
```
A cinematic YouTube thumbnail (1280x720, 16:9).

VISUAL CONTEXT: The BASELINE UNIT is the hero — a 20-foot shipping container (approx. 6m long) converted into a vertical plant factory. Corrugated metal exterior in steel gray (#6b7280), rectangular ventilation units on the roof, support feet at the base. Neat rows of dark blue solar panels with silver aluminum frames mounted on the roof. Warm yellow LED light glows from within. Inside (if visible through an opening or cutaway): multi-tier white cultivation racks, purple LED grow lights, rows of vibrant green lettuce. This sits on a minimalist sandy ground with subtle grid lines, evoking a deployment site.

THE HERO VISUAL: A MASSIVE golden sun trajectory arc — thick, luminous, unmissable — sweeps diagonally from lower-left to upper-right across the entire frame like a master painter's single bold stroke. Three glowing dots mark time along the arc: "03:00" at dawn position (blue-white), "12:00" at apex (bright white), "20:00" at dusk (warm orange). Golden energy particles stream along the arc and cascade down into the container, showing solar energy becoming plant light.

SKY: Gradients from deep blue-black (upper-left, pre-dawn) through bright sky blue (center-top) to warm sunset orange (upper-right). The arc VISUALLY connects the sun's position to the container — the container sits at the receiving end of the arc's lower third.

RIGHT SIDE: ONE SINGLE LINE of MASSIVE GOLDEN BOLD CHINESE TEXT "−40%" — positioned vertically in the right third of the frame, anchoring the composition. The golden arc connects this number to the container, making the causality VISUAL: change the timing → save 40% storage.

NO other text, NO labels, NO attribution anywhere on the thumbnail. The −40% and the sun arc are the ENTIRE message.

Style: cinematic diagram meets architectural visualization. The arc must be the spine of the composition — every other element orbits around it. Ultra high contrast, phone-thumbnail ready.
```


## 方向5：框架结构图型 —— 唯一文字：第四层"10584" + 前三层各一词

**视觉背景**：VFED框架处理的是同一个基准系统——20英尺集装箱植物工厂（波纹金属箱体，16m²种植面积，内部多层紫色LED栽培架）。四层级从下到上分别是：(1)气候数据与EnergyPlus热模型——将当地气象数据（温度、太阳辐射、湿度）输入建筑能耗模型；(2)混合建模——将光伏单二极管模型、电池充放电模型、植物工厂负荷模型耦合；(3)参数扫描——对441种PV-BES配置和24种光周期起始时间进行全组合，共10584种配置逐小时能量平衡仿真；(4)经济评估——计算平准化能源成本(LCOE)和投资回收期(PBP)，输出最优设计。

**英文Prompt**：
```
A bold graphic YouTube thumbnail (1280x720, 16:9), pure white background (#faf9f5).

VISUAL CONTEXT: The VFED framework optimizes the energy system for ONE baseline unit — a 20-foot shipping container vertical plant factory (corrugated metal exterior, 16m² growing area, multi-tier purple LED-lit lettuce racks inside). The four horizontal bars represent the optimization pipeline that processes climate data through models, runs 10,584 simulations, and outputs economic decisions — all for this same container unit.

FOUR THICK HORIZONTAL COLOR BARS stacked from edge to edge, filling the entire frame:
- BOTTOM BAR (blue #4285f4, medium height): "实测数据" in bold white Chinese — 2024 Shanghai, hourly resolution, EnergyPlus
- SECOND BAR (orange #ea852e, medium height): "混合建模" in bold white — PV single-diode + BES charge/discharge + load models coupled
- THIRD BAR (deep orange #d97757, TALLEST — at least 2x the others): ONLY ONE MASSIVE NUMBER "10584" in bold white, filling the bar — 441 PVBES × 24 photoperiods, every combination simulated hour-by-hour for the container factory
- TOP BAR (green #059669, medium height): "经济评估" in bold white — LCOE minimization, PBP analysis, optimal system design for the 20ft container unit

Thick upward arrows connect each bar. The number "10584" in the third bar is the PUNCHLINE — it must be DRAMATICALLY larger than all other text, at least 3x the font size. NO subtitles, NO explanations beneath the bars. The bars are the only content. Style: Swiss graphic design, monument to methodology. Zero decoration.
```


## 方向6：5城市数据柱 ⭐ —— 唯一文字：柱顶5个数字 + 顶部"同一基准"

**视觉背景**：五根柱子的高度差异展示的是同一个基准系统在不同城市所需的光伏面积。基准单元：20英尺海运集装箱植物工厂（波纹金属箱体，16m²种植面积，内部多层紫色LED栽培架）。5个气候带从青藏高原（拉萨，年均太阳辐射5.88 kWh/m²/天，冷凉干燥，制冷需求低）到东北严寒（哈尔滨，年均太阳辐射仅3.81 kWh/m²/天，冬季日照极短，制热需求高）。柱子高度差异直接反映气候对光伏配置需求的3倍影响——同一个集装箱，在拉萨只需40m²光伏，在哈尔滨需要120m²。

**英文Prompt**：
```
A high-impact YouTube thumbnail (1280x720, 16:9), dark background (#141413).

VISUAL CONTEXT: Every bar represents the solar panel area required for the EXACT SAME baseline unit — a 20-foot shipping container vertical plant factory (corrugated metal box, 16m² growing area, multi-tier purple LED lettuce racks inside). The only variable is LOCATION: Lhasa (high-altitude plateau, abundant sun, low cooling load) vs Harbin (bitter winter, short daylight, high heating demand). The height difference between bars tells the entire story — 3x more PV area needed at the extremes.

FIVE VERTICAL BARS forming a dramatic staircase from left (shortest) to right (tallest):
- Bar 1 (cold blue #4285f4, SHORTEST): MASSIVE NUMBER "40" at top, tiny "m²" below. Represents Lhasa baseline.
- Bar 2 (warm yellow #f9a825): MASSIVE NUMBER "50" — Haikou
- Bar 3 (warm orange #ea852e, GLOWING subtly — the REFERENCE case): MASSIVE NUMBER "80" — Shanghai, where the 2024 full-year measured data validated the model
- Bar 4 (purple #9c6ade): MASSIVE NUMBER "110" — Urumqi, continental extreme
- Bar 5 (slate gray #64748b, TALLEST): MASSIVE NUMBER "120" — Harbin, requiring 3x the PV area of Lhasa

A thin horizontal baseline cuts across all bars: a faint line labeled "20ft集装箱 · 16m² · TGD<5%". ONE LINE at top edge: large white bold Chinese text "同一基准". The five numbers are the real text — they must be IMMENSE, at least 1/6 of total frame height each. The visual staircase from 40 to 120 must be UNMISTAKABLE. No city names, no labels beyond the baseline. Style: bold infographic monument to comparative data.
```


## 方向7：简洁学术型 —— 唯一文字："VFED" + "光伏储能设计基准"

**视觉背景**：VFED (Vertical Farm Energy Designer) 是这个仿真优化框架的名称。它处理的核心对象是一个20英尺集装箱植物工厂（波纹金属箱体，16m²种植面积，多层紫色LED栽培架），通过10584次仿真为5个气候带生成了光伏储能系统的设计基准。这个封面不展示具体图形，而是用极简排版传递学术权威感——框架的名称本身就是品牌。

**英文Prompt**：
```
An ultra-minimalist YouTube thumbnail (1280x720, 16:9).

VISUAL CONTEXT: VFED (Vertical Farm Energy Designer) is the simulation-optimization framework name. It processes climate data for the SAME baseline unit — a 20-foot shipping container plant factory (corrugated metal box, 16m² growing area, multi-tier purple LED-lit vertical racks) — across 5 Chinese climate zones, running 10,584 configuration simulations to produce PV+BES design baselines. This cover communicates that authority through pure typography alone — the framework's name IS the brand.

NEAR-BLACK BACKGROUND (#141413). CENTER: three MASSIVE letters "VFED" in ultra-thin weight sans-serif (weight 100), extremely wide letter spacing, soft white with subtle luminosity — filling approximately 50% of the frame area. Below, ONE LINE of golden Chinese text (#d97757): "光伏储能设计基准" at medium size. A single hairline rule spans the top edge. Top-left corner: the tiniest possible gray annotation "10,584 simulations".

THAT IS EVERYTHING. No icons, no container image, no charts, no attribution, no decoration whatsoever. The emptiness surrounding the letters IS the design. Style: Hermès catalog meets Nature journal cover. Pure typographic authority. The letters must feel like they were carved from light itself.

Warning for AI: If you add ANY graphic element — a container, a solar panel, a leaf, a chart, a line that isn't the top hairline — you have FAILED this prompt. The letters are the image.
```


## 方向8：植物工厂+太阳 —— 唯一文字："光到菜"

**视觉背景**：上半部分展示的是一线实景——20英尺海运集装箱改造的垂直植物工厂内部。波纹金属外壳的内壁可见，多层白色栽培架从地板延伸到天花板，紫色/品红色LED植物生长灯条照射下方，翠绿色生菜（奶油生菜或罗马生菜）成排生长在白色栽培槽中，精密滴灌管道和传感器可见，空气质量监测显示屏在角落闪烁。**这是"菜"的终点**。从左上角切入的金色太阳光线是"光"的起点——它代表光伏发电，从太阳到光伏板到电池到LED再到作物，一条能量链。VFED框架让这条链上的每个环节都被精确计算过。

**英文Prompt**：
```
A magazine-quality YouTube thumbnail (1280x720, 16:9) in two visual zones connected by light.

VISUAL CONTEXT: The upper zone shows the destination — inside a 20-foot shipping container vertical plant factory. Corrugated metal interior walls visible, multi-tier white cultivation racks floor to ceiling, purple/magenta LED grow light strips illuminating rows of vibrant green butter lettuce, white cultivation trays with precision drip irrigation tubes, environmental sensors and a small monitor glowing in the corner. This is "菜" (the crop).

The golden sun ray entering from upper-left originates from "光" (the light) — it represents the solar PV energy chain: sun → solar panels → battery storage → LED lights → crop. VFED optimizes every link in this chain across 10,584 configuration combinations.

UPPER ZONE (60% of frame): the immersive plant factory interior as described above, lit with a dramatic golden sun ray angling diagonally from the upper-left corner, creating a natural-meets-artificial lighting mix across the lettuce rows. The ray feels physical — it should look like it's actually illuminating the leaves.

LOWER ZONE (40%): a dark band (#141413) with a single subtle glowing flow diagram: "PV → BES → LED → 作物" in tech-blue, connecting the sun ray above to the final crop.

CENTER OVERLAY, spanning across both zones: ONE LINE of MASSIVE GOLDEN BOLD CHINESE TEXT "光到菜" — filling the middle third of the thumbnail horizontally, with a subtle dark glow behind the text for readability against both the bright photo and dark band. The golden text must feel like it belongs to the sun ray — as if the ray itself wrote the words.

NO other text, NO attribution, NO labels. Style: WIRED magazine cover photography meets cinematic lighting design. The text "光到菜" and the sun ray are a single visual unit — they tell the complete story.
```

---

## 推荐矩阵

| 方向 | 文字 | 视觉冲击 | 手机可读 | 数据说服 | 综合 |
|------|------|---------|---------|---------|------|
| 1.前后对比 | "差40%" | ★★★★ | ★★★★★ | ★★★ | ★★★★ |
| 2.城市叠加 | "同一个基准" | ★★★ | ★★★★ | ★★★★ | ★★★ |
| 3.仪表盘 | "10584" | ★★★★ | ★★★★★ | ★★★ | ★★★★ |
| **4.集装箱+太阳** | **"−40%"** | **★★★★★** | **★★★★★** | **★★★★** | **★★★★★** |
| 5.框架结构 | "10584"为主 | ★★★ | ★★★★ | ★★★ | ★★★ |
| 6.5城市数据 | "同一基准"+数字 | ★★★★ | ★★★★★ | ★★★★★ | ★★★★ |
| 7.简洁学术 | "VFED" | ★★ | ★★★★ | ★ | ★ |
| 8.植物工厂+太阳 | "光到菜" | ★★★★★ | ★★★★★ | ★★★ | ★★★★★ |
