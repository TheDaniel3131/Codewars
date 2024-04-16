def warn_the_sheep(queue):
    n = len(queue)
    if queue[n-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    else:
        for i in range(n-2, -1, -1):
            if queue[i] == "wolf":
                return f"Oi! Sheep number {n-i-1}! You are about to be eaten by a wolf!"
            
            
def warn_the_sheep(queue):
    n = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'


def warn_the_sheep(queue):
    queue.reverse()
    return 'Pls go away and stop eating my sheep' if queue[0] == 'wolf' else 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(queue.index('wolf'))


def warn_the_sheep(queue):    
    queue.reverse()
    wolfnum = queue.index("wolf")
    if wolfnum == 0:
        return "Pls go away and stop eating my sheep"
    else:
        return "Oi! Sheep number {0}! You are about to be eaten by a wolf!".format(wolfnum)
                                                                                   

                                                                                   
def warn_the_sheep(queue):
  return 'Pls go away and stop eating my sheep' if queue[-1] == 'wolf' else f'Oi! Sheep number {queue[::-1].index("wolf")}! You are about to be eaten by a wolf!'
                                                                                   
                                                                                   