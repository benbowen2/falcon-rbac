import falcon
import jwt
from datetime import datetime, timedelta
import json

from auth_hook import AvailablePermissions, PermissionRoles, PermissionGroups

from models.user import User

from settings import jwt_secret_key



def returnUnAuthorized():
	raise falcon.HTTPUnauthorized(
		title="Incorrect Login",
		description="The username or password are not correct."
	)

def create_scope(user_type, company_type):
    roles = PermissionGroups[company_type][user_type]
    scope = 0
    for role in roles:
        for permission in PermissionRoles[role]:
            scope += AvailablePermissions[permission]
    return int(scope)


class Authorize(object):
	def on_post(self, req, resp):
		body = json.loads(req.stream.read())

        # Important to note that the password is plain text. The FE service should hash the password before its sent.
        if body['email'] and body['password']:
            user = self.session.query(User). \
                filter(User.email == body['email']). \
                filter(User.is_active).first()
        else:
            returnUnAuthorized()

        if  user and user.password == body['password']:
            payload = {
                'user_id': user.id,
                'scope': create_scope(user.group.key, user.company.company_type.key),
                'exp': datetime.utcnow() + timedelta(days=10)
            }
            token = jwt.encode(payload, jwt_secret_key)
        else:
            returnUnAuthorized()

        response = {
        	'token': token.decode('ASCII')
        	'user':serialize(user, UserSchema, exclude=['password'])
        }

        resp.body = json.dumps(response)		