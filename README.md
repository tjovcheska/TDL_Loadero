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

  ## Manage tests

  - Back up all test/s from source
  ```
  python manage-tests.py \
  --auth_token_from {AUTH_TOKEN} \
  --project_id_from {PROJECT_ID}  \
  --action backup
  ```
  - Back up certain test/s from source (only tests with test_ids TEST_ID1...TEST_IDN will be backed up)
  ```
  python manage-tests.py \
  --auth_token_from {AUTH_TOKEN} \
  --project_id_from {PROJECT_ID}  \
  --test_ids {TEST_ID1} {TEST_ID2} {TEST_IDN} \
  --action backup
  ```
  - Restore all test/s to destination
  ```
  python manage-tests.py \
  --auth_token_to {AUTH_TOKEN} \
  --project_id_to {PROJECT_ID}  \
  --action restore
  ```
  - Restore certain test/s to destination
  ```
  python manage-tests.py \
  --auth_token_to {AUTH_TOKEN} \
  --project_id_to {PROJECT_ID}  \
  --test_ids {TEST_ID1} {TEST_ID2} {TEST_IDN} \
  --action restore
  ```
  - --auth_token_from - Source project's authentication token
  - --project_id_from - Source project's id
  - --auth_token_to - Destination project's authentication token
  - --project_id_to - Destination project's id
  - --test_ids - ids from tests to be backed up and restored, optional parameter (if not specified all test will be covered)
  - --action - can be backup, restore or clone (includes both backup and restore), optional parameter (if not specified clone)

## Test cases data

  - test.json - Default information about test in json format
  - script_content.json - Test's script in json format
  - groups.json - Test's groups in json format
  - participants.json - Test's participants in json format
  - asserts.json - Test's asserts in json format

## Run tests
- Run test
  ```
  python run.py \
  --auth_token {AUTH_TOKEN} \
  --project_id {PROJECT_ID}  \
  --test_id {TEST_ID}
  ```
  - --auth_token - Project's authentication token
  - --project_id - Project's id
  - --test_id - Test's id
