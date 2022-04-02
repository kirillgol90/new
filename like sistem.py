def likes(names):
    others = len(names) - 2  # var, counting others in "name,name and N others"
    if len(names) == 0:  # likes for 0
        return "no one likes this"
    elif 3 >= len(names) > 0:
        if len(names) == 1:  # for 1
            return "{name} likes this".format(name=names[0])
        elif len(names) == 2:   # for 2
            return "{name1} and {name2} like this".format(name1=names[0], name2=names[1])
        elif len(names) == 3:   # for 3
            return "{name1}, {name2} and {name3} like this".format(name1=names[0], name2=names[1], name3=names[2])
    else:   # for 4 and next
        return "{name1}, {name2} and {count} others like this".format(name1=names[0], name2=names[1], count=others)


likes('name')
