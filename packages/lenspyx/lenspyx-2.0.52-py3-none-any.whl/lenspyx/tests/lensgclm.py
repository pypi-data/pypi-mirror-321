"""Times the deflection angles calculation etc

    python ./lenspyx/tests/lensgclm.py

"""
import numpy as np
from lenspyx.tests.helper import syn_ffi_ducc_29, syn_ffi_ducc, cls_unl, syn_alms
from lenspyx.utils_hp import synalm, Alm
import multiprocessing
import argparse
import time
import tracemalloc
from lenspyx.utils import timer
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test FFP10-like fwd building')
    parser.add_argument('-s', dest='spin', type=int, default=0, help='spin to test')
    parser.add_argument('-lmaxlen', dest='lmax_len', type=int, default=4096, help='lmax of lensed CMBs')
    parser.add_argument('-dlmaxgl', dest='dlmax_gl', type=int, default=1024, help='buffer to GL grid')
    parser.add_argument('-dlmax', dest='dlmax', type=int, default=1024, help='buffer to lensed alms')
    parser.add_argument('-eps', dest='epsilon', type=float, default=5, help='-log10 of nufft accuracy')
    parser.add_argument('-n', dest='nt', type=int, default=4, help='number of threads')
    parser.add_argument('-bwd', dest='bwd', action='store_true', help='adjoint lensing')
    parser.add_argument('-gonly', dest='gonly', action='store_true', help='grad-only mode')
    parser.add_argument('-v', dest='verbose', action='store_true')
    parser.add_argument('-valg', dest='algversion', type=int, default=29)
    parser.add_argument('-inplace', dest='inplace', action='store_true', help='write to input array (spares a gclm with lmax_len')
    parser.add_argument('-tracemalloc', dest='tracemalloc',  action='store_true', help='trace memory usage')

    args = parser.parse_args()
    nthreads = args.nt
    if args.algversion == 29:
        ffi, geom = syn_ffi_ducc_29(lmax_len=args.lmax_len, dlmax=args.dlmax, dlmax_gl=args.dlmax_gl, nthreads=nthreads,
                                 verbosity=args.verbose, epsilon=10 ** (-args.epsilon))
    else:
        ffi, geom = syn_ffi_ducc(lmax_len=args.lmax_len, dlmax=args.dlmax, dlmax_gl=args.dlmax_gl, nthreads=nthreads,
                                 verbosity=args.verbose, epsilon=10 ** (-args.epsilon))
    lmax_len, mmax_len = args.lmax_len, args.lmax_len
    lmax_unl, mmax_unl = args.lmax_len + args.dlmax, args.lmax_len + args.dlmax

    rtyp = np.float32 if ffi.single_prec else np.float64
    ctyp = np.complex64 if ffi.single_prec else np.complex128

    npix = geom.npix()
    nrings = ffi.geom.theta.size
    ncomp = 1 + (args.spin > 0) * (not args.gonly)
    eblm = syn_alms(args.spin, lmax_unl=lmax_unl, ctyp=ctyp)
    if args.inplace:
        outsize = Alm.getsize(args.lmax_len, args.lmax_len)
        eblm_out = eblm[:, :outsize] # NB slicing not a must here
        assert eblm_out.base is eblm # Checking this is indeed a view
    else:
        eblm_out = None
    mode = 'STANDARD' if not args.gonly or args.spin == 0 else 'GRAD_ONLY'
    if args.tracemalloc:
        tracemalloc.start()
    ffi._build_angles()
    for nthreads in [nthreads]:
        ffi.sht_tr = nthreads
        ffi.tim = timer('ffi timer', False)
        t0 = time.time()
        len_tlm1 = ffi.lensgclm(eblm, mmax_unl, args.spin, args.lmax_len, args.lmax_len, backwards=args.bwd,
                                out_sht_mode=mode, gclm_out=eblm_out)
        t1 = time.time()
        print('Transform type', eblm.dtype, ' to ', len_tlm1.dtype)
        print(" %s threads, spin %s lmax %s, nrings %s Mpix %s:"%(ffi.sht_tr, args.spin, ffi.lmax_dlm, nrings, npix/1e6))
        print('            calc: %.3f Mpix/s, total %.3f sec'%(npix / (t1 - t0) / 1e6, t1 - t0))
        print(ffi.tim)
        if args.inplace:
            assert len_tlm1.base is eblm

        if args.tracemalloc:
            size, peak = tracemalloc.get_traced_memory()
            print("     Tracemalloc size and peak :", f"{size=}, {peak=}")
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')
            print("     Tracemalloc first 4 lines:")
            for stat in top_stats[:4]:
                print(stat)