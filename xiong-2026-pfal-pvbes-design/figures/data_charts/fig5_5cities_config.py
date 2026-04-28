"""
Fig5: 五城市近能源自主系统配置对比
5-City Near-Energy-Autonomous System Configuration

分组柱状图：光伏面积(蓝) + 储能容量(橙)
目标: TGD<5%, 20ft集装箱, 16m²
"""
import plotly.graph_objects as go
import numpy as np

# 统一配色方案
COLORS = {
    'background': '#faf9f5',
    'primary_text': '#141413',
    'accent': '#d97757',
    'data_blue': '#4285f4',
    'grid': '#e8e6dc',
    'green': '#059669',
    'purple': '#9c6ade',
    'warm_yellow': '#f9a825',
    'slate_gray': '#64748b'
}

# 五城市配置数据 (TGD<5%, 20ft集装箱, 16m²种植面积)
cities_cn = ['拉萨', '海口', '上海', '乌鲁木齐', '哈尔滨']
cities_en = ['Lhasa', 'Haikou', 'Shanghai', 'Urumqi', 'Harbin']
pv_area = [40, 50, 80, 110, 120]  # m²
storage = [40, 45, 50, 45, 50]  # kWh

# 颜色
city_colors = [
    COLORS['data_blue'],   # 拉萨 - 蓝
    COLORS['warm_yellow'],  # 海口 - 黄
    COLORS['accent'],       # 上海 - 橙(参考案例)
    COLORS['purple'],       # 乌鲁木齐 - 紫
    COLORS['slate_gray']   # 哈尔滨 - 灰
]

def create_fig5_5cities_config(lang='cn'):
    """生成五城市系统配置对比图"""
    title_cn = '五城市近能源自主系统配置 (TGD<5%)'
    title_en = 'Near-Energy-Autonomous System Configurations (TGD<5%)'
    subtitle_cn = '20尺集装箱植物工厂 · 16m²种植面积'
    subtitle_en = '20ft Container PFAL · 16m² Growing Area'
    yaxis_title_cn = '系统规模'
    yaxis_title_en = 'System Size'
    pv_label_cn = '光伏面积 (m²)'
    pv_label_en = 'PV Area (m²)'
    storage_label_cn = '储能容量 (kWh)'
    storage_label_en = 'Storage (kWh)'

    title = title_cn if lang == 'cn' else title_en
    subtitle = subtitle_cn if lang == 'cn' else subtitle_en
    yaxis_title = yaxis_title_cn if lang == 'cn' else yaxis_title_en
    pv_label = pv_label_cn if lang == 'cn' else pv_label_en
    storage_label = storage_label_cn if lang == 'cn' else storage_label_en
    cities = cities_cn if lang == 'cn' else cities_en

    fig = go.Figure()

    # 柱状图组1: 光伏面积
    fig.add_trace(go.Bar(
        x=cities,
        y=pv_area,
        name=pv_label,
        marker_color=[COLORS['data_blue']] * 5,
        width=0.35,
        offset=0,
        text=pv_area,
        textposition='outside',
        textfont=dict(size=12, color=COLORS['data_blue']),
        hovertemplate='%{x}<br>PV: %{y} m²<extra></extra>'
    ))

    # 柱状图组2: 储能容量 (叠加显示)
    fig.add_trace(go.Bar(
        x=cities,
        y=storage,
        name=storage_label,
        marker_color=[COLORS['accent']] * 5,
        width=0.35,
        offset=0.4,
        text=storage,
        textposition='outside',
        textfont=dict(size=12, color=COLORS['accent']),
        hovertemplate='%{x}<br>Storage: %{y} kWh<extra></extra>'
    ))

    # 标注3倍差异
    fig.add_annotation(
        x=4,
        y=125,
        text='×3' if lang == 'cn' else '×3',
        showarrow=False,
        font=dict(size=24, color=COLORS['accent']),
        bgcolor='rgba(250, 249, 245, 0.8)',
        bordercolor=COLORS['accent'],
        borderwidth=2,
        borderpad=6
    )

    fig.update_layout(
        title=dict(
            text=f'{title}<br><sub>{subtitle}</sub>',
            x=0.5,
            font=dict(size=18, family='Arial, Microsoft YaHei', color=COLORS['primary_text'])
        ),
        paper_bgcolor=COLORS['background'],
        plot_bgcolor=COLORS['background'],
        font=dict(family='Arial, Microsoft YaHei', size=14, color=COLORS['primary_text']),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.05,
            xanchor='center',
            x=0.5,
            font=dict(size=12)
        ),
        barmode='group',
        xaxis=dict(
            showgrid=False,
            tickfont=dict(size=14),
            title=dict(text='')
        ),
        yaxis=dict(
            title=dict(text=yaxis_title, font=dict(size=14)),
            range=[0, 150],
            gridcolor=COLORS['grid'],
            linewidth=2,
            linecolor=COLORS['primary_text'],
            tickfont=dict(size=12)
        ),
        hovermode='x unified'
    )

    return fig


if __name__ == '__main__':
    fig_cn = create_fig5_5cities_config('cn')
    fig_en = create_fig5_5cities_config('en')

    # HTML first (always works)
    fig_cn.write_html('fig5_5cities_config_cn.html')
    fig_en.write_html('fig5_5cities_config_en.html')
    print('HTML generated')

    # PNG (requires kaleido, may fail on some systems)
    try:
        fig_cn.write_image('fig5_5cities_config_cn.png', width=1200, height=600, scale=2)
        fig_en.write_image('fig5_5cities_config_en.png', width=1200, height=600, scale=2)
        print('PNG generated')
    except Exception as e:
        print(f'PNG export skipped: {e}')

    print('Fig5 complete')
