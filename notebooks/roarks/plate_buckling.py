"""
Reference: Roark's 7th Edition
Table 15.2: Formulas for elastic stability of plates and shells
"""
import numpy as np
from scipy.interpolate import interp1d


def critical_stress_1(side_b: float, thickness: float,
                      elastic_modulus: float, poisson: float,
                      k: float) -> float:
    """Calculates the critical compressive stress for all case 1's."""
    b = side_b
    t = thickness
    e = elastic_modulus
    v = poisson

    stress: float = k * e / (1 - v ** 2) * (t / b) ** 2

    return stress


def k_interpolation(ab_ratio: float, a_over_b: list[float],
                    k_table: list[float]) -> float:
    k_interp = interp1d(a_over_b, k_table, kind='linear',
                        bounds_error=False,
                        fill_value="extrapolate")
    return k_interp(ab_ratio)


def roarks_15_2_1a(side_a: float, side_b: float, thickness: float,
                   elastic_modulus: float, poisson: float) -> float:
    """Rectangular plate under uniform compression on two opposite edges b.
    All edges simply supported.  Returns the critical compressive stress."""
    a_over_b = [0.2, 0.3, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.4, 2.7,
                3.0, np.inf]
    k_table = [22.2, 10.9, 6.92, 4.23, 3.45, 3.29, 3.4, 3.68, 3.45, 3.32, 3.29,
               3.32, 3.40, 3.32, 3.29, 3.29]
    ab_ratio = side_a / side_b
    k = k_interpolation(ab_ratio=ab_ratio, a_over_b=a_over_b, k_table=k_table)
    return critical_stress_1(side_b=side_b, thickness=thickness,
                             elastic_modulus=elastic_modulus, poisson=poisson,
                             k=k)


def roarks_15_2_1b(side_a: float, side_b: float, thickness: float,
                   elastic_modulus: float, poisson: float) -> float:
    """Rectangular plate under uniform compression on two opposite edges b.
    All edges clamped.  Returns the critical compressive stress."""
    a_over_b = [1, 2, 3, np.inf]
    k_table = [7.7, 6.7, 6.4, 5.73]
    ab_ratio = side_a / side_b
    k = k_interpolation(ab_ratio=ab_ratio, a_over_b=a_over_b, k_table=k_table)
    return critical_stress_1(side_b=side_b, thickness=thickness,
                             elastic_modulus=elastic_modulus, poisson=poisson,
                             k=k)


def roarks_15_2_1c(side_a: float, side_b: float, thickness: float,
                   elastic_modulus: float, poisson: float) -> float:
    """Rectangular plate under uniform compression on two opposite edges b.
    Edges b simply supported, edges a clamped.  Returns the critical compressive
    stress."""
    a_over_b = [0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.1, np.inf]
    k_table = [7.76, 6.32, 5.80, 5.76, 6.0, 6.32, 5.80, 5.76, 6.0, 5.8, 5.76,
               5.73]
    ab_ratio = side_a / side_b
    k = k_interpolation(ab_ratio=ab_ratio, a_over_b=a_over_b, k_table=k_table)
    return critical_stress_1(side_b=side_b, thickness=thickness,
                             elastic_modulus=elastic_modulus, poisson=poisson,
                             k=k)


def roarks_15_2_1d(side_a: float, side_b: float, thickness: float,
                   elastic_modulus: float, poisson: float) -> float:
    """Rectangular plate under uniform compression on two opposite edges b.
    Edges b simply supported, one edges a simply supported, other edge a free.
    Returns the critical compressive stress."""
    a_over_b = [0.5, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.5, 3.0, 4.0, 5.0]
    k_table = [3.62, 1.18, 0.934, 0.784, 0.687, 0.622, 0.574, 0.502, 0.464,
               0.425, 0.416]
    ab_ratio = side_a / side_b
    k = k_interpolation(ab_ratio=ab_ratio, a_over_b=a_over_b, k_table=k_table)
    return critical_stress_1(side_b=side_b, thickness=thickness,
                             elastic_modulus=elastic_modulus, poisson=poisson,
                             k=k)


def roarks_15_2_1e(side_a: float, side_b: float, thickness: float,
                   elastic_modulus: float, poisson: float) -> float:
    """Rectangular plate under uniform compression on two opposite edges b.
    Edges b simply supported, one edges a clamped, other edge a free.
    Returns the critical compressive stress."""
    a_over_b = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.2, 2.4]
    k_table = [1.40, 1.28, 1.21, 1.16, 1.12, 1.10, 1.09, 1.09, 1.10, 1.12, 1.14,
               1.19, 1.21]
    ab_ratio = side_a / side_b
    k = k_interpolation(ab_ratio=ab_ratio, a_over_b=a_over_b, k_table=k_table)
    return critical_stress_1(side_b=side_b, thickness=thickness,
                             elastic_modulus=elastic_modulus, poisson=poisson,
                             k=k)


def roarks_15_2_1f(side_a: float, side_b: float, thickness: float,
                   elastic_modulus: float, poisson: float) -> float:
    """Rectangular plate under uniform compression on two opposite edges b.
    Edges b clamped, edges a simply supported.
    Returns the critical compressive stress."""
    a_over_b = [0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.7, 1.8, 2.0, 2.5, 3.0]
    k_table = [11.0, 7.18, 5.54, 4.80, 4.48, 4.39, 4.39, 4.26, 3.99, 3.72, 3.63]
    ab_ratio = side_a / side_b
    k = k_interpolation(ab_ratio=ab_ratio, a_over_b=a_over_b, k_table=k_table)
    return critical_stress_1(side_b=side_b, thickness=thickness,
                             elastic_modulus=elastic_modulus, poisson=poisson,
                             k=k)

# todo case 11
# todo case 12
# todo case 15
# todo case 16
# todo case 19
# todo case 20
