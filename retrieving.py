from mapping_single import User, Session, engine

local_session = Session(bind=engine)

users = local_session.query(User).all()

for user in users:
    print(user.username)

