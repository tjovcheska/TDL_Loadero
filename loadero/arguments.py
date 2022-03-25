import sys
import argparse

auth_token="LoaderoAuth 57e4fed9ea8a52a26872cad37129231c52e34b06bcbfcca5"
project_id=10571
test_id=13807
group_id=57508
participant_id=109647

num=1
default_browser="firefoxLatest"
participant_timeout=1500
test_name="Default Test"
group_name="Default Group"
participant_name="Default Participant"
script="script.py"

def parse_arguments():
    x = int(len(sys.argv))
    if(x < 1):
        raise argparse.ArgumentTypeError("Value should be >= 1")

    parser = argparse.ArgumentParser()

    parser.add_argument('--auth_token', help='Authentication Token', default=auth_token, required=False)
    parser.add_argument('--project_id', help='Project Id', default=project_id, required=False)
    parser.add_argument('--test_id', help='Test Id', default=test_id, required=False)
    parser.add_argument('--group_id', help='Group Id', default=group_id, required=False)
    parser.add_argument('--participant_id', help='Participant Id', default=participant_id, required=False)

    parser.add_argument('--number_groups', help='Number of groups', default=num, required=False)
    parser.add_argument('--number_participants', help='Number of participants', default=num, required=False)
    
    parser.add_argument('--browser_type', help='Browser type', default=default_browser, required=False)
    
    parser.add_argument('--participant_timeout', help='Participant timeout', default=participant_timeout, required=False)
    parser.add_argument('--test_name', help='Test name', default=test_name, required=False)
    parser.add_argument('--group_name', help='Test name', default=group_name, required=False)
    parser.add_argument('--participant_name', help='Test name', default=participant_name, required=False)
    parser.add_argument('--script', help='Script', default=script, required=False)


    args = parser.parse_args()
    return args