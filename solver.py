"""A solver for the 1D diffusion equation."""
## Libraries
import numpy as np 

np.set_printoptions(formatter={"float":"{:6.1f}".format})

## Solving it

# C = concentration
# dx = space step
# dt = time step
# D = diffusivity
# q = flux

def solve1d(C,dx,dt,D,it, maxit): 
    # pass # it worked as a place holder when learning about functions
    # print("hi")
    q = -D * np.diff(C) / dx
    C[1:-1] -= dt * np.diff(q) / dx
    print(f'Output {it}:')
    print(C)
    it += 1
    if it <= maxit:
       C = solve1d(C,dx,dt,D,it, maxit) 
    return C

def _example(): # _ stands for don't the main function
    D = 100
    Lx = 10
    dx =0.5
    C1 = 500
    C2 = 0
    C = np.empty(Lx)
    C[: int(Lx/2)] = C1 # from first element to the halfway
    C[int(Lx/2) :] = C2 # from halfway to last element
    dt = dx * dx / D / 2.1
    it = 1
    maxit = 4
    
    print('Input:')
    print(C)
    
    C = solve1d(C, dx, dt, D, it, maxit)
    
    # for _ in range(1,5): # Look for iterations that yield estable conditions
        # C = solve1d(C, dx, dt, D)
        # print(f'Output {_}:')
        # print(C)
        # if _ == 1:
        #     print('We operate in this region')
        #     print(C[1:-1])
        
print(__name__)
if __name__ == "__main__": # if the name of the modulus is __main__
    _example()