users = [{
    "id": 1,
    "first_name": "Clementia",
    "last_name": "Curran",
    "email": "ccurran0@geocities.jp"
}, {
    "id": 2,
    "first_name": "Lucho",
    "last_name": "Cockling",
    "email": "lcockling1@cbslocal.com"
}, {
    "id": 3,
    "first_name": "Gussie",
    "last_name": "Crichley",
    "email": "gcrichley2@elegantthemes.com"
}, {
    "id": 4,
    "first_name": "Ashla",
    "last_name": "Sawkins",
    "email": "asawkins3@reddit.com"
}, {
    "id": 5,
    "first_name": "Reinwald",
    "last_name": "Edwin",
    "email": "redwin4@phoca.cz"
}, {
    "id": 6,
    "first_name": "Carlynne",
    "last_name": "Janks",
    "email": "cjanks5@opera.com"
}, {
    "id": 7,
    "first_name": "Packston",
    "last_name": "Breed",
    "email": "pbreed6@icq.com"
}, {
    "id": 8,
    "first_name": "Douglas",
    "last_name": "Ziehms",
    "email": "dziehms7@flavors.me"
}, {
    "id": 9,
    "first_name": "Debbie",
    "last_name": "Tench",
    "email": "dtench8@washingtonpost.com"
}, {
    "id": 10,
    "first_name": "Wilie",
    "last_name": "Huntley",
    "email": "whuntley9@shutterfly.com"
}]


# CRUD: Crete, Read, Update, Delete

def find_user(id: int):
    for user in users:
        if user['id'] == id:
            return user
    # return None


# def find_user_by(key, value):
#     for user in users:
#         if user[key] == value:
#             return user


print('finduser', find_user(1))


def remove_user(id):
    user = find_user(id)
    if user is not None:
        users.remove(user)


remove_user(10)
print(users)


def update_user(id: int, updated_user: dict) -> dict:
    # find updatable user
    user = find_user(id)
    # if user exists
    if user is not None:
        # get the index
        i = users.index(user)
        users[i].update(updated_user)
        return users[i]


update_user(1, {'first_name': 'Johnny', 'last_name': 'Doedoe'})
print(find_user(1))


# NOOOOOO!!!!!!
# index = 10
# def index()

def create_user(user: dict) -> dict:
    # id-t generáljátok le, az utolsó elem id-ja + 1
    new_user = {'id': users[-1]['id'] + 1}
    new_user.update(user)
    users.append(new_user)
    return users[-1]


print(create_user({'first_name': 'first', 'last_name': 'last', 'mail': 'email@mail.com'})
      )
