import falcon

from middleware.sessionMiddleware import SQLAlchemySessionManager

from views.authView import AuthorizeUser
from views.healthView import HealthCheck

api = falcon.API(middleware=[
	SQLAlchemySessionManager()
])

api.add_route('/auth', AuthorizeUser())
api.add_route('/health', HealthCheck())
