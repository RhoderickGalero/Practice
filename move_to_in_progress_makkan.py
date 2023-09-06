import os
import subprocess
import json


def get_assigned_issues():
    issues = json.loads(run_cmd('gh issue list --json number,title,state,assignees'))
    assigned_issues = [issues for issues in issues if issues["assignees"] is not None]
    return assigned_issues


def list_project():
    cmd = 'gh project item-list 6 --owner RhoderickGalero'
    return run_cmd(cmd)


def move_to_in_progress(issue_nr):
    cmd = 'gh project item-edit --id issue_id --field-id "PVTSSF_lAHOBbg8Ns4AT02azgMqiD8" --project-id PVT_kwHOBbg8Ns4AT02a --single-select-option-id "47fc9ee4"'
    print(run_cmd(cmd))
    

def run_cmd(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, text=True)
    return result.stdout.strip()


def print_envs():
    for name, value in os.environ.items():
        print("{0}: {1}".format(name, value))


def main():
    print("Envs")
    print_envs()
    assigned_issues = get_assigned_issues()
    project_items = list_project()
    print("Project items")
    print(project_items)
    for issue in assigned_issues:
        issue_number = issue["number"]
        move_to_in_progress(issue_number)
        print(f"Moved Issue #{issue_number} to 'InProgress'")


if __name__ == "__main__":
    main()
