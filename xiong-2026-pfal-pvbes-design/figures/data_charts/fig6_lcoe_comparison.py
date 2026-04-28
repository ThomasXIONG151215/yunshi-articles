"""
Fig6: 平准化能源成本(LCOE)与电网电价对比
Levelized Cost of Energy (LCOE) vs. Grid Electricity Price

柱状图：电网电价 vs 3年PBP vs 5年PBP，标注节省比例
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
    'gray': '#7f7f7f'
}

# LCOE数据 ($/kWh)
labels_cn = ['电网电价\n(上海)', '3年PBP最优', '5年PBP最优']
labels_en = ['Grid Price\n(Shanghai)', '3-Year PBP Optimal', '5-Year PBP Optimal']

# 数值: 电网0.096, 3年PBP 0.034-0.042(取中值0.038), 5年PBP 0.032-0.039(取中值0.0355)
lcoe_values = [0.096, 0.038, 0.0355]

# 节省比例计算 (相对于电网电价)
savings = [(1 - v/0.096) * 100 for v in lcoe_values]

# 五城市LCOE排名数据 (3年PBP, $kWh)
cities_cn = ['拉萨', '海口', '上海', '乌鲁木齐', '哈尔滨']
cities_en = ['Lhasa', 'Haikou', 'Shanghai', 'Urumqi', 'Harbin']
city_lcoe_3yr = [0.032, 0.034, 0.038, 0.040, 0.042]  # 近似值

def create_fig6_lcoe_comparison(lang='cn'):
    """生成LCOE对比图"""
    title_cn = '平准化能源成本(LCOE)与电网电价对比'
    title_en = 'Levelized Cost of Energy (LCOE) vs. Grid Price'
    yaxis_title_cn = 'LCOE ($/kWh)'
    yaxis_title_en = 'LCOE ($/kWh)'

    title = title_cn if lang == 'cn' else title_en
    yaxis_title = yaxis_title_cn if lang == 'cn' else yaxis_title_en
    labels = labels_cn if lang == 'cn' else labels_en

    fig = go.Figure()

    # 颜色列表
    bar_colors = [COLORS['gray'], COLORS['data_blue'], COLORS['green']]

    # 主柱状图
    fig.add_trace(go.Bar(
        x=labels,
        y=lcoe_values,
        name='LCOE',
        marker_color=bar_colors,
        width=0.5,
        text=[f'${v:.3f}' for v in lcoe_values],
        textposition='outside',
        textfont=dict(size=14, color=[COLORS['primary_text']] * 3),
        hovertemplate='%{x}<br>LCOE: $%{y:.3f}/kWh<extra></extra>'
    ))

    # 标注节省比例
    annotations = [
        dict(x=1, y=0.055, text='节省40%' if lang == 'cn' else '40% Savings',
             showarrow=True, arrowhead=2, arrowsize=1, arrowcolor=COLORS['data_blue']),
        dict(x=2, y=0.05, text='节省63%' if lang == 'cn' else '63% Savings',
             showarrow=True, arrowhead=2, arrowsize=1, arrowcolor=COLORS['green'])
    ]

    fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            font=dict(size=20, family='Arial, Microsoft YaHei', color=COLORS['primary_text'])
        ),
        paper_bgcolor=COLORS['background'],
        plot_bgcolor=COLORS['background'],
        font=dict(family='Arial, Microsoft YaHei', size=14, color=COLORS['primary_text']),
        showlegend=False,
        xaxis=dict(
            showgrid=False,
            tickfont=dict(size=14),
            title=dict(text='')
        ),
        yaxis=dict(
            title=dict(text=yaxis_title, font=dict(size=14)),
            range=[0, 0.12],
            gridcolor=COLORS['grid'],
            linewidth=2,
            linecolor=COLORS['primary_text'],
            tickfont=dict(size=12),
            tickformat='$.3f'
        ),
        annotations=annotations,
        hovermode='x unified'
    )

    return fig


def create_fig6b_city_lcoe(lang='cn'):
    """生成五城市LCOE排名图"""
    title_cn = '五城市LCOE排名 (3年投资回收期)'
    title_en = '5-City LCOE Ranking (3-Year PBP)'
    yaxis_title_cn = 'LCOE ($/kWh)'
    yaxis_title_en = 'LCOE ($/kWh)'

    title = title_cn if lang == 'cn' else title_en
    yaxis_title = yaxis_title_cn if lang == 'cn' else yaxis_title_en
    cities = cities_cn if lang == 'cn' else cities_en

    # 颜色渐变: 从低(绿)到高(橙)
    colors = [COLORS['green'], COLORS['data_blue'], COLORS['data_blue'],
              COLORS['accent'], COLORS['accent']]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=cities,
        y=city_lcoe_3yr,
        name='LCOE',
        marker_color=colors,
        width=0.6,
        text=[f'${v:.3f}' for v in city_lcoe_3yr],
        textposition='outside',
        textfont=dict(size=12, color=COLORS['primary_text']),
        hovertemplate='%{x}<br>LCOE: $%{y:.3f}/kWh<extra></extra>'
    ))

    fig.update_layout(
        title=dict(
            text=title,
            x=0.5,
            font=dict(size=18, family='Arial, Microsoft YaHei', color=COLORS['primary_text'])
        ),
        paper_bgcolor=COLORS['background'],
        plot_bgcolor=COLORS['background'],
        font=dict(family='Arial, Microsoft YaHei', size=14, color=COLORS['primary_text']),
        showlegend=False,
        xaxis=dict(
            showgrid=False,
            tickfont=dict(size=14),
            title=dict(text='')
        ),
        yaxis=dict(
            title=dict(text=yaxis_title, font=dict(size=14)),
            range=[0, 0.05],
            gridcolor=COLORS['grid'],
            linewidth=2,
            linecolor=COLORS['primary_text'],
            tickfont=dict(size=12),
            tickformat='$.3f'
        ),
        hovermode='x unified'
    )

    return fig


if __name__ == '__main__':
    # 主图: LCOE对比
    fig6_cn = create_fig6_lcoe_comparison('cn')
    fig6_en = create_fig6_lcoe_comparison('en')

    # HTML first
    fig6_cn.write_html('fig6_lcoe_comparison_cn.html')
    fig6_en.write_html('fig6_lcoe_comparison_en.html')
    print('Fig6 HTML generated')

    # PNG
    try:
        fig6_cn.write_image('fig6_lcoe_comparison_cn.png', width=1200, height=600, scale=2)
        fig6_en.write_image('fig6_lcoe_comparison_en.png', width=1200, height=600, scale=2)
        print('Fig6 PNG generated')
    except Exception as e:
        print(f'Fig6 PNG skipped: {e}')

    # 副图: 五城市LCOE排名
    fig6b_cn = create_fig6b_city_lcoe('cn')
    fig6b_en = create_fig6b_city_lcoe('en')

    fig6b_cn.write_html('fig6b_city_lcoe_cn.html')
    fig6b_en.write_html('fig6b_city_lcoe_en.html')

    try:
        fig6b_cn.write_image('fig6b_city_lcoe_cn.png', width=1200, height=500, scale=2)
        fig6b_en.write_image('fig6b_city_lcoe_en.png', width=1200, height=500, scale=2)
        print('Fig6b PNG generated')
    except Exception as e:
        print(f'Fig6b PNG skipped: {e}')

    print('Fig6 complete')
