from scipy.optimize import root_scalar


def diaphragm_constants_case_1(poissons: float = 0.3) -> dict:
    k1 = 1.016 / (1 - poissons)
    k2 = 0.376
    k3 = 1.238 / (1 - poissons)
    k4 = 0.294
    return {"k1": k1, "k2": k2, "k3_center": k3, "k4_center": k4, "k3_edge": 0,
            "k4_edge": 0}


def diaphragm_constants_case_2(poissons: float = 0.3) -> dict:
    k1 = 5.33 / (1 - poissons ** 2)
    k2 = 0.857
    k3_center = 2 / (1 - poissons)
    k4_center = 0.50
    k3_edge = 4 / (1 - poissons ** 2)
    k4_edge = 0.0
    return {"k1": k1, "k2": k2, "k3_center": k3_center, "k4_center": k4_center,
            "k3_edge": k3_edge, "k4_edge": k4_edge}


def diaphragm_constants_case_3(poissons: float = 0.3) -> dict:
    k1 = 5.33 / (1 - poissons ** 2)
    k2 = 2.6 / (1 - poissons ** 2)
    k3_center = 2 / (1 - poissons)
    k4_center = 0.976
    k3_edge = 4 / (1 - poissons ** 2)
    k4_edge = 1.73
    return {"k1": k1, "k2": k2, "k3_center": k3_center, "k4_center": k4_center,
            "k3_edge": k3_edge, "k4_edge": k4_edge}

# TODO # Implement Case 4
# TODO # Implement Case 5
# TODO # Implement Case 6
# TODO # Implement Case 7
# TODO # Implement Case 8
# TODO # Implement Case 9

def roarks_11_11_1(deflection: float, thickness: float, outer_radius: float,
                   pressure: float, elastic_modulus: float,
                   k1: float, k2: float):
    """Presents the equation as a difference to facilitate finding the root."""
    y = deflection
    t = thickness
    a = outer_radius
    q = pressure
    E = elastic_modulus

    return k1 * y / t + k2 * (y / t) ** 3 - q * a ** 4 / (E * t ** 4)


def find_diaphragm_deflection(thickness: float, outer_radius: float,
                              pressure: float, elastic_modulus: float,
                              k1: float,
                              k2: float) -> float:
    """Finds the deflection that is the solution for Roark's equation 11.11-1"""
    args = (thickness, outer_radius, pressure, elastic_modulus, k1, k2)
    bracket = [0, outer_radius]
    x0 = thickness

    y = root_scalar(f=roarks_11_11_1, args=args, method='bisect',
                    bracket=bracket).root

    return y


def roarks_11_11_2(deflection: float, thickness: float, outer_radius: float,
                   elastic_modulus: float, k3: float,
                   k4: float) -> float:
    """Returns the stress from Roark's equation 11.11-2"""
    y = deflection
    t = thickness
    a = outer_radius
    E = elastic_modulus
    stress = (k3 * y / t + k4 * (y / t) ** 2) * E * t ** 2 / a ** 2

    return stress


def diaphragm_stresses(thickness: float, outer_radius: float, pressure: float,
                       elastic_modulus: float,
                       poissons_ratio: float, case_no: int = 1) -> dict:
    """
    Find the maximum deflection and the diaphragm stresses for a circular plate.
    Case 1: Simply supported (neither fixed nor held), Pressure over entire plate.
    Case 2: Fixed but not held (no edge tension). Pressure over entire plate.
    Case 3: Fixed and held. Pressure over entire plate.
    Case 4: not implemented
    Case 5: not implemented
    Case 6: not implemented
    Case 7: not implemented
    Case 8: not implemented
    Case 9: not implemented
    """

    t = thickness
    a = outer_radius
    q = pressure
    E = elastic_modulus
    v = poissons_ratio
    case_no = case_no

    if case_no == 1:
        constants = diaphragm_constants_case_1(poissons=v)
    elif case_no == 2:
        constants = diaphragm_constants_case_2(poissons=v)
    elif case_no == 3:
        constants = diaphragm_constants_case_3(poissons=v)
    else:
        return "Case is not implemented."

    k1 = constants["k1"]
    k2 = constants["k2"]
    k3_center = constants["k3_center"]
    k4_center = constants["k4_center"]
    k3_edge = constants["k3_edge"]
    k4_edge = constants["k4_edge"]

    # find the deflection
    y = find_diaphragm_deflection(thickness=t, outer_radius=a, pressure=q,
                                  elastic_modulus=E, k1=k1, k2=k2)

    # find the stress at the edge
    s_edge = roarks_11_11_2(deflection=y, thickness=t, outer_radius=a,
                            elastic_modulus=E, k3=k3_edge, k4=k4_edge)

    # find the stress at the center
    s_center = roarks_11_11_2(deflection=y, thickness=t, outer_radius=a,
                              elastic_modulus=E, k3=k3_center, k4=k4_center)

    return {"deflection": y, "stress_center": s_center, "stress_edge": s_edge}
