
def forward_chaining(KB, q: Symbol) -> bool:
    count = {c: len(c.premise) for c in KB.clauses}
    inferred = set()
    # initially known to be true symbols:
    queue = [c.conclusion for c in KB.clauses if len(c.premise)==0]
    while queue:
        p = queue.pop()
        if p == q: return True
        if p not in inferred:
            inferred.add(p)
            for c in KB.clauses:
                if p in c.premise:
                    count[c] -= 1
                    if count[c] == 0: queue.append(c.conclusion)
    return False