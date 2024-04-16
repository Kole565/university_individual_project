class RentModel:

    TABLE_NAME = "rents"

    def __init__(self, rooms_ids, clients_ids, transaction_id, since, due):
        self._rooms_ids = rooms_ids
        self._clients_ids = clients_ids
        self._transaction_id = transaction_id

        self._since = since
        self._due = due
        self._duration = self._due - self._since

    @staticmethod
    def from_table(id, rooms_ids, clients_ids, since, due, transaction_id=0):
        return RentModel(rooms_ids=rooms_ids, clients_ids=clients_ids, transaction_id=transaction_id, since=since, due=due)

    @property
    def rooms_ids(self):
        return self._rooms_ids

    @rooms_ids.setter
    def rooms_ids(self, value):
        self._rooms_ids = value

    @property
    def clients_ids(self):
        return self._clients_ids

    @clients_ids.setter
    def clients_ids(self, value):
        self._clients_ids = value

    @property
    def transaction_id(self):
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, value):
        self._transaction_id = value

    @property
    def since(self):
        return self._since

    @since.setter
    def since(self, value):
        self._since = value

    @property
    def due(self):
        return self._due

    @due.setter
    def due(self, value):
        self._due = value

    @property
    def duration(self):
        return self._duration

    def save(self, db):
        db.connect()

        db.execute(self._get_save_query(), self._get_save_arguments())
        db.commit()

        db.disconnect()

    def _get_save_query(self):
        query = "INSERT INTO {} (room_id, transaction_id, since, due) VALUES (%s, %s, %s, %s)".format(self.TABLE_NAME)

        return query

    def _get_save_arguments(self):
        return self._rooms_ids, self._transaction_id, self._since, self._due