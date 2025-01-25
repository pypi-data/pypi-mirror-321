# pylint: disable=invalid-name
"""
Decorator module for Robotframework Relukko to skip the real locking.
"""
import os
from datetime import datetime
from functools import wraps

SKIP_RELUKKO = {
    "id": "00000000-0000-0000-0000-000000000000",
    "lock_name": "WE TRUST YOU",
    "creator": "Dummy Dummy",
    "ip": "0.0.0.0",
    "expires_at": "1970-01-01T00:00:00Z",
    "created_at": "1970-01-01T00:00:00Z",
    "updated_at": "1970-01-01T00:00:00Z"
}


def trust_me_i_know_what_i_do():
    """
    Decorator for Robotframework Relukko methods.

    It skips the actual method if the environment variable
    `RELUKKO_TRUST_ME_IT_IS_LOCKED` is set and returns instead a static lock
    dictionary or it's expire time (1970-01-01T00:00:00z).
    """
    def deco_skip(f):

        @wraps(f)
        def f_skip(*args, **kwargs):
            if os.environ.get('RELUKKO_TRUST_ME_IT_IS_LOCKED'):
                if f.__name__ == "get_relukko_expires_at_time":
                    return datetime.fromisoformat(SKIP_RELUKKO["expires_at"])
                return SKIP_RELUKKO
            return f(*args, **kwargs)
        return f_skip  # true decorator
    return deco_skip
