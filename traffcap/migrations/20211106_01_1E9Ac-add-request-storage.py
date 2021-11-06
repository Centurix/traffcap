import logging
from yoyo import step
"""
Add request storage
"""


__depends__ = {'20211023_01_xNSB9-baseline-schema'}

def upgrade(connection):
    cursor = connection.cursor()
    logging.info("Creating requests table...")
    cursor.execute("""
CREATE TABLE requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	code TEXT(20) NOT NULL,
	created TEXT(19) NOT NULL,
	modified TEXT(19) NOT NULL,
    scope TEXT NOT NULL,
    body BLOB NULL
)
""")

def downgrade(connection):
    cursor = connection.cursor()
    logging.info("Dropping requests table...")
    cursor.execute("""DROP TABLE requests""")

steps = [
    step(upgrade, downgrade)
]
