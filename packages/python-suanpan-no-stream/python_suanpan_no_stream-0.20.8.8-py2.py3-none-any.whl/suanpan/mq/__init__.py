# coding=utf-8
from __future__ import absolute_import, print_function

import itertools

from suanpan.arguments import Bool, Float, Int, String
from suanpan.mq import redis
from suanpan.proxy import Proxy


class MQProxy(Proxy):
    MAPPING = {"redis": redis.MQ}
    DEFAULT_ARGUMENTS = [String("mq-type", default="redis")]
    REDIS_ARGUMENTS = [
        String("mq-redis-host", default="localhost"),
        Int("mq-redis-port", default=6379),
        Bool("mq-redis-realtime", default=False),
        Bool("mq-redis-keepalive", default=True),
        String("mq-redis-password", default=""),
        # Int("mq-redis-keepalive-idle", default=120),
        # Int("mq-redis-keepalive-cnt", default=2),
        # Int("mq-redis-keepalive-intvl", default=30),
        Float("mq-redis-socket-connect-timeout", default=1),
        String("mq-redis-unix-socket-path"),
        Bool("__p2p_stream", default=False),
    ]
    ARGUMENTS = list(itertools.chain(DEFAULT_ARGUMENTS, REDIS_ARGUMENTS))


mq = MQProxy()
