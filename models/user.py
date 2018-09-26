from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from models.type import UserType

class User(object):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	email = Column(String(300), nullable=False, unique=True)
	password = Column(String(300), nullable=False)
	is_active = Column(Boolean, nullable=False, default=True)
	user_group_key = Column(String(100), nullable=False, ForeignKey('user_groups.key'))
	first_name = Column(String(100), nullable=False)
	last_name = Column(String(100))

	type = relationship(UserType)
