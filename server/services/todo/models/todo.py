from app import db
from pydal import Field

db.define_table('todo', Field('Desc', 'string', required=True), Field('user', 'integer', required=True))
