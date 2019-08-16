import mysql.connector.pooling

#数据库配置
__config = {
    "host":"localhost",
    "port":"3306",
    "user":"root",
    "password":"123456",
    "database":"gc"
}

#数据库连接池
try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size = 10
    )
except Exception as e:
    print(e)