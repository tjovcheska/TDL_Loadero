import loadero.cloner as Cloner
import argparse

def parse_arguments():

    parser = argparse.ArgumentParser()

    parser.add_argument('--auth_token_from', help='Authentication Token From', default='', required=False)
    parser.add_argument('--project_id_from', help='Project Id From', default=0, required=False)
    parser.add_argument('--auth_token_to', help='Authentication Token To', default='', required=False)
    parser.add_argument('--project_id_to', help='Project Id To', default=0, required=False)

    parser.add_argument('--test_ids', help='Test Ids', default=[], required=False, nargs="*", type=int)
    parser.add_argument('--action', help='Actions: backup, restore, clone', default='clone', required=False)

    args = parser.parse_args()
    return args

def main():
    args=parse_arguments()

    class switch(object):
        value = None
        def __new__(class_, value):
            class_.value = value
            return True

    def case(*args):
        return any((arg == switch.value for arg in args))

    if (args.project_id_from != 0 or args.project_id_to != 0) and (len(args.auth_token_from) != 0 or len(args.auth_token_to) != 0):

        while switch(args.action):
            if case('backup'):
                Cloner.backup_tests(args.project_id_from, args.auth_token_from, args.test_ids)
                break
            if case('restore'):
                Cloner.restore_tests(args.project_id_to, args.auth_token_to, args.test_ids)
                break
            if case('clone'):
                Cloner.backup_tests(args.project_id_from, args.auth_token_from, args.test_ids)
                Cloner.restore_tests(args.project_id_to, args.auth_token_to, args.test_ids)
                break
            if case('default'):
                break

        else:
            print('Invalid parameters!')

main()
