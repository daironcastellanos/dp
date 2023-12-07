class InMemoryDB:
    def __init__(self):
        self.main_store = {}
        self.transaction_store = None

    def get(self, key):
        if self.transaction_store is not None and key in self.transaction_store:
            return self.transaction_store[key]
        return self.main_store.get(key, None)

    def put(self, key, val):
        if self.transaction_store is None:
            raise Exception("No transaction in progress")
        self.transaction_store[key] = val

    def begin_transaction(self):
        if self.transaction_store is not None:
            raise Exception("Transaction already in progress")
        self.transaction_store = {}

    def commit(self):
        if self.transaction_store is None:
            raise Exception("No transaction to commit")
        self.main_store.update(self.transaction_store)
        self.transaction_store = None

    def rollback(self):
        if self.transaction_store is None:
            raise Exception("No transaction to rollback")
        self.transaction_store = None


# Example usage
if __name__ == "__main__":
    db = InMemoryDB()

    # Demonstration of functionality
    print(db.get("A"))  # Should return None

    try:
        db.put("A", 5)  # Should raise an error
    except Exception as e:
        print(e)

    db.begin_transaction()
    db.put("A", 5)
    print(db.get("A"))  # Should return None as transaction is not committed
    db.put("A", 6)
    db.commit()
    print(db.get("A"))  # Should return 6
