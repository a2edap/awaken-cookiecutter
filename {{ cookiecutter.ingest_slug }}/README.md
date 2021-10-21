# {{ cookiecutter.ingest }}

{{ cookiecutter.description}}

Writen by [{{ cookiecutter.author }}](mailto:{{ cookiecutter.email }})

## Getting started

1. Ensure that your development environment is set up according to 
[a2edap/ingest-awaken](https://github.com/a2edap/ingest-awaken).

2. Use the `TODO-Tree` VS Code extension or use the search tool to find occurances of
"`# TODO – Developer:`". Each instance of this requires your attention. Attend to all
of these TODOs and remove the "`TODO – Developer:`" text as you do so.

3. As you are developing, try to follow best practices to save yourself (and others)
time:
    - Commit your changes early, and make commits after each significant change.
    - Tests should be written as soon as possible, and you should test your code often.
    - Try to write clean and readable code that can be reused by others.
    - Document complexities such that future you and readers of this code understand
    what it is that you are doing.

4. You can run your code locally in VS Code by running the tests, or by 
running/debugging the `runner.py` script at the same level as this `README.md` file.

5. When you have finished the ingest script your tests should pass, the code should be
formatted by `black`, there should be no `flake8` warnings (Use "`# noqa`" to disable
a specific line, if need be), and this `README.md` file should be totally re-written to
describe your ingest pipeline to end-users, project maintainers, and curious onlookers
who may not be familiar with your work. If this has all been completed, then sync your
local changes with your remote fork of `a2edap/ingest-awaken` and submit a pull request
with the `master` branch so that your changes can be reviewed and merged into
production.   
