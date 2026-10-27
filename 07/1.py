def modus_ponens(kb, f):
    nf = set(f)
    ch = True
    
    while ch:
        ch = False
        for r in kb:
            pre, con = r
            if all(p in nf for p in pre):
