from repo.db import SessionLocal,Base,engine
from models.users_models import Users
import bcrypt

Base.metadata.create_all(bind=engine)

password = "Your password here"

hash_passsword = bcrypt.hashpw(password.encode(),bcrypt.gensalt())

with SessionLocal() as db:
    admin = Users(
        user_id = "Your id here",
        user_name = "Your name here",
        user_email = "Your mail here",
        user_password = hash_passsword,
        role = "admin",
        is_active = "true"
    )
    db.add(admin)
    db.commit()
    print("Admin Created")
    print("Email : your email")
    print("password : your password")