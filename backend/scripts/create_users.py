from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.db import Base
from backend.db.models import User as UserModel
from backend.db.session import get_db_url


def create_demo_user():
    db_url = get_db_url()

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)

    session = Session()

    user1 = UserModel(1, 'tina@centria.fi', '1234', 'user')
    user2 = UserModel(2, 'admin@hda.com', '1234', 'admin')

    existing_users = session.query(UserModel).filter(UserModel.username.in_(["tina@centria.fi", "admin@hda.com"])).all()
    if len(existing_users) == 2:
        print("Users already exists")
    else:
        session.add(user1)
        session.add(user2)
        session.commit()
        print("Users created")
    session.close()
