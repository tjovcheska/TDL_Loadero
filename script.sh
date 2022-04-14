pip3 install virtualenv
virtualenv --version
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 run.py --auth_token $1 --project_id $2 --test_id $3
