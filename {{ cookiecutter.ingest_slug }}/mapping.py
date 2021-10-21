import re

from typing import AnyStr, Dict
from utils import IngestSpec
from . import Pipeline

# TODO – Developer: Update the regex patterns to match files that should trigger your
# ingest pipeline. See http://www.pyregex.com for help setting up a regex pattern. Note
# that the full filepath will be passed to the compiled regex pattern, so you can
# optionally match the directories as well as the file name.
mapping: Dict["AnyStr@compile", IngestSpec] = {
    # Mapping for Raw Data -> Ingest
    re.compile("YOUR-REGEX-HERE"): IngestSpec(
        pipeline=Pipeline,
        pipeline_config="config/pipeline_config_{{ cookiecutter.location_slug }}.yml",
        storage_config="config/storage_config.yml",
        name="awaken_buoy_ingest",
    ),
    # Mapping for Processed Data -> Ingest (so we can reprocess plots)
    re.compile("YOUR-REGEX-HERE"): IngestSpec(
        pipeline=Pipeline,
        pipeline_config="config/pipeline_config_{{ cookiecutter.location_slug }}.yml",
        storage_config="config/storage_config.yml",
        name="plot_awaken_buoy_ingest",
    ),
    # You can add as many {regex: IngestSpec} entries as you would like. This is useful
    # if you would like to reuse this ingest at other locations or possibly for other
    # similar instruments
}
