"""Generate deterministic explanatory figures for the AQDS research note."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"

INK = "#17202A"
TEAL = "#087E8B"
ORANGE = "#D97706"
RED = "#B42318"
GREEN = "#3A7D44"
GREY = "#667085"
LIGHT = "#F4F6F8"


def save(fig: plt.Figure, name: str) -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / name, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def contact_map() -> None:
    fig, ax = plt.subplots(figsize=(15.5, 7.2))
    ax.set_xlim(0, 15.5)
    ax.set_ylim(0, 7.2)
    ax.axis("off")

    nodes = [
        (0.2, 4.35, 2.4, 1.35, "Scalar time\n" + r"$\tau=t_*-t$", INK),
        (3.1, 4.35, 2.4, 1.35, "Radial scale\n" + r"$\ell_r\asymp\tau^{1/2}$", TEAL),
        (6.0, 4.35, 2.4, 1.35, "Circle geometry\n" + r"$A=\pi\ell_r^2$", GREEN),
        (8.9, 4.35, 2.65, 1.35, "Rotational period\n" + r"$P_\theta=2\pi\ell_r/u_\theta$", ORANGE),
        (12.05, 4.35, 3.2, 1.35, "Acceleration / pressure\n" + r"$a_c=u_\theta^2/\ell_r$", RED),
    ]

    for x, y, w, h, label, color in nodes:
        box = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.03,rounding_size=0.08",
            linewidth=1.8,
            edgecolor=color,
            facecolor="white",
        )
        ax.add_patch(box)
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=11.5, color=INK)

    for start, end, color in [
        ((2.62, 5.02), (3.05, 5.02), TEAL),
        ((5.52, 5.02), (5.95, 5.02), GREEN),
        ((8.42, 5.02), (8.85, 5.02), ORANGE),
        ((11.57, 5.02), (12.0, 5.02), RED),
    ]:
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=15, color=color, linewidth=1.8))

    ax.text(7.75, 6.65, "Centre-Radius Contact Map", ha="center", va="center", fontsize=22, weight="bold", color=INK)
    ax.text(
        7.75,
        3.15,
        r"For fixed similarity position $X$:  $X=r^2/(2q)$,  $A=2\pi qX$,  and  $q\asymp\tau$",
        ha="center",
        va="center",
        fontsize=15,
        color=INK,
    )
    ax.text(
        7.75,
        2.35,
        r"Derived bridge:  $\tau\leftrightarrow r^2\leftrightarrow A\leftrightarrow P_\theta\leftrightarrow u_\theta\leftrightarrow a_c$",
        ha="center",
        va="center",
        fontsize=15,
        color=TEAL,
        weight="bold",
    )
    boundary = FancyBboxPatch(
        (1.25, 0.55), 13.0, 0.9,
        boxstyle="round,pad=0.03,rounding_size=0.08",
        linewidth=1.2,
        edgecolor=GREY,
        facecolor=LIGHT,
    )
    ax.add_patch(boundary)
    ax.text(
        7.75,
        1.0,
        "Boundary: this mapping is mathematical; it does not prove that physical time is spatial or circular.",
        ha="center",
        va="center",
        fontsize=12,
        color=INK,
    )
    save(fig, "figure-1-centre-radius-contact-map.png")


def centre_ring_geometry() -> None:
    fig, ax = plt.subplots(figsize=(8.4, 8.4))
    ax.set_aspect("equal")
    ax.set_xlim(-4.6, 4.6)
    ax.set_ylim(-4.6, 4.6)
    ax.axis("off")

    for radius, color, width in [(1.25, ORANGE, 2.6), (2.35, TEAL, 2.2), (3.45, GREEN, 2.0)]:
        ax.add_patch(Circle((0, 0), radius, fill=False, color=color, linewidth=width))

    ax.scatter([0], [0], s=75, color=RED, zorder=5)
    ax.text(0.15, -0.25, r"centre $r=0$", fontsize=12, color=RED)
    ax.add_patch(FancyArrowPatch((0.15, 0.15), (3.2, 2.0), arrowstyle="-|>", mutation_scale=16, color=INK, linewidth=1.8))
    ax.text(1.55, 1.35, r"radial coordinate $r$", fontsize=12, color=INK, rotation=31)
    ax.add_patch(FancyArrowPatch((2.6, -1.9), (1.2, -2.8), connectionstyle="arc3,rad=-0.35", arrowstyle="-|>", mutation_scale=16, color=ORANGE, linewidth=2.0))
    ax.text(2.2, -2.9, r"angular direction $\theta$", fontsize=12, color=ORANGE)
    ax.add_patch(FancyArrowPatch((3.25, 0.2), (1.45, 0.1), arrowstyle="-|>", mutation_scale=16, color=RED, linewidth=2.0))
    ax.text(2.0, 0.35, "radial inflow", fontsize=11, color=RED)
    ax.text(0, 4.15, "Spatial Centre-and-Ring Geometry", ha="center", fontsize=19, weight="bold", color=INK)
    ax.text(0, -4.1, r"The construction uses $(r,\theta,z)$ in space while retaining scalar time $t$.", ha="center", fontsize=11.5, color=GREY)
    save(fig, "figure-2-spatial-centre-ring-geometry.png")


def scaling_plot() -> None:
    h = 1 / 200
    tau = np.logspace(0, -6, 600)
    curves = {
        r"radius $\ell_r\sim\tau^{1/2}$": (tau ** 0.5, TEAL, "-"),
        r"area $A\sim\tau$": (tau, GREEN, "-"),
        r"period $P_\theta\sim\tau^{1+h}$": (tau ** (1 + h), ORANGE, "-"),
        r"velocity $u_\theta\sim\tau^{-1/2-h}$": (tau ** (-0.5 - h), RED, "--"),
        r"acceleration $a_c\sim\tau^{-3/2-2h}$": (tau ** (-1.5 - 2 * h), INK, "--"),
        r"energy $E_c\sim\tau^{1/2-3h}$": (tau ** (0.5 - 3 * h), GREY, ":"),
    }

    fig, ax = plt.subplots(figsize=(11.5, 7.2))
    for label, (values, color, linestyle) in curves.items():
        ax.plot(tau, values, label=label, color=color, linestyle=linestyle, linewidth=2.3)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.invert_xaxis()
    ax.grid(True, which="both", linewidth=0.55, color="#D0D5DD", alpha=0.7)
    ax.set_xlabel(r"Remaining scalar time $\tau=t_*-t$ (approaching zero to the right)", fontsize=12)
    ax.set_ylabel("Normalised asymptotic magnitude", fontsize=12)
    ax.set_title("Rates Implied by the Published Similarity Scales", fontsize=19, weight="bold", color=INK, pad=14)
    ax.legend(loc="upper left", frameon=True, framealpha=0.96, fontsize=10.5)
    ax.text(
        0.98,
        0.03,
        r"Illustrative exponent $h=1/200$; constants suppressed.",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=10,
        color=GREY,
    )
    fig.tight_layout()
    save(fig, "figure-3-similarity-scaling.png")


def main() -> int:
    contact_map()
    centre_ring_geometry()
    scaling_plot()
    print(f"Generated 3 figures in {FIGURES}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
