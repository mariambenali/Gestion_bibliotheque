from info import users, books,books_liked


def filter_adults ():
    return [user for user in users if user[3] >= 18]

print(filter_adults())



def modify_names():
    return list(map(str.upper,[user[1] for user in users]))

print(modify_names())


def dictionary_users(users, books_liked):
    dict = {}
    for (id_users, prenom, nom, age ) in users:
        liked_list =[]
        for (id_book, title)in books_liked:
            if id_users == id_book:
                liked_list.append(title)

        dict [id_users]= {
                "prenom": prenom, 
                "nom": nom, 
                "age":age, 
                "books_liked": liked_list}

    return dict

print(dictionary_users(users, books_liked))








        
    


            
        



