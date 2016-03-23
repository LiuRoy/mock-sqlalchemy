# -*- coding=utf8 -*-

import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from session import MockSession, create_table, drop_table

BaseModel = declarative_base()


class User(BaseModel):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    created_at = Column(DateTime, default=datetime.datetime.now)


if __name__ == '__main__':

    create_table(User)

    # add data
    session = MockSession()
    session.add(User(name='1'))
    session.add(User(name='2'))
    session.add(User(name='2'))
    session.commit()

    # query data
    session = MockSession()
    result = session.query(User).filter(User.name == '2').all()
    session.commit()

    for record in result:
        print 'id:{} name:{} created_at:{}'.format(record.id,
                                                   record.name,
                                                   str(record.created_at))
    drop_table(User)