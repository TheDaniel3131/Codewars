def generate_hashtag(s):
    format_s = "#" +  "".join(i.capitalize() for i in s.split())
    
    # use "or" because it could be one of each
    if not s or len(format_s) > 140:
        return False
    else:
        return format_s