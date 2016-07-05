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
    
#### run 

python demo.py

