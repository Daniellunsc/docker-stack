from user import db
from pydal import Field

db.define_table('users',
     Field('username', 'string', required=True), Field('password', 'string', required=True))
