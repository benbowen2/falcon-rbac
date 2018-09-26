from settings import session

class SQLAlchemySessionManager:

    def __init__(self):
        self.session = session

    def process_resource(self, req, resp, resource, params):
        resource.session = self.session

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'session'):
            self.session.close()