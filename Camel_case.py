def to_camel_case(text):
    rep = text.replace("_", " ").replace("-", " ")  # replacing separators in original name
    spl = rep.split(" ")  # splitting original name
    x = spl[0].lower()  # variable, needed to maintain capitalizing only if the first letter is capital
    '''doing camel'''
    if spl[0] == x:  # "if" for string 4
        for i in range(len(spl)):
            spl[i] = spl[i].capitalize()  # capitalizing every part of the name

        spl[0] = spl[0].lower()  # lowering first letter for string 4
        return "".join(spl)

    else:
        for i in range(len(spl)):
            spl[i] = spl[i].capitalize()

        return "".join(spl)



