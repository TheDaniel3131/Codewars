def are_you_playing_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
    
def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";