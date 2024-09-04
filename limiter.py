from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(key_func=get_remote_address, default_limits=["500 per day", "3 per second"]) #instantiating our Limiter object
