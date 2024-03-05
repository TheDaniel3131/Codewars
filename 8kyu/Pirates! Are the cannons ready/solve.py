def cannons_ready(gunners):
    # values() method returns a view object.
    # The view object contains the values of the dictionary, as a list.
    
    # Test Cases:
#         a = {'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}
#         b = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}
#         c = {'Joe':'nay','Johnson':'nay','Peter':'aye'}
#         d = {'Mike':'nay','Joe':'nay','Johnson':'nay','Peter':'nay'}
    
    if "nay" in gunners.values():
        return "Shiver me timbers!"
    else:
        return "Fire!"