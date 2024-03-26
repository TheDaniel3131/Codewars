def solution(arr_val, arr_unit):
    
    G = 6.67 * (10**-11) 
    mass_units = {"kg": 1, "g": 10**-3, "mg": 10**-6, "μg": 10**-9, "lb": 0.453592}
    distance_units = {"m": 1, "cm": 10**-2, "mm": 10**-3, "μm": 10**-6, "ft": 0.3048}

    m1 = arr_val[0] * mass_units[arr_unit[0]]
    m2 = arr_val[1] * mass_units[arr_unit[1]]
    r = arr_val[2] * distance_units[arr_unit[2]]
    
    # formula of gravitational force
    # F = G * M * m / (r ** 2)
    F = G * (m1 * m2) / (r**2)

    return F
