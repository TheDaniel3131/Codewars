def rgb(*args):
    # check if the args are within the RGB range 
    check_rgb = [max(min(i, 255), 0) for i in args]
    
    # return with Hexadecimal Converted Codes and uppercases
    return ''.join(f'{j:02x}' for j in check_rgb).upper()
