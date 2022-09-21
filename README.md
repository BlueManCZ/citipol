# Citipol

### Entities

TODO

### DEV Scripts

Codebase should follow our pylint and mypy rules.

#### Pylint
```shell
pylint $(pwd) -v
```

#### Mypy
```shell
mypy . --explicit-package-bases --namespace-packages
```