from os.path import abspath, dirname, join
from requests import Session
from loguru import logger
from environs import Env
import argparse
import sys

env = Env()

# redis 配置
REDIS_HOST = env.str('REDIS_HOST', '127.0.0.1')
REDIS_PORT = env.int('REDIS_HOST', 6379)
REDIS_PASSWORD = env.str('REDIS_PASSWORD', '123456')
REDIS_KEY = env.str('REDIS_KEY', 'Taobao')

# mysql 配置
MYSQL_HOST = env.str('MYSQL_HOST', '127.0.0.1')
MYSQL_PORT = env.int('MYSQL_PORT', 3306)
MYSQL_USER = env.str('MYSQL_USER', 'root')
MYSQL_PASSWORD = env.str('MYSQL_PASSWORD', '123456')
MYSQL_DATABASE = env.str('MYSQL_DATABASE', 'rb-school')

