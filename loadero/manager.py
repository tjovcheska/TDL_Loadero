import json
import requests
import sys
import os

# Read test from a file
def read_test_from_file(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name +'/test.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        return response_json

# Read groups from a file
def read_groups_from_file(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' +test_name +'/groups.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        return response_json

# Read participants from a file
def read_participants_from_file(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' +test_name +'/participants.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        return response_json

# Read asserts from a file
def read_asserts_from_file(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' +test_name +'/asserts.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        return response_json

# Read script template from a file
def get_script_template_from_file(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name +'/script_content.json')
    with open(absolute_path, 'r') as script:
        template=script.read()
        template_json = json.loads(template)
        template_content=template_json["content"]
    return template_content

# Read group_id from a file
def read_group_id(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' +test_name +'/groups.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        for result in response_json:
            group_id=result["id"]
            return group_id

# Read participant_id a from file
def read_participant_id(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name + '/participants.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        for result in response_json:
            participant_id=result["id"]
            return participant_id

# Create test on Loadero
def create_test(project_id, auth_token, test_name, start_interval, participant_timeout, mode, increment_strategy, script_template):
    url="https://api.loadero.com/v2/projects/{0}/tests/".format(project_id)
    payload=json.dumps({
        "name": test_name,
        "start_interval": start_interval,
        "participant_timeout": participant_timeout,
        "mode": mode,
        "increment_strategy": increment_strategy,
        "script": script_template
    })
    headers={}
    headers["Authorization"]= 'LoaderoAuth {0}'.format(auth_token)
    headers["Content-type"]="application/json"

    try:
        response=requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==201):
            print("Test created successfully!")
            response_json=response.json()
            return response_json

    except requests.exceptions.RequestException as e:
            print("Error: {}".format(e))
            sys.exit(e)

# Delete test on Loadero
def delete_test(project_id, auth_token, test_id):
        url="https://api.loadero.com/v2/projects/{0}/tests/{1}/".format(project_id, test_id)
        payload={}
        headers={}
        headers["Authorization"]='LoaderoAuth {0}'.format(auth_token)
    
        try:
            response=requests.delete(url, headers=headers, data=payload)
            response.raise_for_status()
            if(response.status_code==200):
                print("Test deleted successfully !")

        except requests.exceptions.RequestException as e:
            print("Error: {}".format(e))
            sys.exit(e)

# Read test from loadero
def read_test(project_id, auth_token, test_id):
        url="https://api.loadero.com/v2/projects/{0}/tests/{1}/".format(project_id, test_id)
        payload={}
        headers={}
        headers["Authorization"]='LoaderoAuth {0}'.format(auth_token)
    
        try:
            response=requests.get(url, headers=headers, data=payload)
            response.raise_for_status()
            if(response.status_code==200):
                json_response=response.json()
                return json_response

        except requests.exceptions.RequestException as e:
            print("Error: {}".format(e))
            sys.exit(e)

# Update test on Loadero
def update_test(project_id, auth_token, test_id, template, test_name, participant_timeout):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/".format(project_id, test_id)
    headers={}
    headers["Authorization"]='LoaderoAuth {0}'.format(auth_token)
    headers["Content-type"]="application/json"

    payload = json.dumps({
        'name': test_name,
        'start_interval': 1,
        'participant_timeout': participant_timeout,
        'mode': 'performance',
        'increment_strategy': 'linear',
        'script': template
        })

    try:
        response = requests.put(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            print("Successfully updated test!")

    except requests.exceptions.RequestException as e:
            print("Error: {}".format(e))
            sys.exit(e)

# Update group on Loadero
def update_group(project_id, auth_token,test_id, group_id, group_name, number_groups):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/groups/{2}".format(project_id, test_id, group_id)
    headers={}
    headers["Authorization"]='LoaderoAuth {0}'.format(auth_token)
    headers["Content-type"]="application/json"
    payload=json.dumps({
            'name': group_name,
            'count': number_groups})

    try:
        response=requests.put(url, headers=headers, data=payload)
        response.raise_for_status()
        print(response.status_code)
        if(response.status_code==200):
            print("Successfully updated group!")

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Update participant on Loadero
def update_paricipant(project_id, auth_token, test_id, group_id, participant_id, browser_type, number_participants, participant_name):
    url = "https://api.loadero.com/v2/projects/{0}/tests/{1}/groups/{2}/participants/{3}/".format(project_id, test_id, group_id, participant_id)
    payload = json.dumps({
    "browser": browser_type,
    "count": number_participants,
    "name": participant_name
    })
    headers={}
    headers["Authorization"]='LoaderoAuth {0}'.format(auth_token)
    headers["Content-type"]="application/json"

    try:
        response = requests.put(url, headers=headers, data=payload)
        response.raise_for_status()
        print(response.status_code)
        if(response.status_code==200):
            print("Successfully updated participant!")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Get all tests from Loadero
def get_all_tests(project_id, auth_token):
    url="https://api.loadero.com/v2/projects/{0}/tests".format(project_id)
    payload={}
    headers={}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)

    try:
        response=requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            all_tests=json_response['results']
            return all_tests

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Get all tests from Loadero and store theirs ids in a list
def get_all_test_ids(project_id, auth_token):
    url="https://api.loadero.com/v2/projects/{0}/tests".format(project_id)
    payload={}
    headers={}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)

    try:
        response=requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            test_ids=[]
            json_response=response.json()
            all_tests=json_response['results']
            for test in all_tests:
                test_id=test["id"]
                test_ids.append(test_id)
            return test_ids

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Get script_file_id from loadero
def get_script_file_id(project_id, auth_token):
    url="https://api.loadero.com/v2/projects/{0}/tests".format(project_id)
    payload={}
    headers={}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)

    try:
        response=requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            all_tests=json_response['results']
            for result in all_tests:
                script_file_id=result['script_file_id']
                return script_file_id

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Get script content from Loadero
def get_script_content_api(project_id, auth_token, script_file_id, test_id, test_name):
    url="https://api.loadero.com/v2/projects/{0}/files/{1}/".format(project_id, script_file_id)
    payload={}
    headers={}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)

    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            script_file=json.dumps(json_response)
            path=os.path.abspath('test_cases/' + str(test_id) +  '_' + str(test_name) + '/script_content.json')
            with open(path, "w") as f:
                f.write(script_file)

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Create subdirectory for new test case
def create_test_case_subdirectory(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name)
    if(not os.path.exists(absolute_path)):
        os.makedirs(absolute_path)
    else:
        print("Subdirectory for test case with " + str(test_id) + " already exists!")
        
# Duplicate existing test on Loadero
def duplicate_existing_test(project_id, auth_token, test_id):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/copy/".format(project_id, test_id)
    payload={}
    headers={}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            print("Successfully duplicated test!")

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Create group for test on Loadero
def create_new_group(project_id, auth_token, test_id, group_count, group_name):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/groups/".format(project_id, test_id)
    payload=json.dumps({
        "count": group_count,
        "name": group_name
    })
    headers={}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)
    headers['Content-Type']='application.json'

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==201):
            print("Successfully created new group!")
            response_json=response.json()
            return response_json

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)   

