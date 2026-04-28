"""
Fig2: 五城市光伏资源与储能配置对比
5-City PV Resource & Storage Configuration Comparison

双Y轴柱状图：光伏辐射(蓝) + 储能容量(橙线)
"""
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np

# 统一配色方案 (Swiss Pulse Academic Style)
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

# 城市数据
cities_cn = ['拉萨', '海口', '上海', '乌鲁木齐', '哈尔滨']
cities_en = ['Lhasa', 'Haikou', 'Shanghai', 'Urumqi', 'Harbin']
pv_resource = [5.88, 4.72, 4.25, 4.21, 3.81]  # kWh/m²/day
storage_capacity = [40, 45, 50, 45, 50]  # kWh

def create_fig2_5cities_climate(lang='cn'):
    """生成五城市光伏资源与储能配置对比图"""
    title_cn = '五城市光伏资源与储能配置对比'
    title_en = 'PV Resource & Storage Configuration: 5 Cities Comparison'
    yaxis1_title_cn = '年均光伏辐射 (kWh/m²/天)'
    yaxis1_title_en = 'Avg. PV Resource (kWh/m²/day)'
    yaxis2_title_cn = '储能容量需求 (kWh)'
    yaxis2_title_en = 'Storage Capacity (kWh)'

    title = title_cn if lang == 'cn' else title_en
    yaxis1_title = yaxis1_title_cn if lang == 'cn' else yaxis1_title_en
    yaxis2_title = yaxis2_title_cn if lang == 'cn' else yaxis2_title_en
    cities = cities_cn if lang == 'cn' else cities_en

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # 柱状图: 光伏辐射
    fig.add_trace(
        go.Bar(
            x=cities,
            y=pv_resource,
            name='光伏辐射' if lang == 'cn' else 'PV Resource',
            marker_color=COLORS['data_blue'],
            width=0.6,
            hovertemplate='%{x}<br>%{y:.2f} kWh/m²/day<extra></extra>'
        ),
        secondary_y=False
    )

    # 折线+点: 储能容量
    fig.add_trace(
        go.Scatter(
            x=cities,
            y=storage_capacity,
            name='储能容量' if lang == 'cn' else 'Storage',
            mode='lines+markers+text',
            line=dict(color=COLORS['accent'], width=3),
            marker=dict(size=12, color=COLORS['accent']),
            text=storage_capacity,
            textposition='top center',
            textfont=dict(size=14, color=COLORS['accent']),
            hovertemplate='%{x}<br>Storage: %{y} kWh<extra></extra>'
        ),
        secondary_y=True
    )

    fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            font=dict(size=20, family='Arial, Microsoft YaHei', color=COLORS['primary_text'])
        ),
        paper_bgcolor=COLORS['background'],
        plot_bgcolor=COLORS['background'],
        font=dict(family='Arial, Microsoft YaHei', size=14, color=COLORS['primary_text']),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='center',
            x=0.5,
            font=dict(size=12)
        ),
        hovermode='x unified',
        xaxis=dict(
            showgrid=False,
            tickfont=dict(size=14),
            title=dict(text='')
        )
    )

    fig.update_yaxes(
        title_text=yaxis1_title,
        secondary_y=False,
        range=[0, 7],
        gridcolor=COLORS['grid'],
        linewidth=2,
        linecolor=COLORS['primary_text'],
        tickfont=dict(size=12),
        showgrid=True
    )

    fig.update_yaxes(
        title_text=yaxis2_title,
        secondary_y=True,
        range=[0, 70],
        gridcolor='rgba(255,255,255,0)',
        linewidth=2,
        linecolor=COLORS['primary_text'],
        tickfont=dict(size=12),
        showgrid=False
    )

    return fig


if __name__ == '__main__':
    # 生成中英文版本
    fig_cn = create_fig2_5cities_climate('cn')
    fig_en = create_fig2_5cities_climate('en')

    # 保存HTML (PNG导出需要kaleido如有报错可注释掉)
    try:
        fig_cn.write_image('fig2_5cities_climate_cn.png', width=1200, height=600, scale=2)
        fig_en.write_image('fig2_5cities_climate_en.png', width=1200, height=600, scale=2)
        print('PNG files generated')
    except Exception as e:
        print(f'PNG export skipped: {e}')

    fig_cn.write_html('fig2_5cities_climate_cn.html')
    fig_en.write_html('fig2_5cities_climate_en.html')
    print('HTML files generated: fig2_5cities_climate_cn.html, fig2_5cities_climate_en.html')
