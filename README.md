# pdbsync
configurable db sync tool using python

### demo 

https://github.com/knightliao/pdbsync/tree/master/demo

#### prepare

请确认 本地的 mysql / mysqldump 已经安装.

#### config

    {
        "settings": {
            "basesrc": {
                "host": "127.0.0.1",
                "port": 3306,
                "username": "root",
                "password": "123456"
            },
            "basedest": {
                "host": "127.0.0.1",
                "port": 3306,
                "username": "root",
                "password": "123456"
            }
        },
        "dbs": [
            {
                "src": {
                    "db_name": "disconf"
                },
                "dest": {
                    "db_name": "disconf2",
                    "pre_sql": "sql/disconf2/pre.sql",
                    "after_sql": "sql/disconf2/after.sql"
                }
            },
            {
                "src": {
                    "db_name": "disconf"
                },
                "dest": {
                    "db_name": "disconf3",
                    "after_sql": "sql/disconf3/after.sql"
                }
            }
        ]
    }
    
说明:

- settings.basesrc 是所有 dbs[?].src db 的父类配置, 可被继承
- settings.basedest 是所有 dbs[?].dest db 的父类配置, 可被继承
- dbs[?].dest.pre_sql 是同步前的 SQL 执行文件, 一般在这里进行目标数据库的drop和create
- dbs[?].dest.after_sql 是同步后的 SQL 执行文件, 一般在这里进行关键数据的隐藏
    
#### run 

python demo.py

