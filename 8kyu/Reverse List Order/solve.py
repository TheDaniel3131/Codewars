def reverse_list(l):
    return l[::-1]

def reverse_list(l):
    return list(reversed(l))

    
def reverse_list(l):
  new_list = []
  for i in l:
      new_list = [i] + new_list
  return new_list

reverse_list = lambda l: l.reverse() or l


def reverse_list(l):
    l.reverse()
    return l
