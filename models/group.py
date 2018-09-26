from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from models.type import GroupType

class Group(object):
	__tablename__ = 'groups'

	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	group_type_key = Column(String, nullable=False, ForeignKey('group_types.key'))
	is_active = Column(String, nullable=False, defualt=True)

	type = relationship(GroupType)
