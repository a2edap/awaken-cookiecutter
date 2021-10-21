import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def copy_file(filepath, target):
    shutil.copy(filepath, os.path.join(PROJECT_DIRECTORY, target))


if __name__ == "__main__":

    if "{{ cookiecutter.use_custom_filehandler }}" in ["n", "N", "no", "No"]:
        remove_file("pipeline/filehandler.py")

    if "{{ cookiecutter.use_custom_qc }}" in ["n", "N", "no", "No"]:
        remove_file("pipeline/qc.py")
