def ping_pong(sounds):
    who_serve = None
    last_hit = None
    pong = 0
    ping = 0
    for h in sounds.split("-"):
        if h in ["ping", "pong"]:
            last_hit = h
            if not who_serve:
                who_serve = h
        else:
            if who_serve == "ping" and last_hit == "pong":
                ping += 1
            elif who_serve == "pong" and last_hit == "ping":
                pong += 1
            who_serve = None
    if ping > pong:
        return "ping"
    if pong > ping:
        return "pong"
    return "pong" if last_hit == "ping" else "ping"
    
    
    
                
    
       