from __future__ import annotations

def stockfinder_safe(
    stockfinder_fn,
    *,
    concUM: float,
    highest_stock_mM: float,
    V2_ul: float,
    dmso_percmax: float,
    sourceplate_type: str,
):
    """
    Wrapper around stockfinder() that makes plate type explicit.

    stockfinder() reads a global variable named `sourceplate_type`.
    This wrapper sets it only for the duration of the call (contained side-effect).
    """
    stockfinder_fn.__globals__["sourceplate_type"] = sourceplate_type
    return stockfinder_fn(concUM, highest_stock_mM, V2_ul, dmso_percmax)
