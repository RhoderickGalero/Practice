import os
import subprocess
import json


def list_project():
    cmd = 'gh project item-list 6 --owner RhoderickGalero'
    return run_cmd(cmd)


def move_to_in_progress(issue_id):
    cmd = 'gh project item-edit --id {0} --field-id "PVTSSF_lAHOBbg8Ns4AT02azgMqiD8" --project-id PVT_kwHOBbg8Ns4AT02a --single-select-option-id "47fc9ee4"'.format(issue_id)
    print(run_cmd(cmd))
    

def run_cmd(cmd):
    print('Running cmd "{0}"'.format(cmd))
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, text=True)
    return result.stdout.strip()


def print_auth_info():
    print(run_cmd('gh auth status'))


def print_envs():
    for name, value in os.environ.items():
        print("{0}: {1}".format(name, value))


def main():
    print_auth_info()
    project_items = list_project()
    print("Project items:")
    print(project_items)
    issue_nr = os.getenv("ISSUE_NR")
    #TODO get issue_id from issue_nr
    move_to_in_progress(issue_nr)
    print(f"Moved Issue #{issue_nr} to 'InProgress'")


if __name__ == "__main__":
    main()
