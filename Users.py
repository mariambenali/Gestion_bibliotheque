from data import users



def filter_adults ():
    return list(filter(lambda user: user[2] >= 18, users))

print(filter_adults())



def modify_names():
    return list (map(str.upper, [user[0] for user in users]))

print(modify_names())