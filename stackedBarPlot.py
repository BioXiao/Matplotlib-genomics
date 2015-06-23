#This is a useful stacked barPlot example using matplotlib
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')
data = pd.read_csv("AS_significant_Events_all_summary_for_plotting.csv")
x= range(7)
wid = 0.5
as_type = ['SE','MXE','A5SS','A3SS','RT']
title = ['SHhESC2_Total_AS_Events','SHhESC8_Total_AS_Events','SHhESC2_Sig_AS_Events','SHhESC8_Sig_AS_Events']
with plt.xkcd():
    fig = plt.figure(figsize=(12,12))
    for i in range(4):
        n = i*7
        m = i*7 +6
        sample = sig_events.ix[n:m,'Time'].values
        se = data.ix[n:m,'SE']
        mxe = data.ix[n:m,'MXE']
        a5ss = data.ix[n:m,'A5SS']
        a3ss = data.ix[n:m,'A3SS']
        ri = data.ix[n:m,'RI']
    
        
        ax = fig.add_subplot(2,2,i+1)
        ax.bar(x,se,width = wid,color='#FF403A',label='SE',align="center")
        ax.bar(x,mxe,width = wid, color='#7CC8EC', bottom= se,label='MXE',align="center")
        ax.bar(x,a5ss,width = wid, color='#FF8D93', bottom= se+mxe , label='A5SS',align="center")
        ax.bar(x,a3ss,width = wid, color='#759FE8', bottom= se+mxe+a5ss,label='A3SS',align="center")
        ax.bar(x,ri,width = wid, color='#ADFF80', bottom= se+mxe+a5ss+a3ss, label='RI',align="center" )
        ax.set_xticklabels([' ','D0_VS_D5N','D5N_VS_D10N','D10N_VS_D20R',
                            'D20R_VS_D25','D0_VS_D25', 'D5N_VS_D5','D10N_VS_D10',' '],
                            rotation=90)
        ax.tick_params(top='off',right='off',bottom='off')
        ax.set_title(title[i])
        ax.legend(loc='best',fontsize = 'x-small')
    fig.tight_layout()
    fig.savefig("AS_significant_Events_all_summary.pdf")
    fig.show()
