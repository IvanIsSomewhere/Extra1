import matplotlib.pyplot as plt
from numpy.ma.core import maximum, append

from Custom_Plots import cplot_1


def get_intensity_color(value):
    """
    Returns an RGB color tuple representing a grayscale intensity.

    Args:
        value (int/float): Intensity value (0-255). Values outside this range are clipped.

    Returns:
        tuple: RGB color (r, g, b) where all components are equal to the clipped intensity value.
    """
    intensity = max(0, min(255, value))
    return (int(intensity), int(intensity), int(intensity))


def cplot_function_3(x,y,intensity):

    # Clip intensity to [0, 255] and normalize to [0, 1] for matplotlib
    normalized_intensity = max(0, min(255, intensity)) / 255.0

    # Plot the point with grayscale color
    plt.scatter(x, y, c=[[normalized_intensity, normalized_intensity, normalized_intensity]], s=100)

    # Optional: Add grid and labels for clarity
    plt.grid(True)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(f"Point at ({x}, {y}) with Intensity {intensity}")
    plt.show()



def divide_z_value(z=None):
    if z is None:
        z = [1, 2, 3]

    _min = min(z)
    _max = max(z)

    step = (255) / (_max - _min)

    intensity = []
    for i in range(len(z)):
        intensity.append(
            ((z[i] - _min) * step)
        )
    return intensity


print(divide_z_value())

def cplot_3d(x,y,z):
    intensity = divide_z_value(z)

    cplot_function_3(x,y,z)
