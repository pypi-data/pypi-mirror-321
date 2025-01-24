import logging
import numpy as np
import matplotlib
# matplotlib.use("TkAgg")

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, pathpatch_2d_to_3d

from craterslab.ellipse import EllipseVisualConfig, EllipticalModel
from craterslab.profiles import Profile
from craterslab.sensors import DepthMap


def plot_3D(
    dm: DepthMap,
    profile: Profile | None = None,
    ellipse: EllipticalModel | None = None,
    title: str = "Crater view in 3D",
    preview_scale: tuple[float, float, float] = (1.0, 1.0, 1.0),
    block: bool = False,
    ellipse_config: EllipseVisualConfig | None = None,
) -> None:
    """
    Create a 3D plot of the surface considering the sensor resolution.
    Preview scale can be passed to enlarge or shrink specific dimensions
    in order to create the desired visual effect.
    """

    x = np.linspace(0, dm.x_count * dm.x_res, dm.x_count)
    y = np.linspace(0, dm.y_count * dm.y_res, dm.y_count)

    X, Y = np.meshgrid(x, y)
    Z = dm.map * dm.z_res

    # Set up the plot
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    surface = ax.plot_surface(X, Y, Z, cmap="viridis")

    # Preserve aspect ratio
    aspect = [
        preview_scale[0] * np.ptp(X),
        preview_scale[1] * np.ptp(Y),
        preview_scale[2] * np.ptp(Z),
    ]
    ax.set_box_aspect(aspect)

    if ellipse is not None:
        visual_config = ellipse_config if ellipse_config is not None else ellipse.visual
        p = ellipse.ellipse_patch(scale=dm.x_res, visual_config=ellipse_config)
        ax.add_patch(p)
        pathpatch_2d_to_3d(p, z=visual_config.z_val, zdir="z")

    # Plot the profile if any
    if profile is not None:
        x1, x2 = profile.x_bounds
        y1, y2 = profile.y_bounds
        z1, z2 = profile.z_bounds
        dz = 0.25 * abs(z2 - z1)
        z1p, z2p = z1 - dz, z2 + dz
        points = [
            (x1, y1, z1p),
            (x1, y1, z2p),
            (x2, y2, z2p),
            (x2, y2, z1p),
        ]
        ax.add_collection3d(
            Poly3DCollection([points], facecolors="tab:brown", alpha=0.6)
        )

    ax.set_xlabel(
        f"X[{dm.sensor.scale}]",
        fontweight="bold",
        fontsize=15,
        labelpad=10,
        loc="center",
    )
    ax.set_ylabel(
        f"Y[{dm.sensor.scale}]",
        fontweight="bold",
        fontsize=15,
        labelpad=10,
        rotation=90,
        loc="center",
    )
    ax.set_zlabel(f"Z[{dm.sensor.scale}]", fontweight="bold", fontsize=15, labelpad=10)
    ax.tick_params(axis="x", labelsize=15)
    ax.tick_params(axis="y", labelsize=15)
    ax.tick_params(axis="z", labelsize=15)
    plt.title(title)
    cbar = plt.colorbar(surface, shrink=0.7, aspect=13, orientation="vertical")
    cbar.ax.tick_params(labelsize=15)
    plt.show(block=block)


def plot_2D(
    dm: DepthMap,
    profile: Profile | None = None,
    ellipse: EllipticalModel | None = None,
    title: str = "Crater view in 2D",
    block: bool = False,
) -> None:
    """
    Create a 2D plot of the surface
    """
    fig, ax = plt.subplots()
    ax.imshow(dm.map)
    ax.set_xlabel("X [px]", fontweight="bold", fontsize=15)
    ax.set_ylabel("Y [px]", fontweight="bold", fontsize=15)
    ax.set_title(title, fontweight="bold")
    ax.set_xlim(0, dm.x_count)
    ax.set_ylim(0, dm.y_count)

    ax.tick_params(axis="x", labelsize=15)
    ax.tick_params(axis="y", labelsize=15)

    if profile is not None:
        ax.plot(profile.x_bounds_px, profile.y_bounds_px, "ro-")

    if ellipse is not None:
        ax.add_patch(ellipse.ellipse_patch())
        ax.scatter(*list(zip(*ellipse.landmarks)))
    plt.show(block=block)


def plot_profile(profile: Profile, draw_slopes: bool = False, block: bool = False) -> None:
    """
    Create a profile plot
    """
    fig, ax = plt.subplots()  # create figure and axes
    ax.plot(profile.s, profile.h)
    ax.set_ylabel(
        f"Depth ({profile.dm.sensor.scale})",
        labelpad=13,
        fontsize=20,
    )
    ax.set_xlabel(
        f"Distance along the segment ({profile.dm.sensor.scale})",
        labelpad=13,
        fontsize=20,
    )
    ax.tick_params(axis="x", labelsize=20)
    ax.tick_params(axis="y", labelsize=20)

    if draw_slopes:
        key_indices = [profile.t1, profile.t2, profile.b1, profile.b2]
        if all(key_indices):
            profile.slopes()
            selected_indices = np.array(key_indices)
            ax.scatter(profile.s[selected_indices], profile.h[selected_indices])
            for i, line in enumerate([profile.l1, profile.l2]):
                line_model = np.poly1d(line)
                i0, i1 = (profile.t1, profile.b1) if i == 0 else (profile.t2, profile.b2)
                x_bounds, z_bounds = slope_bounds(profile, line_model, i0, i1)
                ax.plot(x_bounds, z_bounds, color="blue", linestyle="--")
        else:
            logging.error("Attempt to draw profile slopes failed."
                          "Make sure you are using the depth map from a crater")
    ax.grid()
    plt.show(block=block)


def slope_bounds(profile: Profile, line_model: np.poly1d, index_0: int, index_1: int) -> tuple[tuple[float,float], tuple[float,float]]:
    x = [profile.s[index_0], profile.s[index_1]]
    if line_model:
        z = [line_model(v) for v in x]
    else:
        z = x
        logging.error("Slopes are invalid")
    return x, z