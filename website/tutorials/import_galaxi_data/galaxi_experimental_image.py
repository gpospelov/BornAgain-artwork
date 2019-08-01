"""
Shows experimental image for blender
"""

import matplotlib
from matplotlib import pyplot as plt
import math
import random
import numpy
import bornagain as ba
from SampleBuilder import MySampleBuilder

wavelength = 1.34*ba.angstrom
alpha_i = 0.46*ba.degree



def plot_as_colormap(hist, zmin=None, zmax=None):
    """
    Simple plot of intensity data as color map
    """
    if not zmin:
        zmin = 1.0

    if not zmax:
        zmax = hist.getMaximum()

    im = plt.imshow(hist.getArray(),
                    norm=matplotlib.colors.LogNorm(zmin, zmax),
                    extent=[hist.getXmin(), hist.getXmax(), hist.getYmin(), hist.getYmax()],
                    aspect='auto')
    # cb = plt.colorbar(im, pad = 0.025)
    # plt.xlabel(r'$\phi_f ^{\circ}$', fontsize=16)
    # plt.ylabel(r'$\alpha_f ^{\circ}$', fontsize=16)



def create_detector():
    """
    Creates and returns GALAXY detector
    """
    # detector setup as given from instrument responsible
    npx, npy = 981, 1043
    pixel_size = 0.172  # in mm
    detector_distance = 1730.0  # in mm
    beam_xpos, beam_ypos = 597.1, 323.4  # in pixels

    u0 = beam_xpos*pixel_size  # in mm
    v0 = beam_ypos*pixel_size  # in mm
    detector = ba.RectangularDetector(npx, npx*pixel_size, npy, npy*pixel_size)
    detector.setPerpendicularToDirectBeam(detector_distance, u0, v0)
    return detector


def create_simulation():
    """
    Creates and returns GISAS simulation with beam and detector defined
    """
    simulation = ba.GISASSimulation()
    simulation.setDetector(create_detector())
    simulation.setBeamParameters(wavelength, alpha_i, 0.0)
    simulation.setBeamIntensity(1e9)
    return simulation


def load_real_data(hist, filename="/home/pospelov/development/BornAgain/BornAgain/Examples/python/fitting/ex10_FitGALAXIData/galaxi_data.tif.gz"):
    """
    Fill histogram representing our detector with intensity data from tif file.
    Returns cropped version of it, which represent the area we are interested in.
    """
    #hist.load(filename)
    return ba.IntensityDataIOFactory.readIntensityData(filename)


def make_image():
    simulation = create_simulation()
    sample_builder = MySampleBuilder()
    simulation.setSampleBuilder(sample_builder)

    real_data = load_real_data(simulation.getIntensityData())

    matplotlib.rc('xtick', labelsize=20)
    matplotlib.rc('ytick', labelsize=20)
    fig = plt.figure(figsize=(14.0, 16.0), facecolor='#EFEFEF')
    plot_as_colormap(real_data)
    plt.tight_layout()
    # plt.savefig('galaxi_experimental_image.png', facecolor=fig.get_facecolor(), transparent=True, edgecolor='none')
    plt.savefig('galaxi_experimental_image.png', facecolor=fig.get_facecolor())
    plt.subplots_adjust(left=0.055)
    plt.show()

if __name__ == '__main__':
    make_image()
