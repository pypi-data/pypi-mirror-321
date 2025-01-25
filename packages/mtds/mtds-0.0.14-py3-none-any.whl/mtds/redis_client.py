import json
import math
import os
from numbers import Number

import redis
from redis.exceptions import AuthenticationError
from redis.exceptions import ConnectionError

from mtds.common.errors import EnvironmentVariableNotFoundError
from mtds.common.errors import WrongProgressTypeError


class RedisClient:
    def __init__(self, redis_url):
        self.r = redis.StrictRedis.from_url(redis_url)

        try:
            self.r.ping()
        except AuthenticationError:
            raise Exception('Redis authentication failed')
        except ConnectionError as e:
            raise Exception(f'Redis connection failed, {e}')
        except Exception as e:
            raise Exception(f'Redis error {e}')

    @classmethod
    def create_from_env(cls):
        redis_url = os.environ.get('REDIS_URL') or os.environ.get('redis_url')

        if not redis_url:
            raise ValueError('REDIS_URL or redis_url environment variable not found')
        return cls(redis_url)

    def refresh_progress(self, task_id, progress):
        if not isinstance(progress, int) or not (0 <= progress <= 100):
            raise WrongProgressTypeError()

        self.r.hset(f'model_status:{task_id}', 'progress', progress)

    def get_progress(self, task_id):
        progress = self.r.hget(f'model_status:{task_id}', 'progress')
        return int(progress) or -1
