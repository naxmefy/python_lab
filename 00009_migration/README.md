# 00009_migration

## info

- [see more](https://sqlalchemy-migrate.readthedocs.io/en/latest/versioning.html)
- [warning: consistent behavior](https://sqlalchemy-migrate.readthedocs.io/en/latest/versioning.html#writing-scripts-with-consistent-behavior)

## steps

- `migrate create my_repository "Example project"` (initialize project)
- `python my_repository/manage.py version_control sqlite:///test.db my_repository` (set db under version_control)
- `python my_repository/manage.py db_version sqlite:///project.db my_repository` (db version)
- `python my_repository/manage.py version my_repository` (latest version of repository/project)
- `migrate manage manage.py --repository=my_repository --url=sqlite:///test.db` (project management script - tool)
- `python manage.py db_version` (is possible now)
- `python manage.py script "Add account table"` (adds a new change in versions folder)
- `python manage.py test` (test the script)
- `python manage.py upgrade` (to apply changes)
- `python manage.py downgrade 0 --preview_py` (preview downgrade)
- `python manage.py downgrade 0` (downgrades the database to version 0)
