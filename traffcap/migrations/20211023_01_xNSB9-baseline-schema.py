import logging
from yoyo import step
"""
Baseline schema
"""


__depends__: dict = {}


def upgrade(connection):
    cursor = connection.cursor()
    logging.info("Creating endpoints table...")
    cursor.execute("""
CREATE TABLE endpoints (
	code TEXT(20) PRIMARY KEY NOT NULL,
	created TEXT(19) NOT NULL,
	modified TEXT(19) NOT NULL,
	description TEXT(256)
)
""")

def downgrade(connection):
    cursor = connection.cursor()
    logging.info("Dropping endpoints table...")
    cursor.execute("""DROP TABLE endpoints""")

steps = [
    step(upgrade, downgrade)
]
