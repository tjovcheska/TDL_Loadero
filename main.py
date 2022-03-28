import json
from multiprocessing import managers
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

    # # Get all tests
    # Manager.get_all_tests(args)

    # Read from all_tests.json, old test
    test = Manager.read_test_from_responses() 
    test_name=test["name"]
    test_id=test["id"]
    start_interval=test["start_interval"]
    participant_timeout=test["participant_timeout"]
    mode=test["mode"]
    increment_strategy=test["increment_strategy"]
    script_template=Manager.get_script_template(test_id, test_name)

    # Create new test with name TestX
    testX=Manager.create_test(args, args.test_name, start_interval, participant_timeout, mode, increment_strategy, script_template)
    testX_id=testX["id"]
    testX_name=testX["name"]

    # Create subdirectory for test with test_id
    Manager.create_test_case_subdirectory(testX_id, testX_name)

    # Read from groups.json, old test
    groups=Manager.read_groups_from_groups(test_id, test_name)

    # Read from participants.json, old test
    participants=Manager.read_participants_from_participants(test_id, test_name)

    for group in groups:
        group_name=group["name"]
        group_count=group["count"]
        new_group=Manager.create_new_group(args, testX_id, group_count, group_name)
        new_group_id=new_group["id"]
        for participant in participants:
            participant_browser=participant["browser"]
            participant_name=participant["name"]
            participant_count=participant["count"]
            Manager.create_new_participant(args, testX_id, new_group_id, participant_browser, participant_count, participant_name)

    # Get all groups for test with test_id
    Manager.get_all_groups(args, testX_id, testX_name)

    # Get all participants for test with test_id
    Manager.get_all_participants(args, testX_id, testX_name)

    # Get script_file_id
    script_file_id=Manager.get_script_file_id(args)
    print(script_file_id)

    # Get script content
    Manager.get_script_content(args, script_file_id, testX_id, testX_name)

    # Get test info and write it to a folder
    Manager.get_test_with_id(args, testX_id, testX_name)

    # # Running test 
    # test_run_id = Runner.start_test(args, testX_id)
    # status = Runner.get_test_run_id_status(args, testX_id, test_run_id)
    # Runner.wait_for_test_completion(args, testX_id, test_run_id, status)
    # Runner.check_status(args, testX_id, test_run_id)

main()
