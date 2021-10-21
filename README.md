# AWAKEN Ingest Template

This cookiecutter template is intended to be used in conjunction with the 
[ingest-awaken](https://github.com/a2edap/ingest-awaken) repository.

To use it, make sure you have `cookiecutter` installed
```
pip install cookiecutter
```

Then run the following command from the top-level directory of the ingest awaken
repository:
```
cookiecutter https://github.com/a2edap/awaken-cookiecutter -o ingest/
```

This will bring up a commandline interface which will go through some options. Consult
the documentation below for more information regarding these prompts.


| Field                    | Default               | Description                                                                                                                         |
|--------------------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `author`                 | `First Last`          | Main author of this ingest.                                                                                                         |
| `email`                  |                       | Contact email of the author.                                                                                                        |
| `ingest`                 | `Ingest Name`         | Verbose name of the ingest. Used in the README.md                                                                                   |
| `ingest_slug`            | `ingest_name`         | Name used for the ingest module. Lowercase alphanumeric and '_' characters allowed.                                                 |
| `description`            | `description`         | A brief description of the ingest. Used in README.md                                                                                |
| `location`               | `Location`            | The verbose location                                                                                                                |
| `location_slug`          | `location`            | Location used to name files and attributes. Lowercase alphanumeric and '_' characters allowed.                                      |
| `use_custom_filehandler` | `yes`                 | Flag to generate a custom FileHandler template. Use this if data cannot be read in using out-of-box FileHandlers provided by tsdat. |
| `use_custom_qc`          | `yes`                 | Flag to generate a custom QC template module. Use this if you want to apply custom quality checks or handlers.                      |

