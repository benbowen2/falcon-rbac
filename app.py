import falcon

from views.authorize import AuthorizeUser

api.application.falcon()

api.add_route('/auth', AuthorizeUser())
