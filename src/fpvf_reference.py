"""Numerical FPVF/Soul-Shell reference kernels.

Historical model only. Names do not imply consciousness, awareness or subjective state.
"""
from math import fsum
from typing import Callable, Sequence

def fpvf(n: float, score: Callable[[float],float], perspective: Callable[[float],float]) -> float:
    return score(n)*perspective(n)

def weighted_memory(values: Sequence[float], weights: Sequence[float], n: int) -> float:
    if n < 0: raise ValueError("n must be nonnegative")
    if len(values) != len(weights): raise ValueError("values and weights must align")
    if n >= len(values): raise IndexError("n outside sequence")
    return fsum(values[i]*weights[i] for i in range(n+1))

def finite_difference(f: Callable[[float],float], x: float, h: float=1e-5) -> float:
    if h == 0: raise ValueError("h must be nonzero")
    return (f(x+h)-f(x))/h

def trapezoid_projection(t: float, score: Callable[[float],float],
                         perspective: Callable[[float],float], intervals: int=100) -> float:
    if t < 0: raise ValueError("t must be nonnegative")
    if intervals < 1: raise ValueError("intervals must be >= 1")
    h=t/intervals
    vals=[score(i*h)*perspective(i*h) for i in range(intervals+1)]
    return h*(0.5*vals[0]+fsum(vals[1:-1])+0.5*vals[-1])

def soul_shell(motive: float, memory_sum: float, temporal_sum: float,
               score_delta: float, residual: float) -> float:
    return fsum([motive,memory_sum,temporal_sum,score_delta,residual])

def unified(shell: float, projection: float) -> float:
    return shell+projection
