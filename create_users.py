from mapping_single import User, Session, engine

users = [
    {
        "username": "nick",
        "email": "nick@gmail.com"
    },
    {
        "username": "michel",
        "email": "michel@gmail.com"
    }, {
        "username": "natalia",
        "email": "natalia@gmail.com"
    }, {
        "username": "larissa",
        "email": "larissa@gmail.com"
    }, {
        "username": "john",
        "email": "john@gmail.com"
    }, {
        "username": "frederico",
        "email": "frederico@gmail.com"
    },
]

local_session = Session(bind=engine)

# new_user=User(username="jona",email="jona@company.com")

# local_session.add(new_user)

# local_session.commit()


for u in users:
    new_user = User(username=u["username"], email=u["email"])

    local_session.add(new_user)

    local_session.commit()

    # f strings
    print(f"Added {u['username']}")
