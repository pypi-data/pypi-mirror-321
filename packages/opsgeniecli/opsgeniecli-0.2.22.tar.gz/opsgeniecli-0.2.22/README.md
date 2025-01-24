# Opsgeniecli

A cli for Opsgenie

## TODO:
- add python version - setuptools-scm
- try uploading new package to pypi using uv
- validate if `opsgeniecli alerts list --team-name saas --not-filtered --last 7d` still fails after
- install opsgeniecli via uv?
- add tests for alerts 


# TODO: create a function to create a config
# TODO: check if the config provided is a valid path
# @click-option("--notes_directory", "-n", type=click.Path(exists=True))
# why does '/Users/yhoorneman/.local/bin/uv run pytest tests ' work, but 'uv run pytest tests' not?