from .pipeline import (
    Pipeline,
    pipeline,
    {% if cookiecutter.use_custom_filehandler == "y" %}filehandler,{% endif %}
    {% if cookiecutter.use_custom_qc != "n" %}qc,{% endif %}
)
from .mapping import mapping