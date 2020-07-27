# Returns the riemann zeta value of a given number
def riemann_zeta(p,limit):
    convergence_sum = 0
    for i in range(1, limit + 1):
        convergence_sum += 1/(i ** p)
    return convergence_sum


