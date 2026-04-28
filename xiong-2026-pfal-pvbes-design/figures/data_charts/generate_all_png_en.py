"""
English versions of 5 data figures for VFED paper blog
Same layout as Chinese version, English text
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

C = {'bg':'#ffffff','primary':'#000000','accent':'#d85117','blue':'#24719e','grid':(0,0,0,0.1),'green':'#487980','gray':'#7f7f7f'}
FT=22; FD=17; FLB=18; FTK=16; FAN=13
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
    fig.savefig(name+'_.svg', bbox_inches='tight', transparent=True, dpi=300)
    fig.savefig(name+'_.png', bbox_inches='tight', facecolor=C['bg'], dpi=200)
    print(f'  {name}_ OK')

# Fig2 EN
fig=plt.figure(figsize=(FW,FH))
ct=make_desc_ax(fig,'Why These Five Cities?',
    'These five cities represent China\'s five major climate zones.\nLhasa (left): strongest sun (~5.9) and cool; Harbin (right): weakest sun (~3.8) and cold.', lines=2)
ax1=chart_ax(fig,ct)
c=['Lhasa\n(Plateau)','Haikou\n(Tropical)','Shanghai\n(Subtropical)','Urumqi\n(Continental)','Harbin\n(Frigid)']
solar=[5.88,4.72,4.25,4.21,3.81]
temp=[8.0,25.5,16.5,7.5,5.7]
x=np.arange(5); w=0.35
ax1.bar(x,solar,w,color=C['blue'],alpha=0.85,label='Annual Solar Radiation')
ax1.set_ylabel('Solar Radiation (kWh/m\u00b2/day)',fontsize=FLB-2,color=C['blue']); ax1.set_ylim(0,7.5)
ax1.set_xticks(x); ax1.set_xticklabels(c,fontsize=FTK-2)
ax1.tick_params(axis='y',labelsize=FTK-1,labelcolor=C['blue'])
ax2=ax1.twinx()
ax2.plot(x,temp,'s-',color=C['accent'],linewidth=3,markersize=14,label='Annual Mean Temp.')
ax2.set_ylim(0,30); ax2.set_ylabel('Temperature (°C)',fontsize=FLB-2,color=C['accent'])
ax2.tick_params(axis='y',labelsize=FTK-1,labelcolor=C['accent'])
for i,v in enumerate(temp): ax2.annotate(f'{v}°C',xy=(i,v),xytext=(0,12),textcoords='offset points',ha='center',fontsize=FAN+1,color=C['accent'],fontweight='bold')
l1,la1=ax1.get_legend_handles_labels(); l2,la2=ax2.get_legend_handles_labels()
ax1.legend(l1+l2,la1+la2,loc='upper left',fontsize=FAN-1,framealpha=0.9)
save(fig,'fig2_5cities_climate_en'); plt.close()

# Fig3 EN
fig=plt.figure(figsize=(FW,FH))
ct=make_desc_ax(fig,'Winter vs. Summer: Where Does the Electricity Go?',
    'We collected full-year 2024 energy data from a 20ft container plant factory.\nIn winter, LED lighting dominates; in summer, air conditioning takes over.', lines=2)
a1=fig.add_axes([0.10,0.06,0.38,ct-0.06],facecolor=C['bg'])
a2=fig.add_axes([0.52,0.06,0.38,ct-0.06],facecolor=C['bg'])
a1.pie([13,3,4],explode=(.04,.04,.04),colors=[C['blue'],C['accent'],C['grid']],labels=['LED Lighting\n(~13 kWh/day)','AC\n(~3 kWh/day)','Fans/Other\n(~4 kWh/day)'],autopct='%1.0f%%',startangle=90,textprops={'fontsize':FAN-2})
a1.set_title('Winter Typical Day\n(~20 kWh total)',fontsize=FT-7,fontweight='bold',color=C['blue'],pad=2)
a2.pie([18,25,5],explode=(.04,.04,.04),colors=[C['blue'],C['accent'],C['grid']],labels=['LED Lighting\n(~18 kWh/day)','AC\n(~25 kWh/day)','Fans/Other\n(~5 kWh/day)'],autopct='%1.0f%%',startangle=90,textprops={'fontsize':FAN-2})
a2.set_title('Summer Typical Day\n(~48 kWh total)',fontsize=FT-7,fontweight='bold',color=C['accent'],pad=2)
save(fig,'fig3_energy_seasonality_en'); plt.close()

# Fig4 EN
fig=plt.figure(figsize=(FW,FH*1.05))
ct=make_desc_ax(fig,'What Time to Turn On the Lights? 40% Battery Saving!',
    'To achieve energy self-sufficiency, simply shifting the photoperiod to early morning\ncan dramatically cut battery storage needs by 40%.', lines=2)
ax=chart_ax(fig,ct)
hr=np.arange(24)
sd=np.array([75,70,60,52,50,55,62,68,72,76,78,80,82,85,87,88,88,87,85,82,78,75,72,73])
ax.fill_between(hr,sd,alpha=0.12,color=C['blue']); ax.plot(hr,sd,'o-',color=C['blue'],linewidth=3,markersize=7)
ax.axvspan(2,5,alpha=0.08,color=C['green']); ax.axvspan(13,17,alpha=0.08,color=C['accent'])
ax.text(3.5,91,'Early Morning On\nOptimal Zone',fontsize=FAN,color=C['green'],ha='center',va='center',fontweight='bold',bbox=dict(boxstyle='round,pad=0.3',facecolor='white',edgecolor=C['green'],lw=1.5,alpha=0.9))
ax.text(15,91,'Afternoon On\nHigh-Demand Zone',fontsize=FAN,color=C['accent'],ha='center',va='center',fontweight='bold',bbox=dict(boxstyle='round,pad=0.3',facecolor='white',edgecolor=C['accent'],lw=1.5,alpha=0.9))
ax.annotate('Optimal:\n4 AM start\n~50 kWh',xy=(4,50),xytext=(6.5,43),fontsize=FAN,color=C['green'],fontweight='bold',ha='left',arrowprops=dict(arrowstyle='->',color=C['green'],lw=2,connectionstyle='arc3,rad=0.3'),bbox=dict(boxstyle='round,pad=0.4',facecolor='white',edgecolor=C['green'],lw=1.5))
ax.annotate('Battery\nRequirement\nReduced by\n~40%',xy=(0.82,0.28),xycoords='axes fraction',fontsize=FAN+8,color=C['accent'],fontweight='bold',ha='center',va='center',bbox=dict(boxstyle='round,pad=0.7',facecolor='white',edgecolor=C['accent'],lw=3))
ax.set_xlabel('Photoperiod Start Time (hour of day)',fontsize=FLB-2); ax.set_ylabel('Battery Storage (kWh)',fontsize=FLB-2)
ax.set_xlim(-0.5,23.5); ax.set_ylim(40,100)
ax.set_xticks([0,2,4,6,8,10,12,14,16,18,20,22])
ax.set_xticklabels(['0:00','2:00','4:00','6:00','8:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00'],fontsize=FTK-2)
ax.tick_params(axis='y',labelsize=FTK)
gp=mpatches.Patch(color=C['green'],alpha=0.25,label='2-5 AM (Optimal)')
op=mpatches.Patch(color=C['accent'],alpha=0.25,label='1-5 PM (High Demand)')
ax.legend(handles=[gp,op],loc='center left',fontsize=FAN-1,framealpha=0.9)
save(fig,'fig4_photoperiod_storage_en'); plt.close()

# Fig5 EN
fig=plt.figure(figsize=(FW*1.05,FH))
ct=make_desc_ax(fig,'From Lhasa to Harbin: 3\u00d7 Hardware Cost Difference?',
    'For energy self-sufficiency: Lhasa (strong sun, cool) needs only 40 m\u00b2 PV + 40 kWh battery;\nHarbin (weak sun, extreme temperatures) requires 120 m\u00b2. A 3-fold difference between the best and worst locations.', lines=2)
ax=chart_ax(fig,ct)
c=['Lhasa\nPlateau·Best Sun\n5.88 kWh/m\u00b2','Haikou\nTropical·Good Sun\n4.72 kWh/m\u00b2','Shanghai\nSubtropical·Baseline\n4.25 kWh/m\u00b2','Urumqi\nContinental·Short Winter\n4.21 kWh/m\u00b2','Harbin\nFrigid·Least Sun\n3.81 kWh/m\u00b2']
pv_a=[40,50,80,110,120]; st=[40,45,50,45,50]; x=np.arange(5); w=0.3
ax.bar(x-w/2,pv_a,w,color=C['blue'],alpha=0.85,label='PV Area (m\u00b2)')
ax.bar(x+w/2,st,w,color=C['accent'],alpha=0.85,label='Battery Capacity (kWh)')
for i,(pv,s) in enumerate(zip(pv_a,st)):
    ax.annotate(f'{pv}',xy=(i-w/2,pv),xytext=(0,5),textcoords='offset points',ha='center',fontsize=FAN+1,color=C['blue'],fontweight='bold')
    ax.annotate(f'{s}',xy=(i+w/2,s),xytext=(0,5),textcoords='offset points',ha='center',fontsize=FAN+1,color=C['accent'],fontweight='bold')
ax.set_ylabel('Configuration Size',fontsize=FLB-2); ax.set_xticks(x); ax.set_xticklabels(c,fontsize=FTK-3); ax.set_ylim(0,160)
ax.legend(loc='upper left',fontsize=FAN-1,framealpha=0.9)
ax.tick_params(axis='y',labelsize=FTK-1)
save(fig,'fig5_5cities_config_en'); plt.close()

# Fig6 EN — USD prices
fig=plt.figure(figsize=(FW*0.9,FH))
ct=make_desc_ax(fig,'How Much Does Self-Generated PV+Storage Electricity Cost?',
    'At a fixed assumed rate of ~$0.096/kWh, after optimal PV-storage system design,\nself-generated power costs ~$0.036/kWh — over 60% cheaper than the grid.', lines=2)
ax=chart_ax(fig,ct)
lb=['Grid Purchase\n(Reference Rate)','PV+Storage\n3-Year Payback','PV+Storage\n5-Year Payback']
lr=[0.096,0.038,0.036]; bc=[C['gray'],C['blue'],C['green']]
ax.bar(lb,lr,color=bc,width=0.5)
for i,v in enumerate(lr): ax.annotate(f'${v:.3f}/kWh',xy=(i,v),xytext=(0,8),textcoords='offset points',ha='center',fontsize=FAN+3,fontweight='bold',color=bc[i])
ax.text(1,0.06,'~60%\nCheaper',fontsize=FAN+1,color=C['blue'],fontweight='bold',ha='center',bbox=dict(boxstyle='round,pad=0.3',facecolor='white',edgecolor=C['blue'],alpha=0.85))
ax.text(2,0.058,'~63%\nCheaper',fontsize=FAN+1,color=C['green'],fontweight='bold',ha='center',bbox=dict(boxstyle='round,pad=0.3',facecolor='white',edgecolor=C['green'],alpha=0.85))
ax.set_ylabel('Cost per kWh ($)',fontsize=FLB-2); ax.set_ylim(0,0.13)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x,_:f'${x:.3f}'))
ax.tick_params(axis='y',labelsize=FTK-1)
save(fig,'fig6_lcoe_comparison_en'); plt.close()

print('=== English versions done ===')
