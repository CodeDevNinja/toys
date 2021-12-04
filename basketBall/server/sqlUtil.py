from sqlalchemy import bindparam
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()
engine = None


class sqlUtil:
    def __init__(self, dburl):
        global engine
        engine = create_engine(dburl, echo=True)
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def bulk_insert(self, datas):
        session = Session(bind=engine)
        session.bulk_save_objects(datas)
        session.commit()

    def query(self,model,condation):
        session = Session(bind=engine)
        return session.query(model).filter(condation).all()

    def update(self, model, condation, update_dic):
        session = Session(bind=engine)
        session.query(model).filter(condation).update(update_dic)
        session.commit()


if __name__ == '__main__':
    main()
    