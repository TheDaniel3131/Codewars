def get_size(w,h,l):
    # l = length, w = width, h = height
    surface_area = 2 * (l * w) + 2 * (w * h) + 2 * (h * l)
    volume = l * w * h
    return [surface_area,volume]