# Create new participant on Loadero
def create_new_participant(project_id, auth_token, test_id, group_id, participant_browser, participant_count, participant_name):
    url = "https://api.loadero.com/v2/projects/{0}/tests/{1}/groups/{2}/participants".format(project_id, test_id, group_id)
    payload=json.dumps({
        "browser": participant_browser,
        "count": participant_count,
        "name": participant_name
    })
    headers={}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)
    headers['Content-Type']='application.json'
    
    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==201):
            print("Successfully created new participant!")

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Create new assert on Loadero
def create_new_assert(project_id, auth_token, test_id, expected, operator, path):
    url = "https://api.loadero.com/v2/projects/{0}/tests/{1}/asserts".format(project_id, test_id)
    payload = json.dumps({
    "expected": expected,
    "operator": operator,
    "path": path
    })
    headers = {}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)
    headers['Content-Type']='application/json'
    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==201):
            print("Successfully created new assert!")
            response_json=response.json()
            return response_json
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Get test info and write it to a file
def get_test_info(project_id, auth_token, test_id, test_name):
    url = "https://api.loadero.com/v2/projects/{0}/tests/{1}/".format(project_id, test_id)
    payload={}
    headers = {}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)

    try:
        response=requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            test_info=json.dumps(json_response)
            absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name + '/test.json')
            with open(absolute_path, "w") as f:
                f.write(test_info)
                f.write("\n")

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Get all groups from loadero and write them to a file
def get_all_groups(project_id, auth_token, test_id, test_name):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/groups".format(project_id, test_id)
    payload={}
    headers={}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)
    
    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            all_groups=json_response['results']
            all_groups_json=json.dumps(all_groups)
            absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name +'/groups.json')
            with open(absolute_path, "w") as f:
                f.write(all_groups_json)
                f.write("\n")

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Get all participants from loadero and write them to a file
def get_all_participants(project_id, auth_token, test_id, test_name):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/participants".format(project_id, test_id)
    payload={}
    headers={}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)

    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            all_participants=json_response['results']
            all_participants_json=json.dumps(all_participants)
            absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_'+ test_name +'/participants.json')
            with open(absolute_path, "w") as f:
                f.write(all_participants_json)
                f.write("\n")

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)


# Get all existing asserts for test and write them to a file
def get_all_asserts(project_id, auth_token, test_id, test_name):
    url = "https://api.loadero.com/v2/projects/{0}/tests/{1}/asserts".format(project_id, test_id)

    payload={}
    headers = {}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)

    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            results=json_response['results']
            asserts=json.dumps(results)
            absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name + '/asserts.json')
            with open(absolute_path, "w") as f:
                f.write(asserts)
                f.write("\n")

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

def get_asserts(project_id, auth_token, test_id):
    url = "https://api.loadero.com/v2/projects/{0}/tests/{1}/asserts".format(project_id, test_id)

    payload={}
    headers = {}
    headers['Authorization']='LoaderoAuth {0}'.format(auth_token)

    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            asserts=json_response['results']
            return asserts

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(e)

# Filter multiple tests as a list or all existing if not specified
def filter_multiple_tests_as_list(args):
    # Test ids from api call
    api_test_ids = get_all_test_ids(args)
    print(api_test_ids)
    # Test ids from args
    print(args.test_ids)
    # Final ids
    test_ids=[]

    if args.test_ids:
        for i in api_test_ids:
            for j in args.test_ids:
                if(i == j):
                    test_ids.append(i)
    else:
        test_ids=api_test_ids

    return test_ids
