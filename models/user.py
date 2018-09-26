from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils import PasswordType

from models.type import UserType

class User(object):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(300), nullable=False, unique=True)
    password = Column(PasswordType, nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    user_group_key = Column(String(100), ForeignKey('user_groups.key'), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))

    type = relationship(UserType)
