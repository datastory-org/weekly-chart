import matplotlib
import matplotlib.pyplot as plt


def ds_plot(nrows=1,
            ncols=1,
            sharex=False,
            sharey=False,
            squeeze=True,
            subplot_kw=None,
            gridspec_kw=None,
            figsize=(11.52, 6.88)):

    fig, ax = plt.subplots(nrows, ncols, sharex, sharey,
                           squeeze, subplot_kw, gridspec_kw,
                           figsize=figsize)

    if type(ax) is matplotlib.axes._subplots.Subplot:
        ax.xaxis.set_tick_params(color='#c2c2c3')
    else:
        for a in ax.flat:
            a.xaxis.set_tick_params(color='#c2c2c3')
    return fig, ax
