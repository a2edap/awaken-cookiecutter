import os
from .pipeline import (
    Pipeline,
    pipeline,
    {{ if cookiecutter.use_custom_filehandler == "y" }}filehandler,{{ endif }}
    {{ if cookiecutter.use_custom_qc != "n" }}qc,{{ endif }}
)
from .mapping import mapping


def _expand_path(rel_filepath: str) -> str:
    parent = os.path.dirname(__file__)
    path = os.path.join(parent, rel_filepath)
    return os.path.abspath(path)

MODULE_NAME = "{{ cookiecutter.ingest_slug }}"

PIPELINE_CONFIG_{{ cookiecutter.location_slug.upper() }} = _expand_path("config/pipeline_config_{{ cookiecutter.location_slug }}.yml")
STORAGE_CONFIG = _expand_path("config/storage_config.yml")

DATA_FILE_{{ cookiecutter.location_slug.upper() }} = _expand_path("data/{{ cookiecutter.location_slug }}/data.txt")