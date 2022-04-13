import loadero.manager as Manager
import os
import re

# Backup test from Loadero
def backup_tests(project_id_from, auth_token_from, test_ids_list):
    all_tests_list = Manager.get_all_tests(project_id_from, auth_token_from)
    print(all_tests_list)

    for test in all_tests_list:
        test_id=test["id"]
        test_name=test["name"]

        if test_ids_list: # if test_ids_list is not empty
            if test_id in test_ids_list:
                Manager.create_test_case_subdirectory(test_id, test_name)
                Manager.get_test_info(project_id_from, auth_token_from, test_id, test_name)
                Manager.get_all_groups(project_id_from, auth_token_from, test_id, test_name)
                Manager.get_all_participants(project_id_from, auth_token_from, test_id, test_name)
                Manager.get_all_asserts(project_id_from, auth_token_from, test_id, test_name)
                script_file_id = Manager.get_script_file_id(project_id_from, auth_token_from)
                Manager.get_script_content_api(project_id_from, auth_token_from, script_file_id, test_id, test_name)
        else: # if test_ids_list is empty backup all tests
            Manager.create_test_case_subdirectory(test_id, test_name)
            Manager.get_test_info(project_id_from, auth_token_from, test_id, test_name)
            Manager.get_all_groups(project_id_from, auth_token_from, test_id, test_name)
            Manager.get_all_participants(project_id_from, auth_token_from, test_id, test_name)
            Manager.get_all_asserts(project_id_from, auth_token_from, test_id, test_name)
            script_file_id = Manager.get_script_file_id(project_id_from, auth_token_from)
            Manager.get_script_content_api(project_id_from, auth_token_from, script_file_id, test_id, test_name)

# Restore test from files and create a copy
def restore_tests(project_id_to, auth_token_to, test_ids_list):
    dir='./test_cases'
    dict={}
    if(len(dir) > 0):
        sub_dir = [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]
        for dir_name in sub_dir:
            dir_name_list = re.split("_", dir_name)
            dict["id"]=int(dir_name_list[0])
            dict["name"]=dir_name_list[1]
            test_id=dict['id']
            test_name=dict['name']

            if test_ids_list: # if test_ids_list is not empty
                if test_id in test_ids_list: 
                    # Read from files
                    test = Manager.read_test_from_file(test_id, test_name)
                    print(test)
                    start_interval = test["start_interval"]
                    participant_timeout = test["participant_timeout"]
                    mode = test["mode"]
                    increment_strategy = test["increment_strategy"]
                    script_template = Manager.get_script_template_from_file(test_id, test_name)

                    # Generate a new test
                    new_test = Manager.create_test(project_id_to, auth_token_to, test_name, start_interval, participant_timeout, mode, increment_strategy, script_template)
                    new_test_id = new_test["id"]
                    groups = Manager.read_groups_from_file(test_id, test_name)
                    participants = Manager.read_participants_from_file(test_id, test_name)
                    asserts = Manager.read_asserts_from_file(test_id, test_name)     
                    
                    for group in groups:
                        group_name = group["name"]
                        group_count = group["count"]
                        new_group = Manager.create_new_group(project_id_to, auth_token_to, new_test_id, group_count, group_name)
                        new_group_id = new_group["id"]
                        for participant in participants:
                            participant_browser=participant["browser"]
                            participant_name=participant["name"]
                            participant_count=participant["count"]
                            Manager.create_new_participant(project_id_to, auth_token_to, new_test_id, new_group_id, participant_browser, participant_count, participant_name)

                    for a in asserts:
                        assert_expected = a["expected"]
                        assert_operator = a["operator"]
                        assert_path = a["path"]
                        Manager.create_new_assert(project_id_to, auth_token_to, new_test_id, assert_expected, assert_operator, assert_path)
            else: # if test_ids_list is empty restore all tests
                # Read from files
                test = Manager.read_test_from_file(test_id, test_name)
                start_interval = test["start_interval"]
                participant_timeout = test["participant_timeout"]
                mode = test["mode"]
                increment_strategy = test["increment_strategy"]
                script_template = Manager.get_script_template_from_file(test_id, test_name)

                # Generate a new test
                new_test = Manager.create_test(project_id_to, auth_token_to, test_name, start_interval, participant_timeout, mode, increment_strategy, script_template)
                new_test_id = new_test["id"]
                groups = Manager.read_groups_from_file(test_id, test_name)
                participants = Manager.read_participants_from_file(test_id, test_name)
                asserts = Manager.read_asserts_from_file(test_id, test_name)     
                
                for group in groups:
                    group_name = group["name"]
                    group_count = group["count"]
                    new_group = Manager.create_new_group(project_id_to, auth_token_to, new_test_id, group_count, group_name)
                    new_group_id = new_group["id"]
                    for participant in participants:
                        participant_browser=participant["browser"]
                        participant_name=participant["name"]
                        participant_count=participant["count"]
                        Manager.create_new_participant(project_id_to, auth_token_to, new_test_id, new_group_id, participant_browser, participant_count, participant_name)

                for a in asserts:
                    assert_expected = a["expected"]
                    assert_operator = a["operator"]
                    assert_path = a["path"]
                    Manager.create_new_assert(project_id_to, auth_token_to, new_test_id, assert_expected, assert_operator, assert_path)

    else:
        print('Directory ' + dir + ' is empty')