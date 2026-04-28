"""
Fig3: 全年能耗季节性分解
Annual Energy Consumption Seasonality (Shanghai PFAL)

堆叠面积图：LED照明(蓝) + 空调(橙) + 其他(灰)
"""
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# 统一配色方案
COLORS = {
    'background': '#faf9f5',
    'primary_text': '#141413',
    'accent': '#d97757',
    'data_blue': '#4285f4',
    'grid': '#e8e6dc',
    'green': '#059669',
    'light_gray': '#e8e6dc'
}

# 上海全年能耗数据 (kWh/天) - 基于论文实测数据
months_cn = ['1月', '4月', '7月', '10月', '12月']
months_en = ['Jan', 'Apr', 'Jul', 'Oct', 'Dec']
month_labels = ['Jan', 'Apr', 'Jul', 'Oct', 'Dec']

# 能耗分解数据
led = [15, 15, 18, 15, 14]  # LED相对稳定
ac = [4, 8, 25, 18, 4]  # 空调季节性变化大
other = [5, 5, 5, 5, 5]  # 风机等相对稳定
total = [24, 28, 48, 38, 23]  # 总能耗

def create_fig3_energy_seasonality(lang='cn'):
    """生成全年能耗季节性分解图"""
    title_cn = '上海集装箱植物工厂全年能耗分解'
    title_en = 'Annual Energy Consumption Breakdown, Shanghai PFAL'
    yaxis_title_cn = '能耗 (kWh/天)'
    yaxis_title_en = 'Energy (kWh/day)'

    title = title_cn if lang == 'cn' else title_en
    yaxis_title = yaxis_title_cn if lang == 'cn' else yaxis_title_en
    months = months_en  # 使用英文月份标签

    fig = go.Figure()

    # 堆叠面积图
    fig.add_trace(go.Scatter(
        x=months,
        y=led,
        name='LED照明' if lang == 'cn' else 'LED Lighting',
        mode='lines',
        fill='tonexty',
        fillcolor='rgba(66, 133, 244, 0.7)',
        line=dict(color='#4285f4', width=2),
        hovertemplate='LED: %{y} kWh/day<extra></extra>'
    ))

    fig.add_trace(go.Scatter(
        x=months,
        y=[led[i] + ac[i] for i in range(len(led))],
        name='空调' if lang == 'cn' else 'Air Conditioning',
        mode='lines',
        fill='tonexty',
        fillcolor='rgba(217, 119, 87, 0.7)',
        line=dict(color='#d97757', width=2),
        hovertemplate='AC: %{customdata} kWh/day<extra></extra>',
        customdata=[ac]
    ))

    fig.add_trace(go.Scatter(
        x=months,
        y=[led[i] + ac[i] + other[i] for i in range(len(led))],
        name='其他设备' if lang == 'cn' else 'Other Equipment',
        mode='lines',
        fill='tonexty',
        fillcolor='rgba(232, 230, 220, 0.9)',
        line=dict(color='#e8e6dc', width=2),
        hovertemplate='Total: %{y} kWh/day<extra></extra>'
    ))

    # 标注关键数值
    annotations = []
    if lang == 'cn':
        annotations.append(dict(x='Jul', y=48, text='夏季峰值<br>>45 kWh/天',
                               showarrow=True, arrowhead=2, arrowsize=1, arrowcolor=COLORS['accent']))
        annotations.append(dict(x='Jan', y=24, text='冬季典型<br>~20 kWh/天',
                               showarrow=True, arrowhead=2, arrowsize=1, arrowcolor=COLORS['data_blue']))
    else:
        annotations.append(dict(x='Jul', y=48, text='Summer Peak<br>>45 kWh/day',
                               showarrow=True, arrowhead=2, arrowsize=1, arrowcolor=COLORS['accent']))
        annotations.append(dict(x='Jan', y=24, text='Winter Typical<br>~20 kWh/day',
                               showarrow=True, arrowhead=2, arrowsize=1, arrowcolor=COLORS['data_blue']))

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
        xaxis=dict(
            showgrid=False,
            tickfont=dict(size=14),
            title=dict(text='')
        ),
        yaxis=dict(
            title=dict(text=yaxis_title, font=dict(size=14)),
            range=[0, 55],
            gridcolor=COLORS['grid'],
            linewidth=2,
            linecolor=COLORS['primary_text'],
            tickfont=dict(size=12),
            showgrid=True
        ),
        annotations=annotations,
        hovermode='x unified'
    )

    return fig


if __name__ == '__main__':
    fig_cn = create_fig3_energy_seasonality('cn')
    fig_en = create_fig3_energy_seasonality('en')

    # HTML first (always works)
    fig_cn.write_html('fig3_energy_seasonality_cn.html')
    fig_en.write_html('fig3_energy_seasonality_en.html')
    print('HTML generated')

    # PNG (requires kaleido, may fail on some systems)
    try:
        fig_cn.write_image('fig3_energy_seasonality_cn.png', width=1200, height=600, scale=2)
        fig_en.write_image('fig3_energy_seasonality_en.png', width=1200, height=600, scale=2)
        print('PNG generated')
    except Exception as e:
        print(f'PNG export skipped: {e}')

    print('Fig3 complete')
