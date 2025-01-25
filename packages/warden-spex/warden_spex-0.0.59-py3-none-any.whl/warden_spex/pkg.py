from importlib.metadata import version
from pathlib import Path

project_path = Path(__file__).parent.parent.parent.absolute()
project_dir = str(project_path)
project_name = project_path.name


def pkg_version():
    return version(project_name)
