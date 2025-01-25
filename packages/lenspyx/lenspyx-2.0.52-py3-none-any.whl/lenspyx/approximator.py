import ducc0
import numpy as np
import matplotlib.pyplot as plt

def bump(n):
    x = np.linspace(0., 1., n, endpoint=True)
    x = np.exp(-1./x)
    x = x/(x+x[::-1])
    return x

def zeropad(a, n):
    res = np.zeros(n)
    res[:a.shape[0]] = np.roll(a, a.shape[0]//2, 0)
    return np.roll(res, -(a.shape[0]//2), 0)

def suppress(a, w, lo, hi):
    res = a.copy()
    res[lo:lo+w] *= 1.-bump(w)
    res[hi-w:hi] *= bump(w)
    res[lo+w:hi-w] *= 0
    return res

def resample(a, n):
    t = ducc0.fft.genuine_fht(a, inorm=2)
    t = zeropad(t, n)
    return ducc0.fft.genuine_fht(t)

def find_approximation(func_in, period_in, limit):
    """
    Approximate parts of a bandlimited, periodic function by another function
    with fewer points.

    Arguments
    ---------
    func_in : np.ndarray((N,), dtype=np.float64)
        function samples for one period
    period_in : float
        period of the input function in arbitrary units
    limit : float
        upper bound (same units as period_in) up to which the function
        shall be approximated

    Returns
    -------
    np.ndarray((N2,), dtype=np.float64)
        samples for one period of the approximating function
    float
        period (same units as period_in) of the approximating function
    """

    N = func_in.shape[0]
    ofactor = 1.5  # oversampling factor
    N_over = ducc0.fft.good_size(int(N*ofactor),True)
    bw = 300 # taper width
    N_cut = int(N_over*limit/period_in)+2*bw
    if N_cut >= N:  # not worth the trouble
        return func_in, period_in
    data_over = resample(func_in, N_over)
    data_suppress = suppress(data_over, bw, N_cut-2*bw, N_over)
    res = np.zeros(N_cut)
    res[:N_cut-bw] = data_suppress[:N_cut-bw]
    res[-bw:] = data_suppress[-bw:]
    return res, period_in*N_cut/N_over 


# input function is white noise (well, in Cartesian space that IS bandlimited :)
func_in = np.random.uniform(low=-0.5,high=0.5,size=(10000,))
# if func_in is 2pi-periodic, get an approximation for the interval [0; 0.3]
appr, period = find_approximation(func_in, 2*np.pi, 0.3)
print(f"approximating function has {appr.size} points and a period of {period}")

# Zoom into original and approximation functions and compare them 
# (this is actually the most complicated part)
func_zoom=resample(func_in,100*func_in.size)
appr_zoom=resample(appr, 100*appr.size)
dx_func = 2*np.pi/func_zoom.size
dx_appr = period/appr_zoom.size
lim=0.1
n_func = int(lim/dx_func)
n_appr =int(lim/dx_appr)
func_zoom = func_zoom[:n_func]
appr_zoom = appr_zoom[:n_appr]
plt.plot(np.arange(func_zoom.size)*dx_func,func_zoom)
plt.plot(np.arange(appr_zoom.size)*dx_appr,appr_zoom)
plt.show()
