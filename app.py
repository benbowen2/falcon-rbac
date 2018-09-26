import falcon

import auth_hook
from views import (
	Authorize,
	Users,
	Notes,
	)

api.application.falcon()

api.add_route('/auth')
api.add_route('/users')
api.add_route('/notes')