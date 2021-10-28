import os
import xarray as xr
from utils import expand, set_dev_env
from ingest.{{ cookiecutter.ingest_slug }} import Pipeline

parent = os.path.dirname(__file__)


# TODO – Developer: Update paths to your input files here. Please add tests if needed.
def test_pipeline_at_sgp():
    set_dev_env()
    pipeline = Pipeline(
        expand("config/pipeline_config_{{ cookiecutter.location_slug }}.yml", parent),
        expand("config/storage_config.yml", parent),
    )
    output = pipeline.run(expand("tests/data/input/data.txt"))
    expected = xr.open_dataset(expand("tests/data/expected/data.txt"))

    assert output.equals(expected)
