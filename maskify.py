def maskify(cc):
    cc = str(cc)
    return '#' * (len(cc) - 4) + cc[-4:]
