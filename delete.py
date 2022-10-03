from mapping_single import Session, engine, User


local_session = Session(bind=engine)

# mudar para o nome do usuario desejado
user_to_delete = local_session.query(User).filter(User.username == "jonathan").first()

local_session.delete(user_to_delete)

local_session.commit()
