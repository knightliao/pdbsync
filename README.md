# pdbsync
configurable db sync tool using python

                     .o8   .o8
                    "888  "888
    oo.ooooo.   .oooo888   888oooo.   .oooo.o oooo    ooo ooo. .oo.    .ooooo.
     888' `88b d88' `888   d88' `88b d88(  "8  `88.  .8'  `888P"Y88b  d88' `"Y8
     888   888 888   888   888   888 `"Y88b.    `88..8'    888   888  888
     888   888 888   888   888   888 o.  )88b    `888'     888   888  888   .o8
     888bod8P' `Y8bod88P"  `Y8bod8P' 8""888P'     .8'     o888o o888o `Y8bod8P'
     888                                      .o..P'
    o888o                                     `Y8P'
    
### install

version: 0.0.6

pip install pdbsync

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
- dbs[?].dest.after_sql 是同步后的 SQL 执行文件, 一般在这里进行关键数据的隐藏
    
#### run 

pdbsync

or 

pdbsync -d

