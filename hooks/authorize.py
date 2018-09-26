import falcon
import jwt

from settings import jwt_secret_key

AvailablePermissions = {
    "allowAPI": 1,
    "canViewAllGroups":2,
    "canModifyGroup":4,
    "canDeleteGroup":8,
    "canViewAllUsers":16,
    "canModifyUser":32,
    "canDeleteUser":64
}

PermissionRoles = {
    "is_bronze_user":[
        "allowAPI",
    ],
    "is_bronze_admin":[

    ],
    "is_silver_user":[
        "canViewAllGroups",
        "canViewAllUsers",
    ],
    "is_silver_admin":[

    ],
    "is_gold_user":[
        "canModifyGroup",
        "canDeleteGroup",
        "canModifyUser",
        "canDeleteUser",
    ],
    "is_gold_admin":[

    ]
}

PermissionGroups = {
    'bronze': {
        'user': [
            'is_bronze_user'
        ],
        'admin': [
            'is_silver_user'
            'is_silver_admin'
        ]
    },
    'silver': {
        'user': [
            'is_bronze_user',
            'is_silver_user'
        ],
        'admin': [
            'is_bronze_user',
            'is_silver_user',
            'is_silver_admin',
        ]
    },
    'gold': {
        'user': [
            'is_bronze_user',
            'is_silver_user',
            'is_gold_user',
        ],
        'admin': [
            'is_bronze_user',
            'is_silver_user',
            'is_gold_user',
            'is_gold_admin'
        ]
    }
}


class Authorize(object):
    def __init__(self, permissions):
        self.permissions = permissions

    def __call__(self, req, resp, resource, params):
        self.resource = resource

        if not self._checkAuth(req):
            raise falcon.HTTPUnauthorized(
                'Permission Denied',
                'You must construct additional pylons.')

    def _checkAuth(self, req):
        # check for valid jwt token
        if hasattr(req, 'auth') and req.auth:
            token = self.token_is_valid(req.auth.replace("Bearer ", ""))
        else:
            raise falcon.HTTPUnauthorized(
                'No Token Given',
                'No Token was given in header'
            )

        self.resource.current_user_id = token['user_id']
        # check permission
        for p in self.permissions:
            print(f'{token["user_id"]} --- {p}')
            if AvailablePermissions[p] & token['scope']:
                continue
            else:
                print(f'User {token["user_id"]} --- Failed on -> {p}')
                return False
        return True

    @staticmethod
    def token_is_valid(encoded_token):
        try:
            token = jwt.decode(encoded_token, jwt_secret_key, algorithms=['HS256'])
        except jwt.InvalidTokenError:
            raise falcon.HTTPUnauthorized(
                'Invalid Token',
                'The Token is invalid or expired.')

        return token
