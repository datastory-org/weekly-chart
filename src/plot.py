def ds_style(ax):
    ax.grid(axis='y', color='#e1e1e1')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['bottom'].set_linewidth(2)
    
    for tick in ax.get_xticklabels():
        tick.set_weight(500)
        tick.set_size(14)
        tick.set_color('#606062')

    for tick in ax.get_yticklabels():
        tick.set_weight(500)
        tick.set_size(14)
        tick.set_color('#606062')
        
    ax.xaxis.set_tick_params(length=8, color='#c2c2c3')
    ax.yaxis.set_tick_params(length=0)

    ax.tick_params(axis='x', which='major', pad=4)
    ax.tick_params(axis='y', which='major', pad=16)

    return ax
