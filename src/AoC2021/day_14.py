from typing import Dict

_pd_cache = { 'cache_hits': 0, 'total_calls': 0 }
def _pair_dive_with_cache(pair: str, rules: Dict[str, str], dives: int) -> Dict[str, int]:
    _pd_cache['total_calls'] += 1
    cache_key = (pair, dives)

    if cache_key in _pd_cache:
        _pd_cache['cache_hits'] += 1

        return _pd_cache[cache_key].copy()
    
    elements = {}
    if not dives:
        elements[pair[1]] = 1
        # print(f"{cache_key}: {elements}")
    else:
        p0 = pair[0] + rules[pair]
        p1 = rules[pair] + pair[1]
        elements = _pair_dive_with_cache(p0, rules, dives - 1)
        e1 = _pair_dive_with_cache(p1, rules, dives - 1)

        # print(f"({p0!r}, {dives}): {elements}")
        # print(f"({p1!r}, {dives}): {e1}")

        for k in e1:
            if k in elements:
                elements[k] += e1[k]
            else:
                elements[k] = e1[k]

    if not cache_key in _pd_cache:
        _pd_cache[cache_key] = elements
    
    return elements.copy()


def apply_polymer_formula_cached(template: str, rules: Dict[str, str], dives: int) -> Dict[str, int]:
    elements = {}
    elements[template[0]] = 1

    for i in range(1, len(template)):
        pair = template[i - 1] + template[i]
        e = _pair_dive_with_cache(pair, rules, dives)
        for k in e:
            if k in elements:
                elements[k] += e[k]
            else:
                elements[k] = e[k]
    
    print(f"Total Calls: {_pd_cache['total_calls']!r}")
    print(f"Cache Hits: {_pd_cache['cache_hits']!r}")
    print(f"Cache Ratio: {_pd_cache['cache_hits']/_pd_cache['total_calls']!r}")
    # print(_pd_cache)
    return elements
