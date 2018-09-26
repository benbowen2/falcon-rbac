from sqlalchemy import Column, Integer, String


class BaseType(object):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    key = Column(String(100), unique=True)
    label = Column(String(100), unique=True)
    description = Column(String(1000))

class UserType(BaseType):
    __tablename__ = 'user_types'

class GroupType(BaseType):
    __tablename__ = 'group_types'