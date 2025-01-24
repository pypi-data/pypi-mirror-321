# nunininu-check-os-ver
 - Detects and outputs the os version. 
 
### Development environment setting
```bash
$ install pdm
$ git clone

# pdm venv create (at different delvelopment environment)
$ source .venv/bin/activate
$ pdm install
$ vi ...(coding)

# TEST
$ pdm install
$ pdm test
$ pip install

$ git add <file_name>
$ git commit -a
$ git push
$ pdm publish
Username: __token__
# PR - Merge
# Tag - Release
```

### Test
 - https://docs.pytest.org/en/stable/
```bash
# $ pdm add -dG test pytest pytest-cov
$ pytest
$ pytest -s
$ pytest --cov
```

### USE
``` 
$ pip install nunininu-check-os-ver
$ python
>>> from nunininu_check_os_ver.hi import hi
>>> hi()
```

### REF
```
- https://pdm-project.org/en/latest/
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
- [console_scripts](https://packaging.python.org/en/latest/specifications/entry-points/#entry-points-specification)
```
