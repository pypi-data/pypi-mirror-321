"""
PostgreSQL Module
-----------------

This module is to read and write to PostgreSQL.
"""

import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import aiosql
import psycopg2
from psycopg2 import OperationalError


@dataclass
class DatabaseData:
    """To load and save data to PostgreSQL."""

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
            connection = psycopg2.connect(
                f"{self.connection_string}?application_name={self.application_name}",
            )
            print("Connection to PostgreSQL DB successful")
        except Exception as e:
            print(f"Error {e} occurred.")

        return connection

    def load_queries(self):
        module_path = Path(sys.modules[self.module_name].__path__[0])
        return aiosql.from_path(module_path / self.query_file, "psycopg2")

    def save_json(self) -> None:
        conn = self.create_connection()
        conn.autocommit = True
        queries = self.load_queries()
        try:
            queries.save_json_data(
                conn,
                entry_date=self.entry_date,
                api_call=self.api_call,
                raw_data=self.raw_data,
                software_version=self.software_version,
            )
        except Exception as e:
            print(f"Error {e} occurred.")

    def setup_database(self) -> None:
        conn = self.create_connection()
        queries = self.load_queries()
        try:
            queries.create_weather_schema_postgresql(conn)
            queries.create_raw_json_data_postgresql(conn)
        except Exception as e:
            print(f"Error {e} occurred.")
        conn.commit()
        conn.close()
