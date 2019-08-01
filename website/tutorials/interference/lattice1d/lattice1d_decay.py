from matplotlib import pyplot as plt
import numpy as np

xmin, xmax = -8.0, 8.0
ymin, ymax = -1.0, 5.0
xoff, yoff = 2.0, 1.0
decay_length = 4.0
peak_count = 7

def plot_bar(ax, xpos, height, width):
    ax.plot([xpos, xpos], [0.0, height], lw=width, color='tab:blue', solid_joinstyle='miter', solid_capstyle='round')
    ax.plot(xpos, 0.0, 'o', color='tab:orange', markersize=15)


def decay_value(x, height):
    xx = np.abs(x)
    return height*np.exp(-xx/decay_length)


def cauchy_value(q):
    x_decay_length=5.0
    sum_sq = q * q * x_decay_length * x_decay_length
    return decay_length * 2.0 / (1.0 + sum_sq)


def plot_decay():
    x1, x2 = xmin + xoff/2, xmax-xoff/2
    point_count = 200
    xp = list()
    yp = list()
    for i in range(point_count):
        x = x1 + i *(x2-x1)/(point_count-1)
        xp.append(x)
        yp.append(decay_value(x, 3.5))
    plt.plot(xp, yp)


def plot_cauchy(ax, xpos, height):
    x1, x2 = -0.5, 0.5
    point_count = 100
    xp = list()
    yp = list()
    for i in range(point_count):
        x = x1 + i *(x2-x1)/(point_count-1)
        xp.append(xpos+x)
        yp.append(-0.46+0.4*cauchy_value(x))
    plt.plot(xp, yp, color='tab:blue')



def plot_lattice():
    ratio = (xmax-xmin)/(ymax-ymin)
    fig, ax = plt.subplots(figsize=(6*ratio, 6))
    fig.tight_layout()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.axis('off')
    x1, x2 = xmin + xoff, xmax-xoff
    for i in range(peak_count):
        xpos = x1 + i *(x2-x1)/(peak_count-1)
        plot_bar(ax, xpos, height=decay_value(xpos, 3.5), width=8)

    # horizontal axes
    ax.arrow(xmin+xoff*0.5, 0.0, xmax-xmin-xoff, 0.0, color='tab:gray', head_width=0.2, head_length=0.4, fc='k', ec='k', zorder=2)
    # vertical axes
    ax.arrow(0.0, ymin+yoff/2, 0.0, 5.0, color='tab:gray', head_width=0.15, head_length=0.3, fc='k', ec='k', zorder=2)
    ax.text(6.8, -0.5, r'$x$', fontsize=25)
    plot_decay()
    # vertical dotted
    ax.plot([5.0, 5.0], [ -0.5, 2.0], 'k--', lw=1, color='tab:grey', solid_joinstyle='miter', solid_capstyle='round')
    # lambda and arrow
    ax.text(5.25, 1.75, r'$\lambda$', fontsize=25)
    ax.arrow(4.25, 1.75, 0.5, 0.0, color='tab:grey', head_width=0.1, head_length=0.15, fc='k', ec='k', zorder=2)
    # text: a, 2d
    ax.text(1.85, -0.45, r'$a$', fontsize=20)
    ax.text(3.85, -0.45, r'$2a$', fontsize=20)
    ax.text(0.25, 4.0, r'P(x)', fontsize=20)
    plt.savefig("lattice1d_decay_real.png")


def plot_reciprocal():
    ratio = (xmax-xmin)/(ymax-ymin)
    fig, ax = plt.subplots(figsize=(6*ratio, 6))
    fig.tight_layout()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.axis('off')
    x1, x2 = xmin + xoff, xmax-xoff
    for i in range(peak_count):
        xpos = x1 + i *(x2-x1)/(peak_count-1)
        plot_bar(ax, xpos, 3.5, width=1.0)
        plot_cauchy(ax, xpos, 3.5)

    # horizontal axes
    ax.arrow(xmin+xoff*0.5, 0.0, xmax-xmin-xoff, 0.0, color='tab:gray', head_width=0.2, head_length=0.4, fc='k', ec='k', zorder=2)
    # vertical axes
    # ax.arrow(0.0, ymin+yoff/2, 0.0, 5.0, color='tab:gray', head_width=0.15, head_length=0.3, fc='k', ec='k', zorder=2)
    ax.text(6.8, -0.5, r'$q_x$', fontsize=25)
    ax.text(0.25, 1.30, r'$\sim\lambda^{-1}$', fontsize=25)
    # ax.arrow(-0.25, 1.2, 0.5, 0.0, color='tab:gray', head_width=0.05, head_length=0.05, fc='k', ec='k', zorder=2)
    ax.plot([-0.25, 0.25], [ 1.0, 1.0], 'k--', lw=2, color='tab:grey', solid_joinstyle='miter', solid_capstyle='round')
    plt.savefig("lattice1d_decay_reciprocal.png")


if __name__ == '__main__':
    plot_lattice()
    plot_reciprocal()
    plt.show()
