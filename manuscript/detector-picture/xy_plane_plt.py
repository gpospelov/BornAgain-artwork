from matplotlib import pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec


xmin, xmax = 0.0, 200.0
ymin, ymax = 0.0, 160.0


def plot_xy():
    ratio = (xmax - xmin) / (ymax - ymin)

    fig, ax = plt.subplots(figsize=(14 * ratio, 14))
    plt.tight_layout(rect=(0.04, 0.015, 0.99, 0.99))
    fig.patch.set_facecolor('#f3f3f3')
    ax.set_facecolor('#f3f3f3')

    ax.tick_params(axis='y', labelsize=30)
    ax.tick_params(axis='x', labelsize=30)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    plt.yticks(np.linspace(ymin, ymax, 5))
    plt.xticks(np.linspace(xmin, xmax, 6))

    plt.grid(True)
    plt.savefig('xy_plane2.png', facecolor=fig.get_facecolor(), edgecolor='none')

if __name__ == '__main__':
    plot_xy()
    plt.show()

