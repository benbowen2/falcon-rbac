import falcon

import auth_hook
from views import (
	AuthorizeUser,
	Users,
	Groups
	)

api.application.falcon()

api.add_route('/auth', AuthorizeUser())
# api.add_route('/users')