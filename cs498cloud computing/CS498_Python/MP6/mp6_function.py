import json
import sys
import logging
import redis
import pymysql


DB_HOST = "database-1.cluster-c5h5eyy3bxdk.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASS = "fWkf0NXH746SsoiV5Kqt"
DB_NAME = "sys"
DB_TABLE = "mp6"
REDIS_URL = "redis://elc-tutorial-2-ro.ynici7.ng.0001.use1.cache.amazonaws.com:6379"

TTL = 10

class DB:
    def __init__(self, **params):
        params.setdefault("charset", "utf8mb4")
        params.setdefault("cursorclass", pymysql.cursors.DictCursor)

        self.mysql = pymysql.connect(**params)

    def query(self, sql):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_idx(self, table_name):
        with self.mysql.cursor() as cursor:
            cursor.execute(f"SELECT MAX(id) as id FROM {table_name}")
            idx = str(cursor.fetchone()['id'] + 1)
            return idx

    def insert(self, idx, data):
        with self.mysql.cursor() as cursor:
            hero = data["hero"]
            power = data["power"]
            name = data["name"]
            xp = data["xp"]
            color = data["color"]
            
            sql = f"INSERT INTO mp6 (`id`, `hero`, `power`, `name`, `xp`, `color`) VALUES ('{idx}', '{hero}', '{power}', '{name}', '{xp}', '{color}')"

            cursor.execute(sql)
            self.mysql.commit()

def read(use_cache, indices, Database, Cache):
    result = []
    for num in indices:
        sql = f"select * from mp6 where id = '{num}'"
        if use_cache:
            if Cache.exists(num):
                result.append(json.loads(Cache.get(num)))
            else:
                d = Database.query(sql)
                if d:
                    result.append(d[0])
                Cache.set(num,json.dumps(d[0]),ex = TTL)
        else:
            d = Database.query(sql)
            if d:
                result.append(d[0])
    return result
    
    
def write(use_cache, sqls, Database, Cache):
    
    if use_cache:
        # write through strategy
        for sql in sqls:
            idx = Database.get_idx(DB_TABLE)
            Database.insert(idx,sql)
            Cache.set(idx, json.dumps(sql))

    else:
        for sql in sqls:
            idx = Database.get_idx(DB_TABLE)
            Database.insert(idx,sql)
    
    return "write success"



def lambda_handler(event, context):
    
    USE_CACHE = (event['USE_CACHE'] == "True")
    REQUEST = event['REQUEST']
    
    # initialize database and cache
    try:
        Database = DB(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
    except pymysql.MySQLError as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(e)
        sys.exit()
        
    Cache = redis.Redis.from_url(REDIS_URL)
    
    result = []
    # if REQUEST == "read":
    #     # event["SQLS"] should be a list of integers
    #     result = read(USE_CACHE, event["SQLS"], Database, Cache)
    # elif REQUEST == "write":
    #     # event["SQLS"] should be a list of jsons
    #     write(USE_CACHE, event["SQLS"], Database, Cache)
    #     result = "write success"
    
    print("test")
    return {
        'statusCode': 200,
        'body': result
    }

try:
    Database = DB(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
    print("Connected")
except pymysql.MySQLError as e:
    print("ERROR: Unexpected error: Could not connect to MySQL instance.")
    print(e)
    sys.exit()
print("test2")