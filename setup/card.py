from pathlib import Path
from typing import Optional


class Card:
    description: Optional[str] = None
    collection_id: Optional[int] = None
    display: str = 'table'

    def __init__(self, name:str, query:str, database:int = 2) -> None:
        self.name = name
        self.query = query
        self.database = database


    @classmethod
    def from_file(cls, filepath:Path) -> 'Card':
        with filepath.open() as f:
            query = f.read()
        return cls(filepath.stem, query)


    @property
    def payload(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "display": self.display,
            "collection_id": self.collection_id,
            "visualization_settings": {},
            "dataset_query": {
                "type": "native",
                "native": {
                    "query": self.query,
                    "template-tags": {}
                },
                "database": self.database
            },
        }

