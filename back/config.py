import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pharmacy.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
PROPAGATE_EXCEPTIONS = True
