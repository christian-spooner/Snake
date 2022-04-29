import numpy

def movement():
    RNG = numpy.random.randint(0, 4)
    if RNG == 1:
        return "UP"
    elif RNG == 2:
        return "DOWN"
    elif RNG == 3:
        return "LEFT"
    elif RNG == 4:
        return "RIGHT"
    else:
        return "NONE"