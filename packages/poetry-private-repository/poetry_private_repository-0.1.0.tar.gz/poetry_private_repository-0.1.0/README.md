# Private repository

To use a private repository with Poetry, you can configure it to authenticate and install packages from the repository.

## 1. Add the Private Repository to Poetry

```bash
poetry config repositories.<repository-name> <repository-url>
```

- Replace `<repository-name>` with a name for the repository (e.g., `my-private-repo`).
- Replace `<repository-url>` with the URL of your private repository.

```
poetry config repositories.my-private-repo https://my-private-repo.example.com/simple
```

## 2. Authenticate with the Repository

If your private repository requires authentication, configure the credentials:

```bash
poetry config http-basic.<repository-name> <username> <password>
```

- Replace `<repository-name>` with the same name as above.
- Replace `<username>` and `<password>` with your repository credentials.

```bash
poetry config http-basic.my-private-repo my-username my-password
```

## 3. Add Dependencies from the Private Repository

```bash
poetry add <package-name> --source <repository-name>
```

```bash
poetry add my-private-package --source my-private-repo
```

## 4. Check Configuration

You can confirm your repository and authentication settings with.

```bash
poetry config --list
```

## 5. Using the pyproject.toml File

```bash
[[tool.poetry.source]]
name = "my-private-repo"
url = "https://my-private-repo.example.com/simple"
default = false

```

When a dependency is added, it will reference the private repository:

```
[tool.poetry.dependencies]
my-private-package = { version = "^1.0.0", source = "my-private-repo" }
```

## 6. Testing Installation

Run the following to verify the setup:

```bash
poetry install
```
