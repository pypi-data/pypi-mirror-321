# Copyright 2024-2025 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
### Number theory library

"""
from __future__ import annotations

from collections.abc import Iterator
from dtools.circular_array.ca import ca, CA
from dtools.fp.iterables import foldL1
from .num_theory import coprime

__all__ = [ 'comb' ]

# Combinatorics

def comb(n: int, m: int, /, targetTop: int=700, targetBot: int=5) -> int:
    """Implementation of the combinatorial `C(n,m)`

    * the number of `n` items taken `m` at a time.
    * geared to works efficiently for Python's arbitrary length integers
    * default parameters geared to large values of `n` and `m`
    * the defaults work reasonably well for smaller (human size) values
    * for inner loops with smaller values, use `targetTop = targetBot = 1`
      * or just use `math.comb(n, m)` instead
    * raises ValueError if `n < 0` or `m < 0`

    """
    # edge cases
    if n < 0 or m < 0:
        raise ValueError('for C(n, m) n and m must be non-negative ints')
    if n == m or m == 0:
        return 1
    elif m > n:
        return 0

    # using C(n, m) = C(n, n-m) to reduce number of factors in calculation
    if m > (n // 2):
        m = n - m

    # Prepare data structures
    tops: ca[int] = ca(range(n - m + 1, n + 1))
    bots: ca[int] = ca(range(1, m+1))

    # Compacting data structures makes algorithm work better for larger values
    size = len(tops)
    while size > targetTop:
        size -= 1
        top, bot = coprime(tops.popL() * tops.popL(), bots.popL() * bots.popL())
        tops.pushR(top)
        bots.pushR(bot)

    while size > targetBot:
        size -= 1
        bots.pushR(bots.popL() * bots.popL())

    # Cancel all factors in denominator before multiplying the remaining factors
    # in the numerator.
    for bot in bots:
        for ii in range(len(tops)):
            top, bot = coprime(tops.popL(), bot)
            if top > 1:
                tops.pushR(top)
            if bot == 1:
                break

    ans = tops.foldL(lambda x, y: x * y, initial=1)
    assert ans is not None
    return ans

