"""
DuckDB Module
-------------

This module is to read and write to DuckDB.
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import aiosql
import duckdb


@dataclass
class DatabaseData:
    """To load and save data to DuckDB."""

    connection_string: str
    entry_date: datetime
    api_call: str
    raw_data: str
    software_version: str
    query_file: str
    module_name: str
    application_name: str = "python_program"

    def create_connection(self):
        connection = None
        try:
            connection = duckdb.connect(
                f"{self.connection_string}",
            )
            print("Connection to DuckDB successful")
        except Exception as e:
            print(f"Error {e} occurred.")

        return connection

    def load_queries(self):
        module_path = Path(sys.modules[self.module_name].__path__[0])
        return aiosql.from_path(module_path / self.query_file, "duckdb")

    def save_json(self) -> None:
        conn = self.create_connection()
        queries = self.load_queries()
        try:
            queries.save_json_data_no_schema(
                conn,
                entry_date=self.entry_date,
                api_call=self.api_call,
                raw_data=self.raw_data,
                software_version=self.software_version,
            )
            print("Data saved.")
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error {e} occurred.")

    def setup_database(self) -> None:
        conn = self.create_connection()
        queries = self.load_queries()
        try:
            queries.create_raw_json_data_duckdb(conn)
        except Exception as e:
            print(f"Error {e} occurred.")
        conn.commit()
        conn.close()
