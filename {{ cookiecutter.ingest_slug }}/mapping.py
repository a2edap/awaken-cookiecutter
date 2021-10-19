import re

from typing import AnyStr, Dict
from utils import IngestSpec
from . import Pipeline


mapping: Dict["AnyStr@compile", IngestSpec] = {
    re.compile("YOUR-REGEX-HERE"): IngestSpec(
        pipeline=Pipeline,
        pipeline_config="config/pipeline_config_{{ cookiecutter.location_slug }}.yml",
        storage_config="config/storage_config.yml",
        name="awaken_buoy_ingest",
    ),
    # Add another regex: IngestSpec entry if you would like to reuse this ingest
}
