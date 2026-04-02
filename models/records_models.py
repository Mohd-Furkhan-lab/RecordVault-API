from repo.db import SessionLocal,base
from sqlalchemy import Column,String,Integer,DateTime

class Records(base):
    __tablename__ = "records"
    record_id=Column(Integer,primary_key=True,autoincrement=True)
    record_type=Column(String,nullable=False)
    category=Column(String,nullable=False)
    amount=Column(Integer,nullable=False)
    create_date=Column(DateTime,nullable=False)
    description=Column(String)


def  get_records(role_auth,type,category):
    if role_auth:
        with SessionLocal() as db:
            if type is not None and category is None:
                data=db.query(Records).filter(Records.record_type == type).all()
                return data
            elif type is  None and category is not None:
                data=db.query(Records).filter(Records.category == category).all()
                return data
            elif type is not None and category is not None:
                data=db.query(Records).filter(Records.record_type == type , Records.category == category).all()
                return data
            data=db.query(Records).all()

def add_records(role_auth,type,category,amount,datetime,description):
    if role_auth:
        with SessionLocal() as db:
            record=Records(
                record_type = type,
                category=category,
                amount = amount,
                create_date = datetime,
                description = description
            )
        db.add(record)
        db.commit()

def update_records(role_auth,record_id,record_type,record_)