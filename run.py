import loadero.runner as Runner
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--auth_token', help='Authentication Token', default='', required=True)
    parser.add_argument('--project_id', help='Project Id', default=0, required=True)
    parser.add_argument('--test_id', help='Test Id', default=0, required=True)

    args = parser.parse_args()
    return args

def main():
    args=parse_arguments()

    if args.project_id!= 0 and len(args.auth_token) != 0 and args.test_id != 0:

        Runner.run_test(args, 1)

main()
