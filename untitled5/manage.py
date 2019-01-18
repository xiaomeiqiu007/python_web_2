# coding: utf-8
# auth:小煤球

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from untitled5 import app
from exts import db
from  models import User,Question,Answer


# 模型 --》 迁移文件  --》表
# 建立模型：manage.py db init :初识化迁移脚本所需要的环境，只需要执行一次
# 生成迁移文件：manage.py db migrate :生成迁移脚本忙（会生成一个versions文件夹）
# 映射到表：manage.py db upgrate ：将迁移文件映射到表

#另外需要注意将数据模型导入

#  1.要使用flask_migrate,必须绑定qpp和db,绑定的db以及app必须是同一个
#  2. 把MigrateCommand命令添加到manager中
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()