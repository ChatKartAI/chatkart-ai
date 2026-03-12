import json
import redis
from session_schema import default_session

class ContextManager:
    def __init__(self):
        self.redis = redis.Redis(host="localhost", port=6379,decode_response=True)

    def get_context(self, user_id):
        key = f"session:{user_id}"
        session= self.redist.get(key)
        if session is None:
            session = default_session()
            self.redis.set(key, json.dumps(session))
            return session
        return json.loads(session)
    
    def update_context(self,user_id, session):
        key = f"session:{user_id}"
        self.redis.set(key, json.dumps(session))
