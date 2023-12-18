import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


class MongoDBClient:

    def __init__(self):
        mongo_uri = f"mongodb://{self.get_user()}:{self.get_password()}@{self.get_host()}:{self.get_port()}"
        self.client = MongoClient(mongo_uri)
        self.db = self.client.get_database(self.get_db_name())

        self.collection = self.db.get_collection(
            self.get_collection_name()
        )

    def get_user(self) -> str:
        return os.getenv("MONGO_DB_USERNAME", "root")

    def get_password(self) -> str:
        return os.getenv("MONGO_DB_PASSWORD", "root")

    def get_host(self) -> str:
        return os.getenv("MONGO_DB_HOST", "localhost")

    def get_port(self) -> int:
        return int(os.getenv("MONGO_DB_PORT", "27017"))

    def get_db_name(self) -> str:
        return os.getenv("MONGO_DB_DB", "db")

    def get_collection_name(self) -> str:
        return os.getenv("MONGO_DB_TABLE", "table")

    def get_collection(self):
        return self.collection

    def get_client(self):
        return self.client

    def get_db(self):
        return self.db
