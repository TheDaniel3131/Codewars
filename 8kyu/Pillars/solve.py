def pillars(num_pill, dist, width):
    dist_cm = dist * 100
    total_dist = (num_pill - 1) * dist_cm
    excluded_width = (num_pill - 2) * width
    
    if num_pill < 1 or dist == width:
        return 0;
    else:
        return total_dist + excluded_width
        