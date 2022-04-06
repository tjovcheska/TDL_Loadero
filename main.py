import json
import loadero.runner as Runner
import loadero.manager as Manager
import sys
import argparse

auth_token="LoaderoAuth 57e4fed9ea8a52a26872cad37129231c52e34b06bcbfcca5"
project_id=10571

test_name="WebRTC"
start_interval=1
participant_timeout=250000
mode="performance"
increment_strategy="linear"
group_count=1
group_name="Group1"
participant_browser="chromeLatest"
participant_count=2
participant_name="Participant"

def parse_arguments():
    x = int(len(sys.argv))
    if(x < 1):
        raise argparse.ArgumentTypeError("Value should be >= 1")

    parser = argparse.ArgumentParser()

    parser.add_argument('--auth_token', help='Authentication Token', default=auth_token, required=False)
    parser.add_argument('--project_id', help='Project Id', default=project_id, required=False)

    parser.add_argument('--test_name', help='Test name', default=test_name, required=False)
    parser.add_argument('--start_interval', help='Start interval', default=start_interval, required=False)
    parser.add_argument('--participant_timeout', help='Participant timeout', default=participant_timeout, required=False)
    parser.add_argument('--mode', help='Mode', default=mode, required=False)
    parser.add_argument('--increment_strategy', help='Increment strategy', default=increment_strategy, required=False)
    parser.add_argument('--group_count', help='Group count', default=group_count, required=False)
    parser.add_argument('--group_name', help='Group name', default=group_name, required=False)
    parser.add_argument('--participant_browser', help='Participant brpwser', default=participant_browser, required=False)
    parser.add_argument('--participant_count', help='Participant count', default=participant_count, required=False)
    parser.add_argument('--participant_name', help='Participant name', default=participant_name, required=False)

    args = parser.parse_args()
    return args

def main():
    args=parse_arguments()

    # # Initial test
    test_id = 14089
    test_name = "WebRTC"

    # Create subdirectory for initial test
    Manager.create_test_case_subdirectory(test_id, test_name)

    # Get test info
    Manager.get_test_with_id(args, test_id, test_name)

    # Get all groups for WebRTC test and store to a file
    Manager.get_all_groups(args, test_id, test_name)

    # Get all participants for WebRTC test and store to a file
    Manager.get_all_participants(args, test_id, test_name)

    # Get all asserts for WebRTC test and store to a file
    Manager.get_all_asserts(args, test_id, test_name)

    # Get script
    script_file_id=Manager.get_script_file_id(args)
    Manager.get_script(args, script_file_id, test_id, test_name)

    #Read WebRTC test info from file
    test = Manager.read_test_from_responses(test_id, test_name)
    start_interval=test["start_interval"]
    # print(start_interval)
    participant_timeout=test["participant_timeout"]
    # print(participant_timeout)
    mode=test["mode"]
    # print(mode)
    increment_strategy=test["increment_strategy"]
    # print(increment_strategy)
    script_template=Manager.get_script_template(test_id, test_name)
    # print(script_template)

    # Generate a new test
    WebRTC_test=Manager.create_test(args, args.test_name, start_interval, participant_timeout, mode, increment_strategy, script_template)
    WebRTC_test_id=WebRTC_test["id"]
    #print(WebRTC_test_id)
    WebRTC_test_name=WebRTC_test["name"]
    #print(WebRTC_test_name)

    # Create subdirectory for WebRTC_test
    Manager.create_test_case_subdirectory(WebRTC_test_id, WebRTC_test_name)

    # Read from groups.json, old test
    groups=Manager.read_groups_from_groups(test_id, test_name)
    #print(groups)

    # Read from participants.json, old test
    participants=Manager.read_participants_from_participants(test_id, test_name)
    #print(participants)

    # Read from asserts.json, old test
    asserts=Manager.read_asserts_from_file(test_id, test_name)
    #print(asserts)

    for group in groups:
        group_name=group["name"]
        group_count=group["count"]
        new_group=Manager.create_new_group(args, WebRTC_test_id, group_count, group_name)
        new_group_id=new_group["id"]
        for participant in participants:
            participant_browser=participant["browser"]
            participant_name=participant["name"]
            participant_count=participant["count"]
            Manager.create_new_participant(args, WebRTC_test_id, new_group_id, participant_browser, participant_count, participant_name)
    
    for a in asserts:
                assert_expected=a["expected"]
                print(assert_expected)
                assert_operator=a["operator"]
                print(assert_operator)
                assert_path=a["path"]
                print(assert_path)
                new_assert=Manager.create_new_assert(args, WebRTC_test_id, assert_expected, assert_operator, assert_path)
                print(new_assert)

    # Get test info
    Manager.get_test_with_id(args, WebRTC_test_id, WebRTC_test_name)

    # Get groups info
    Manager.get_all_groups(args, WebRTC_test_id, WebRTC_test_name)

    # Get participants info
    Manager.get_all_participants(args, WebRTC_test_id, WebRTC_test_name)

    #Get asserts info
    Manager.get_all_asserts(args, WebRTC_test_id, WebRTC_test_name)

    # Get script content
    script_file_id=Manager.get_script_file_id(args)
    Manager.get_script_content(args, script_file_id, WebRTC_test_id, WebRTC_test_name)
    
    # # Running test 
    # test_run_id = Runner.start_test(args, WebRTC_test_id)
    # status = Runner.get_test_run_id_status(args, WebRTC_test_id, test_run_id)
    # Runner.wait_for_test_completion(args, WebRTC_test_id, test_run_id, status)
    # Runner.check_status(args, WebRTC_test_id, test_run_id)

main()
