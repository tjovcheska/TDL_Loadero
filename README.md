# Loadero script

## Prerequisites

- Install Python

  ```
  brew install python
  ```

- Create virtual environment

  ```
  python -m venv venv
  ```

- Activate virtual enviornment

  ```
  source venv/bin/activate
  ```

- Install depenendencies

  ```bash
  pip install -r requirements.txt
  ```

- When done modifying virtual environment, leave it
  ```
  deactivate
  ```

## Run script
- project_id, test_id, test_name are optional parametars. If are not set, uses default.

- Use the following to execute your script, (venv is already activated):

  ```
  python {FILE_NAME}.py
  ```

- Use the following to execute your script with parametars,  (venv is already activated):

  ``'
  python {FILE_NAME}.py \
  --project_id \
  --test_id \
  --test_name
  ```

## Docker

- Build image from Dockerfile

  ```
  docker build -t {IMAGE_NAME} .
  ```

- Run image from Dockerfile 

  ```
  docker run -it {IMAGE_NAME}
  ```

- Run image from Dockerfile with parametars

  ```
  docker run -it {IMAGE_NAME} --project_id {PROJECT_ID} --test_id {TEST_ID} --test-name {TEST_NAME}
  ```
