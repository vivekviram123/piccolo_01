"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

import os

from piccolo.conf.apps import AppConfig, table_finder
from .tables import QuestionHead,Questions,Answers,AddUser

from legal.commands.load_data import load_data

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="legal",
    migrations_folder_path=os.path.join(CURRENT_DIRECTORY, "piccolo_migrations"),
    table_classes=[QuestionHead,Questions,Answers,AddUser],
    migration_dependencies=[],
    commands=[load_data],
)
