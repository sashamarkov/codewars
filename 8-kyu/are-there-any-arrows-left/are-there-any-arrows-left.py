def any_arrows(arrows):
    return any(map(lambda a: 'damaged' not in a or not a['damaged'], arrows))