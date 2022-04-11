import json
import requests
import sys
import os

# Read script template from test with test_id and test_name
def get_script_template(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name +'/script_content.py')
    with open(absolute_path, 'r') as script:
        template=script.read()
    return template

# Read new script template from file
def get_new_script_template():
    absolute_path=os.path.abspath('WebRTC/script_content.py')
    with open(absolute_path, 'r') as script:
        template=script.read()
    return template

# Create new test
def create_test(args, test_name, start_interval, participant_timeout, mode, increment_strategy, script_template):
    url="https://api.loadero.com/v2/projects/{0}/tests/".format(args.project_id)
    payload=json.dumps({
        "name": test_name,
        "start_interval": start_interval,
        "participant_timeout": participant_timeout,
        "mode": mode,
        "increment_strategy": increment_strategy,
        "script": script_template
    })
    headers={}
    headers["Authorization"]=args.auth_token
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
            sys.exit(1)

# Read tests from file
def read_test_from_responses(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name +'/testinfo.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        return response_json

# Read groups from file
def read_groups_from_groups(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' +test_name +'/groups.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        return response_json

# Read participants from file
def read_participants_from_participants(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' +test_name +'/participants.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        return response_json

# Read asserts from file
def read_asserts_from_file(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' +test_name +'/asserts.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        return response_json

# Delete test
def delete_test(args):
        url="https://api.loadero.com/v2/projects/{0}/tests/{1}/".format(args.project_id, args.test_id)
        payload={}
        headers={}
        headers["Authorization"]=args.auth_token
    
        try:
            response=requests.delete(url, headers=headers, data=payload)
            response.raise_for_status()
            if(response.status_code==200):
                print("Test deleted successfully !")

        except requests.exceptions.RequestException as e:
            print("Error: {}".format(e))
            sys.exit(1)

# Read test from loadero
def read_test(args, test_id):
        url="https://api.loadero.com/v2/projects/{0}/tests/{1}/".format(args.project_id, test_id)
        payload={}
        headers={}
        headers["Authorization"]=args.auth_token
    
        try:
            response=requests.get(url, headers=headers, data=payload)
            response.raise_for_status()
            if(response.status_code==200):
                json_response=response.json()
                return json_response

        except requests.exceptions.RequestException as e:
            print("Error: {}".format(e))
            sys.exit(1)
# Update test on loadero
def update_test(args, test_id, template):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/".format(args.project_id, test_id)
    headers={}
    headers["Authorization"]=args.auth_token
    headers["Content-type"]="application/json"

    payload = json.dumps({
        'name': args.test_name,
        'start_interval': 1,
        'participant_timeout': args.participant_timeout,
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
            sys.exit(1)

# Update group on loadero
def update_group(args, test_id, group_id):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/groups/{2}".format(args.project_id, test_id, group_id)
    headers={}
    headers["Authorization"]=args.auth_token
    headers["Content-type"]="application/json"
    payload=json.dumps({
            'name': args.group_name,
            'count': args.number_groups})

    try:
        response=requests.put(url, headers=headers, data=payload)
        response.raise_for_status()
        print(response.status_code)
        if(response.status_code==200):
            print("Successfully updated group!")

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

# Update participant on loadero
def update_paricipant(args, test_id, group_id, participant_id):
    url = "https://api.loadero.com/v2/projects/{0}/tests/{1}/groups/{2}/participants/{3}/".format(args.project_id, test_id, group_id, participant_id)
    payload = json.dumps({
    "browser": args.browser_type,
    "count": args.number_participants,
    "name": args.participant_name
    })
    headers={}
    headers["Authorization"]=args.auth_token
    headers["Content-type"]="application/json"

    try:
        response = requests.put(url, headers=headers, data=payload)
        response.raise_for_status()
        print(response.status_code)
        if(response.status_code==200):
            print("Successfully updated participant!")
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

# Get all tests from loadero and write them to a file
def get_all_tests(args):
    url="https://api.loadero.com/v2/projects/{0}/tests".format(args.project_id)
    payload={}
    headers={}
    headers['Authorization']=args.auth_token

    try:
        response=requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            all_tests=json_response['results']
            all_tests_json=json.dumps(all_tests)
            absolute_path=os.path.abspath('responses/all_tests.json')
            with open(absolute_path, "w") as f:
                f.write(all_tests_json)

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

# Get all groups for test wit test_id and test_name from loadero and write them to a file
def get_all_groups(args, test_id, test_name):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/groups".format(args.project_id, test_id)
    payload={}
    headers={}
    headers['Authorization']=args.auth_token
    
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

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

# Get all participants for test wit test_id and test_name from loadero and write them to a file
def get_all_participants(args, test_id, test_name):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/participants".format(args.project_id, test_id)
    payload={}
    headers={}
    headers['Authorization']=args.auth_token

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

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

# Get script_file_id from loadero
def get_script_file_id(args):
    url="https://api.loadero.com/v2/projects/{0}/tests".format(args.project_id)
    payload={}
    headers={}
    headers['Authorization']=args.auth_token

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
        sys.exit(1)


def get_script(args, script_file_id, test_id, test_name):
    url="https://api.loadero.com/v2/projects/{0}/files/{1}/".format(args.project_id, script_file_id)
    payload={}
    headers={}
    headers['Authorization']=args.auth_token

    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            script_file=json.dumps(json_response)
            path=os.path.abspath('test_cases/' + str(test_id) +  '_' + str(test_name) + '/script_content.py')
            with open(path, "w") as f:
                f.write(script_file)

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

# Get script content from loadero and write it to a file
def get_script_content(args, script_file_id, test_id, test_name):
    url="https://api.loadero.com/v2/projects/{0}/files/{1}/".format(args.project_id, script_file_id)
    payload={}
    headers={}
    headers['Authorization']=args.auth_token

    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            script_file_content=json_response["content"]
            #print(script_file_content)
            path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name + '/script_content.py')
            with open(path, "w") as f:
                f.write(script_file_content)

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

# Read test_id from file
def read_test_id():
    absolute_path=os.path.abspath('responses/all_tests.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        for result in response_json:
            test_id=result["id"]
            return test_id

# Read test_name from file
def read_test_name():
    absolute_path=os.path.abspath('responses/all_tests.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        for result in response_json:
            test_name=result["name"]
            return test_name

# Read group_id from file
def read_group_id(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' +test_name +'/groups.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        for result in response_json:
            group_id=result["id"]
            return group_id

# Read participant_id from file
def read_participant_id(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name + '/participants.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        response_json=json.loads(response)
        for result in response_json:
            participant_id=result["id"]
            return participant_id

# Create subdirectory for new test case
def create_test_case_subdirectory(test_id, test_name):
    absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name)
    if(not os.path.exists(absolute_path)):
        os.makedirs(absolute_path)
    else:
        print("Subdirectory for test case with " + str(test_id) + " successfully created!")
        
# Duplicate existing test on loadero
def duplicate_existing_test(args, test_id):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/copy/".format(args.project_id, test_id)
    payload={}
    headers={}
    headers['Authorization']=args.auth_token

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            print("Successfully duplicated test!")

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

# Read all tests from a fie and filter them
def filter_tests_by_name(name_for_search):
    absolute_path=os.path.abspath('responses/all_tests.json')
    with open(absolute_path, "r") as f:
        response=f.read()
        tests=json.loads(response)
        for test in tests:
            if(test["name"] == name_for_search):
                return test
        print("There is no test with that name!")

# Create group for test with test_id on loadero
def create_new_group(args, test_id, group_count, group_name):
    url="https://api.loadero.com/v2/projects/{0}/tests/{1}/groups/".format(args.project_id, test_id)
    payload=json.dumps({
        "count": group_count,
        "name": group_name
    })
    headers={}
    headers['Authorization']=args.auth_token
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
        sys.exit(1)   

# Create participant for test with test_id and group_id on loadero
def create_new_participant(args, test_id, group_id, participant_browser, participant_count, participant_name):
    url = "https://api.loadero.com/v2/projects/{0}/tests/{1}/groups/{2}/participants".format(args.project_id, test_id, group_id)
    payload=json.dumps({
        "browser": participant_browser,
        "count": participant_count,
        "name": participant_name
    })
    headers={}
    headers['Authorization']=args.auth_token
    headers['Content-Type']='application.json'
    
    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==201):
            print("Successfully created new participant!")

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

# Get test_id for excisting test on loadero and write it to a file
def get_test_with_id(args, test_id, test_name):
    url = "https://api.loadero.com/v2/projects/{0}/tests/{1}/".format(args.project_id, test_id)
    payload={}
    headers = {}
    headers['Authorization']=args.auth_token

    try:
        response=requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            test_info=json.dumps(json_response)
            absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name + '/testinfo.json')
            with open(absolute_path, "w") as f:
                f.write(test_info)

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

# Get all existing asserts for test
def get_all_asserts(args, test_id, test_name):
    url = "https://api.loadero.com/v2/projects/{0}/tests/{1}/asserts".format(args.project_id, test_id)

    payload={}
    headers = {}
    headers['Authorization']=args.auth_token

    try:
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status()
        if(response.status_code==200):
            json_response=response.json()
            #print(json_response)
            results=json_response['results']
            #print(results)
            asserts=json.dumps(results)
            absolute_path=os.path.abspath('test_cases/' + str(test_id) + '_' + test_name + '/asserts.json')
            with open(absolute_path, "w") as f:
                f.write(asserts)

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)

def create_new_assert(args, test_id, expected, operator, path):
    url = "https://api.loadero.com/v2/projects/{0}/tests/{1}/asserts".format(args.project_id, test_id)
    payload = json.dumps({
    "expected": expected,
    "operator": operator,
    "path": path
    })
    headers = {}
    headers['Authorization']=args.auth_token
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
        sys.exit(1)
