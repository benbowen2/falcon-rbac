class HealthCheck(object):
	def on_get(self, req, resp):
		resp.body = '["success"]'