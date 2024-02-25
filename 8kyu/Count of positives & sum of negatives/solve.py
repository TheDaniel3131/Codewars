def count_positives_sum_negatives(arr):
    if not arr: return []
    
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    
    return [pos, neg]