import os
from flask_script import Manager  # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app import model  # need to be there in order to run migrations


app = create_app(config_name=os.getenv('APP_SETTINGS'))
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    db.create_all()
