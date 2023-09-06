# Django workshops

## Setup project

### Clone repository (recommended)
* Clone repository:
  ```bash
  cd <your_projects_dir>
  git clone https://github.com/luk1999/django_workshops.git django_workshops
* Checkout `chapter-0` branch:
  ```bash
  git checkout chapter-0
  ```

### Create from scratch
* Create directory
  ```bash
  cd <your_projects_dir>
  mkdir django_workshops
  ```
* Copy files: `requirements.txt`, `Pipfile` and `Pipfile.lock` from [repository](https://github.com/luk1999/django_workshops.git) to your `django_workshops` directory.


### Create virtual env:
  * Using `venv` (Linux):
    ```bash
    cd django_workshops
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    ```
  * Using `venv` (Windows):
    ```powershell
    cd django_workshops
    C:\python3\python -m venv .venv
    .venv\scripts\activate
    pip install -r requirements.txt
    ```
  * Using [pipenv](https://pipenv.pypa.io/en/latest/):
    ```bash
    cd django_workshops
    pipenv --python 3.12
    pipenv shell
    pipenv install --dev
    ```

### Continue tutorial
Now go to `readme` subdirectory and follow instruction (start with `chapter-0.md`).
