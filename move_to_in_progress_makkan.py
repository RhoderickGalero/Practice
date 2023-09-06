import subprocess
import json


def get_assigned_issues():
    issues = json.loads(run_cmd('gh issue list --json number,title,state,assignees'))
    assigned_issues = [issues for issues in issues if issues["assignees"] is not None]
    return assigned_issues


def move_to_in_progress(issue_nr):
    cmd = 'gh project item-edit --id issue_id --field-id "PVTSSF_lAHOBbg8Ns4AT02azgMqiD8" --project-id PVT_kwHOBbg8Ns4AT02a --single-select-option-id "47fc9ee4"'
    print(run_cmd(cmd))
    

def run_cmd(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, text=True)
    return result.stdout.strip()


def main():
    assigned_issues = get_assigned_issues()
    
    for issue in assigned_issues:
        issue_number = issue["number"]
        move_to_in_progress(issue_number)
        print(f"Moved Issue #{issue_number} to 'InProgress'")

if __name__ == "__main__":
    main()
