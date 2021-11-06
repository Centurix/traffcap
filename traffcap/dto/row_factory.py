class RowFactory:
    @classmethod
    def row_factory(cls, cursor, row):
        """
        Provide a row factory for pydantic
        """
        data = {}
        for index, column in enumerate(cursor.description):
            if row[index]:
                data[column[0]] = row[index]
        return cls(**data)
