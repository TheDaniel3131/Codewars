def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    
    # Test Cases
    print(seconds)
    print(minutes)
    print(hours)
    
    return f"{hours:02}:{minutes:02}:{seconds:02}"
