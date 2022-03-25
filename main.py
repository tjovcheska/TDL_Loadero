import json
from re import template
import loadero.runner as Runner
import loadero.manager as Manager
import sys
import argparse

auth_token="LoaderoAuth 57e4fed9ea8a52a26872cad37129231c52e34b06bcbfcca5"
project_id=10571

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
    #parser.add_argument('--test_id', help='Test Id', default=test_id, required=False)
    # parser.add_argument('--group_id', help='Group Id', default=group_id, required=False)
    # parser.add_argument('--participant_id', help='Participant Id', default=participant_id, required=False)

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

def main():
    args=parse_arguments()

    # Get all tests
    # Manager.get_all_tests(args)

    # Get test_id
    test_id=Manager.read_test_id()
    print(test_id)

    # Get test_name
    test_name=Manager.read_test_name()
    print(test_name)

    script_template=Manager.get_script_template(test_id, test_name)
    print(type(script_template))

    Manager.create_test(args, script_template)

    # # Create subdirectory for test with test_id
    # Manager.create_test_case_subdirectory(test_id, test_name)

    # # Get all groups for test with test_id
    # Manager.get_all_groups(args, test_id, test_name)

    # # Get all participants for test with test_id
    # Manager.get_all_participants(args, test_id, test_name)

    # # Get script_file_id
    # script_file_id=Manager.get_script_file_id(args)
    # # print(script_file_id)

    # # Get script content
    # Manager.get_script_content(args, script_file_id, test_id, test_name)

    # # Get group_id
    # group_id = Manager.read_group_id(test_id, test_name)
    # # print(group_id)

    # # Get participant_id
    # participant_id = Manager.read_participant_id(test_id, test_name)
    # # print(participant_id)

    # Running test 
    # test_run_id = Runner.start_test(args)
    # status = Runner.get_test_run_id_status(args, test_run_id)
    # Runner.wait_for_test_completion(args, test_run_id, status)
    # Runner.check_status(args, test_run_id)



main()
