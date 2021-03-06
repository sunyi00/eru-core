#!/usr/bin/python
#coding:utf-8

DEBUG = False
ERU_BIND = '0.0.0.0:46656'
ERU_WORKERS = 4
ERU_TIMEOUT = 300
ERU_WORKER_CLASS = 'gevent'

DOCKER_REGISTRY = 'docker-registry.intra.hunantv.com'
DOCKER_NETWORK = 'bridge'

GIT_ENDPOINT = 'http://git.hunantv.com'
GIT_WORK_DIR = '/tmp'
GIT_EXTEND_DIR = '/mnt/sda1/tmp/extend'

LOGSTASH = [
    'udp://10.100.1.154:50433',
]

ETCD_SYNC = True
ETCD_MACHINES = (
    ('10.1.201.110', 4001),
    ('10.1.201.110', 4002),
)

INFLUXDB_HOST = '10.1.201.42'
INFLUXDB_PORT = 8086
INFLUXDB_USERNAME = 'root'
INFLUXDB_PASSWORD = 'root'
INFLUXDB_DATABASE = 'test'

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DATABASE = 'eru'

SQLALCHEMY_POOL_SIZE = 100
SQLALCHEMY_POOL_TIMEOUT = 10
SQLALCHEMY_POOL_RECYCLE = 2000

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_POOL_SIZE = 100

REPORT_INTERVAL = 10
CLEAN_NITERVAL = 86400
CLEAN_DIR = '/var/lib/docker/containers'

PUBLIC_HOST_LIMIT = 20

PORT_START = 49000
PORT_RANGE = 2

# Celery Settings
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
CELERY_REDIS_MAX_CONNECTIONS = 1024
# NOT REMOVE
CELERY_TASK_RESULT_EXPIRES = 86400*7
CELERY_TRACK_STARTED = True
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = 'Asia/Chongqing'

CELERY_SEND_TASK_ERROR_EMAILS = True

# Name and email addresses of recipients
ADMINS = (
    ('CMGS', 'ilskdw@gmail.com'),
)

# Email address used as sender (From field).
SERVER_EMAIL = 'gitlab@gitup.me'

# Mailserver configuration
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'gitlab@gitup.me'
EMAIL_HOST_PASSWORD = '^123$456a'
EMAIL_USE_SSL = True

NBE_HOST_PERMDIR = '/mnt/mfs/permdir/%s'
NBE_CONTAINER_PERMDIR = '/%s/permdir'

try:
    from local_settings import *
except ImportError:
    pass

# 需要计算的变量需要在 import 覆盖之后计算.
SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(MYSQL_USER,
        MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE)
