"""
v24 - 统一中文单位: 千瓦时/平米/千瓦
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

C = {'bg':'#ffffff','primary':'#000000','accent':'#d85117','blue':'#24719e','grid':(0,0,0,0.1),'green':'#487980','gray':'#7f7f7f'}
FT=22; FD=18; FLB=20; FTK=18; FAN=14
FW=12; FH=7; RMB=7.2
DESC_Y=0.89; GAP=0.04

def make_desc_ax(fig, title, desc, lines):
    fig.patch.set_facecolor(C['bg'])
    fig.suptitle(title, fontsize=FT, fontweight='bold', color=C['primary'], x=0.5, y=0.97, va='top')
    desc_h = 0.05 + lines * 0.04
    chart_top = DESC_Y - GAP - desc_h
    da = fig.add_axes([0.12, DESC_Y - desc_h, 0.75, desc_h])
    da.set_xticks([]); da.set_yticks([])
    for s in da.spines.values(): s.set_visible(False)
    da.text(0.5, 0.5, desc, transform=da.transAxes, fontsize=FD, color='#555', ha='center', va='center')
    return chart_top

def chart_ax(fig, top):
    return fig.add_axes([0.12, 0.06, 0.75, top-0.06], facecolor=C['bg'])

def save(fig, name):
    fig.savefig(name+'.svg', bbox_inches='tight', transparent=True, dpi=300)
    fig.savefig(name+'.png', bbox_inches='tight', facecolor=C['bg'], dpi=200)
    print(f'  {name} OK')

# Fig2 — 五城市气候差异（光照+温度双轴）
fig=plt.figure(figsize=(FW,FH))
ct=make_desc_ax(fig,'为什么选了这五座城市？',
    '这五座城市代表了中国五种典型气候区，日照和温度较为具备代表性。\n看最左和最右：拉萨日照最强(~5.9)又凉爽(~8°C)；哈尔滨日照最弱(~3.8)又寒冷(~6°C)。', lines=2)
ax1=chart_ax(fig,ct)
c=['拉萨\n(高原气候)','海口\n(热带气候)','上海\n(亚热带气候)','乌鲁木齐\n(温带大陆气候)','哈尔滨\n(严寒气候)']
solar=[5.88,4.72,4.25,4.21,3.81]
temp=[8.0,25.5,16.5,7.5,5.7]
x=np.arange(5); w=0.35
ax1.bar(x,solar,w,color=C['blue'],alpha=0.85,label='年均太阳辐射')
ax1.set_ylabel('年均太阳辐射 (千瓦时/平米/天)',fontsize=FLB-2,color=C['blue']); ax1.set_ylim(0,7.5)
ax1.set_xticks(x); ax1.set_xticklabels(c,fontsize=FTK-2)
ax1.tick_params(axis='y',labelsize=FTK-1,labelcolor=C['blue'])
ax2=ax1.twinx()
ax2.plot(x,temp,'s-',color=C['accent'],linewidth=3,markersize=14,label='年均气温')
ax2.set_ylim(0,30); ax2.set_ylabel('年均气温 (°C)',fontsize=FLB-2,color=C['accent'])
ax2.tick_params(axis='y',labelsize=FTK-1,labelcolor=C['accent'])
for i,v in enumerate(temp): ax2.annotate(f'{v}°C',xy=(i,v),xytext=(0,12),textcoords='offset points',ha='center',fontsize=FAN+1,color=C['accent'],fontweight='bold')
l1,la1=ax1.get_legend_handles_labels(); l2,la2=ax2.get_legend_handles_labels()
ax1.legend(l1+l2,la1+la2,loc='upper left',fontsize=FAN-1,framealpha=0.9)
save(fig,'fig2_5cities_climate_cn'); plt.close()

# Fig3
fig=plt.figure(figsize=(FW,FH))
ct=make_desc_ax(fig,'植物工厂冬天用电和夏天有什么不同？',
    '我们采集了一座20尺集装箱植物工厂在2024年全年的能耗数据。\n可以看到冬天LED灯是主力，夏天一到空调就反超成了最大的耗电项。', lines=2)
a1=fig.add_axes([0.10,0.06,0.38,ct-0.06],facecolor=C['bg'])
a2=fig.add_axes([0.52,0.06,0.38,ct-0.06],facecolor=C['bg'])
a1.pie([13,3,4],explode=(.04,.04,.04),colors=[C['blue'],C['accent'],C['grid']],labels=['LED照明\n(~13千瓦时/天)','空调\n(~3千瓦时/天)','风机/其他\n(~4千瓦时/天)'],autopct='%1.0f%%',startangle=90,textprops={'fontsize':FAN-1})
a1.set_title('冬季典型日 (共约20千瓦时)',fontsize=FT-4,fontweight='bold',color=C['blue'],pad=5)
a2.pie([18,25,5],explode=(.04,.04,.04),colors=[C['blue'],C['accent'],C['grid']],labels=['LED照明\n(~18千瓦时/天)','空调\n(~25千瓦时/天)','风机/其他\n(~5千瓦时/天)'],autopct='%1.0f%%',startangle=90,textprops={'fontsize':FAN-1})
a2.set_title('夏季典型日 (共约48千瓦时)',fontsize=FT-4,fontweight='bold',color=C['accent'],pad=5)
save(fig,'fig3_energy_seasonality_cn'); plt.close()

# Fig4
fig=plt.figure(figsize=(FW,FH*1.05))
ct=make_desc_ax(fig,'几点开灯最省电池？差40%！',
    '为了能实现能源自主，单凭将光周期开灯时间调为凌晨，\n就可以大幅减少储能系统的容量需求（40%）。', lines=2)
ax=chart_ax(fig,ct)
hr=np.arange(24)
sd=np.array([75,70,60,52,50,55,62,68,72,76,78,80,82,85,87,88,88,87,85,82,78,75,72,73])
ax.fill_between(hr,sd,alpha=0.12,color=C['blue']); ax.plot(hr,sd,'o-',color=C['blue'],linewidth=3,markersize=7)
ax.axvspan(2,5,alpha=0.08,color=C['green']); ax.axvspan(13,17,alpha=0.08,color=C['accent'])
ax.text(3.5,91,'凌晨开灯→储能少\n最优区间',fontsize=FAN,color=C['green'],ha='center',va='center',fontweight='bold',bbox=dict(boxstyle='round,pad=0.3',facecolor='white',edgecolor=C['green'],lw=1.5,alpha=0.9))
ax.text(15,91,'下午开灯→储能多\n高配区间',fontsize=FAN,color=C['accent'],ha='center',va='center',fontweight='bold',bbox=dict(boxstyle='round,pad=0.3',facecolor='white',edgecolor=C['accent'],lw=1.5,alpha=0.9))
ax.annotate('● 最优点\n  凌晨4点\n  仅需50千瓦时',xy=(4,50),xytext=(6.5,43),fontsize=FAN,color=C['green'],fontweight='bold',ha='left',arrowprops=dict(arrowstyle='->',color=C['green'],lw=2,connectionstyle='arc3,rad=0.3'),bbox=dict(boxstyle='round,pad=0.4',facecolor='white',edgecolor=C['green'],lw=1.5))
ax.annotate('电池需求\n可减少\n约40%',xy=(0.82,0.28),xycoords='axes fraction',fontsize=FAN+8,color=C['accent'],fontweight='bold',ha='center',va='center',bbox=dict(boxstyle='round,pad=0.7',facecolor='white',edgecolor=C['accent'],lw=3))
ax.set_xlabel('光周期起始时刻',fontsize=FLB-2); ax.set_ylabel('储能 (千瓦时)',fontsize=FLB-2)
ax.set_xlim(-0.5,23.5); ax.set_ylim(40,100)
ax.set_xticks([0,2,4,6,8,10,12,14,16,18,20,22])
ax.set_xticklabels(['0:00','2:00','4:00','6:00','8:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00'],fontsize=FTK-2)
ax.tick_params(axis='y',labelsize=FTK)
gp=mpatches.Patch(color=C['green'],alpha=0.25,label='凌晨2-5点（最优）')
op=mpatches.Patch(color=C['accent'],alpha=0.25,label='下午1-5点（高位）')
ax.legend(handles=[gp,op],loc='center left',fontsize=FAN-1,framealpha=0.9)
save(fig,'fig4_photoperiod_storage_cn'); plt.close()

# Fig5
fig=plt.figure(figsize=(FW*1.05,FH))
ct=make_desc_ax(fig,'从拉萨到哈尔滨，同一个植物工厂的硬件成本差3倍？',
    '为了能实现能源自主，拉萨因为日照好，气候凉爽40平米光伏+40千瓦时电池就可以；\n哈尔滨日照弱，冬冷夏热所以得装120平米；等于日照最好和最弱的地方光伏需求可以差3倍。', lines=2)
ax=chart_ax(fig,ct)
c=['拉萨\n高原·日照最好\n5.88千瓦时/平米','海口\n热带·日照较好\n4.72千瓦时/平米','上海\n亚热带·基准\n4.25千瓦时/平米','乌鲁木齐\n大陆·冬季短\n4.21千瓦时/平米','哈尔滨\n严寒·日照最少\n3.81千瓦时/平米']
pv_a=[40,50,80,110,120]; st=[40,45,50,45,50]; x=np.arange(5); w=0.3
ax.bar(x-w/2,pv_a,w,color=C['blue'],alpha=0.85,label='光伏板面积 (平米)')
ax.bar(x+w/2,st,w,color=C['accent'],alpha=0.85,label='储能电池容量 (千瓦时)')
for i,(pv,s) in enumerate(zip(pv_a,st)):
    ax.annotate(f'{pv}',xy=(i-w/2,pv),xytext=(0,5),textcoords='offset points',ha='center',fontsize=FAN+1,color=C['blue'],fontweight='bold')
    ax.annotate(f'{s}',xy=(i+w/2,s),xytext=(0,5),textcoords='offset points',ha='center',fontsize=FAN+1,color=C['accent'],fontweight='bold')
ax.set_ylabel('配置规模',fontsize=FLB-2); ax.set_xticks(x); ax.set_xticklabels(c,fontsize=FTK-3); ax.set_ylim(0,160)
ax.legend(loc='upper left',fontsize=FAN-1,framealpha=0.9)
ax.tick_params(axis='y',labelsize=FTK-1)
save(fig,'fig5_5cities_config_cn'); plt.close()

# Fig6
fig=plt.figure(figsize=(FW*0.9,FH))
ct=make_desc_ax(fig,'植物工厂自配最优光伏与储能，每千瓦时电成本多少？',
    '按固定假设电价（约0.096美元/千瓦时 ≈ 0.69元/千瓦时），光伏储能系统优化设计后，\n自发电每千瓦时约0.27元，比直接买市电便宜六成多。', lines=2)
ax=chart_ax(fig,ct)
lb=['直接从电网买电\n（固定电价参考）','配光伏+储能\n3年回本','配光伏+储能\n5年回本']
lr=[0.691,0.274,0.256]; bc=[C['gray'],C['blue'],C['green']]
ax.bar(lb,lr,color=bc,width=0.5)
for i,v in enumerate(lr): ax.annotate(f'{v:.2f}元/千瓦时',xy=(i,v),xytext=(0,8),textcoords='offset points',ha='center',fontsize=FAN+3,fontweight='bold',color=bc[i])
ax.text(1,0.44,'比电网\n便宜约60%',fontsize=FAN+1,color=C['blue'],fontweight='bold',ha='center',bbox=dict(boxstyle='round,pad=0.3',facecolor='white',edgecolor=C['blue'],alpha=0.85))
ax.text(2,0.46,'比电网\n便宜约63%',fontsize=FAN+1,color=C['green'],fontweight='bold',ha='center',bbox=dict(boxstyle='round,pad=0.3',facecolor='white',edgecolor=C['green'],alpha=0.85))
ax.set_ylabel('每千瓦时成本 (元)',fontsize=FLB-2); ax.set_ylim(0,0.88)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x,_:f'{x:.2f}元'))
ax.tick_params(axis='y',labelsize=FTK-1)
save(fig,'fig6_lcoe_comparison_cn'); plt.close()

print('=== v24 done ===')
