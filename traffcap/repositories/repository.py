import os
from typing import (
    Any,
    Iterable
)
import logging
import aiosqlite
from traffcap.dto import RowFactory
from yoyo import (
    read_migrations,
    get_backend
)


class Repository:
    db_path: str = ""

    @classmethod
    async def upgrade_db(cls) -> None:
        """
        Upgrade migrations. Downgrades should be performed using yoyo
        """
        logging.info(f"Checking and migrating {cls.db_path!r}...")
        backend = get_backend(cls.db_path)
        migrations = read_migrations(os.path.join("traffcap", "migrations"))
        with backend.lock():
            backend.apply_migrations(backend.to_apply(migrations))

    @classmethod
    async def execute(
        cls,
        sql: str,
        parameters: Iterable[Any] = None,
        row_factory: RowFactory=None
    ) -> Any:
        results = []
        async with aiosqlite.connect(
            cls.db_path.replace("sqlite:///", ""),
            isolation_level=None
        ) as db:
            db.row_factory = aiosqlite.Row
            if row_factory:
                db.row_factory = row_factory.row_factory

            async with db.execute(sql, parameters) as cursor:
                results = await cursor.fetchall()

        return results
