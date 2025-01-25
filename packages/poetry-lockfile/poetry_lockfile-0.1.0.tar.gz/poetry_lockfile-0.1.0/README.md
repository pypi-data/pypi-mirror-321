# Poetry lock

The `poetry lock` command manages the lock file (`poetry.lock`) for a Poetry project.

The `poetry lock` command in the [Poetry](https://python-poetry.org/) dependency management tool is used to lock your project dependencies and ensure consistent environments across different systems. It creates or updates the `poetry.lock` file, which specifies the exact versions of all dependencies (including transitive ones) used in the project.

This file ensures consistent dependency versions across installations, making it a critical part of dependency management.

## 1. poetry.lock file

- **`poetry.lock`** : Tracks the exact versions of dependencies resolved during installation, ensuring reproducible environments.
- It is automatically generated/updated when you run commands like `poetry install` or `poetry update`.

If you have never run the command before and there is also no `poetry.lock` file present, Poetry simply
resolves all dependencies listed in your `pyproject.toml` file and downloads the latest version of their files.

When Poetry has finished installing, it writes all the packages and their exact versions that it
downloaded to the `poetry.lock` file, locking the project to those specific versions.

You should commit the `poetry.lock` file to your project repo so that all people working on the project are locked
to the same versions of dependencies.

Running install when a `poetry.lock` file is present resolves and installs all dependencies that you
listed in `pyproject.toml`, but Poetry uses the exact versions listed in `poetry.lock` to ensure that
the package versions are consistent for everyone working on your project.

As a result you will have all dependencies requested by your `pyproject.toml` file, but they may not all
be at the very latest available versions (some dependencies listed in the `poetry.lock` file may have released
newer versions since the file was created).

This is by design, it ensures that your project does not break because of unexpected changes in dependencies.

### Key Features of `poetry lock`

- Ensures deterministic builds by locking dependencies to specific versions.
- Updates the `poetry.lock` file with resolved dependency versions when changes are made in the `pyproject.toml` file.
- Does not install dependencies; it only resolves and locks them.

## 2. poetry lock command

The `poetry lock` command explicitly generates or updates the `poetry.lock` file based on your `pyproject.toml`.

### Syntax

```bash
poetry lock [options]
```

## 3. Common Use Cases

### a. Generate a Lock File

If you create a project and add dependencies, but no lock file exists, generate it explicitly.

```bash
poetry lock
```

This resolves all dependencies and their versions and writes them to `poetry.lock`.

### b. Regenerate the Lock File

If you manually edit `pyproject.toml` or encounter issues with poetry.lock, regenerate it.

```bash
poetry lock --no-update
```

`--no-update`: Regenerates the lock file without upgrading any dependencies.

### c. Force Dependency Updates

Update all dependencies and refresh the lock file.

```bash
poetry lock --update
```

## 4. Key Options

### a. --no-update

Resolves and writes the lock file based on the current `pyproject.toml` without upgrading dependencies.

```bash
poetry lock --no-update
```

### b. --update

Updates all dependencies to their latest compatible versions and rewrites `poetry.lock`.

```bash
poetry lock --update
```

### c. --check

Verifies if the lock file is up-to-date with `pyproject.toml`.

```bash
poetry lock --check
```

Returns an exit code of 0 if up-to-date, otherwise 1.

## 5. Examples

### Example 1: Initial Lock File Creation

```bash
poetry init
poetry add requests
poetry lock
```

`poetry.lock` will include the resolved version of requests and its dependencies.

### Example 2: Verifying the Lock File

```bash
poetry lock --check
```

If the lock file isn’t in sync with pyproject.toml, the command returns an error.

### Example 3: Updating Specific Dependencies

If you want to update only certain dependencies and rewrite the lock file:

```bash
poetry update requests
poetry lock --no-update
```

### Example 4: Refreshing Without Updates

To ensure the lock file is regenerated (e.g., after a manual edit) without upgrading dependencies:

```bash
poetry lock --no-update
```

## 6. Understanding poetry.lock

### Structure of poetry.lock

The file contains:

`Packages`: Direct and transitive dependencies with exact versions.
`Metadata`: Hashes, sources, and other details for integrity.

Example:

```plaintext
[[package]]
name = "requests"
version = "2.28.2"
description = "Python HTTP for Humans."
category = "main"
optional = false
python-versions = ">=3.7"
[metadata]
lock-version = "1.1"
python-versions = "^3.9"
```

## 7. Best Practices for Managing the Lock File

### Commit the Lock File to Version Control

1. Ensure all team members use consistent dependency versions.
2. Always include `poetry.lock` in your Git repository.

### Avoid Manual Edits:

Use poetry add, poetry remove, or poetry update to manage dependencies.
Use `--no-update` for Stability.

When regenerating the lock file, avoid unintended upgrades.

### Verify Lock File Regularly:

Use poetry lock `--check` in CI pipelines to ensure consistency.

### Test After Updates:

After updating dependencies, test your application to ensure compatibility.

## 8. Common Issues and Fixes

### a. Lock File Out of Sync

#### Error:

```plaintext
poetry.lock is not consistent with pyproject.toml
```

#### Fix:

```bash
poetry lock --no-update
```

### b. Dependency Conflict

#### Error:

```plaintext
SolverProblemError: Because depends <dependency> on incompatible versions...
```

#### Fix:

Manually adjust the dependency version in pyproject.toml.
Regenerate the lock file:

```bash
poetry lock
```

## Key Goals in CI/CD with Poetry Lock

1. **Dependency Management** : Verify that the `poetry.lock` file is up-to-date with `pyproject.toml`.
2. **Dependency Installation** : Install the exact dependencies specified in `poetry.lock`.
3. **Environment Consistency** : Recreate the environment defined by `poetry.lock` for tests and deployments.

## Committing your poetry.lock file to version control

### As an application developer

Application developers commit `poetry.lock` to get more `reproducible` builds.

Committing this file to VC is important because it will cause anyone who sets up the project to use the
exact same versions of the dependencies that you are using.

Your `CI server`, production machines, other developers in your team, everything and everyone runs on the
same dependencies, which mitigates the potential for bugs affecting only some parts of the deployments.

Even if you develop alone, in six months when reinstalling the project you can feel confident the dependencies
installed are still working even if your dependencies released many new versions since then.

### As a library developer

Library developers have more to consider.

Your users are application developers, and your library will run in a Python environment you don't control.

The application ignores your library's lock file.

It can use whatever dependency version meets the constraints in your `pyproject.toml`.

The application will probably use the latest compatible dependency version.

If your library's `poetry.lock` falls behind some new dependency version that breaks things for your
users, you're likely to be the last to find out about it.

A simple way to avoid such a scenario is to omit the `poetry.lock` file.

However, by doing so, you sacrifice reproducibility and performance to a certain extent.

Without a lockfile, it can be difficult to find the `reason for failing tests`, because in addition to
obvious code changes an unnoticed library update might be the culprit.

Further, Poetry will have to lock before installing a dependency if `poetry.lock` has been omitted.

Depending on the number of dependencies, locking may take a significant amount of time.

If you do not want to give up the reproducibility and performance benefits, consider a regular refresh of
`poetry.lock` to stay up-to-date and reduce the risk of sudden breakage for users.

### Installing dependencies only

The current project is installed in editable mode by default.

If you want to install the dependencies only, run the `install` command with the `--no-root` flag:

```
poetry install --no-root
```

### Updating dependencies to their latest versions

The `poetry.lock` file prevents you from automatically getting the latest versions of your dependencies.

To update to the latest versions, use the `update` command.

This will fetch the latest matching versions (according to your pyproject.toml file) and update the lock file
with the new versions.
