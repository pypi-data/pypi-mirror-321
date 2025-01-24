# TextToAPI

A package for the TextToAPI tool.

## Latest Commit

In the latest commit, version 0.1.3, this is the initial setup for the TextToAPI tool. This commit includes the `setup.py` file, which configures the package with necessary metadata such as the name, version, description, and author. It also specifies the required dependencies, including `setuptools`, `python-dotenv`, `llama-index`, `Flask`, and others. The package data is configured to include `.env` files, and the Python version requirement is set to >=3.7. These changes establish the foundational structure for the TextToAPI tool, enabling further development and integration.

## Installation

To install the package, run:

```bash
pip install texttoapi
```

## Usage

After installation, you can import and use the `texttoapi` package in your projects:

```python
from texttoapi import utils
from texttoapi import cli_chat
from texttoapi import env
```

## Contributing / Modifying the Package

If you want to modify the package, follow these steps:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd TexttoApi
```

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment for development:

```bash
python3 -m venv venv
source venv/bin/activate  
```

### 3. Install Dependencies

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Make Changes to the Code

You can now modify the package files (`cli_chat.py`, `utils.py`, `env.py`, etc.) as needed. Ensure you follow best practices for Python development.

### 5. Test Your Changes

To test the changes, you can install the package locally in editable mode:

```bash
pip install -e .
```

This will link the package to your local directory, so any changes you make are reflected immediately.

### 6. Rebuild the Package

After making and testing your changes, rebuild the package for distribution:

```bash
rm -rf dist/ build/ *.egg-info
python setup.py sdist bdist_wheel
```

### 7. Publish the Package (Optional)

If you want to publish the updated package to PyPI, use `twine`:

```bash
pip install twine
twine upload dist/*
```

### 8. Create a Pull Request (Optional)

If this package is hosted on a platform like GitHub or GitLab, and you'd like to contribute your changes back, create a pull request:

1. Push your changes to a new branch:
   ```bash
   git checkout -b feature/your-feature
   git push origin feature/your-feature
   ```

2. Open a pull request from your branch to the main repository.

---

By following these steps, you can modify and improve the TextToAPI package to suit your needs or contribute enhancements back to the project.

