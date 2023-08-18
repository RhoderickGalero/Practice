import os
import subprocess
import json

def get_assigned_issues():
#     command = "gh issue list --json number,title,state,assignees"
    command = "gh project item-list --owner RhoderickGalero --format json id,assignees"
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)
    output = result.stdout.strip()
    issues = json.loads(output)
    assigned_issues = [issue for issue in issues if issue["assignees"] is not None]
    return assigned_issues
    print (assigned_issues)

def move_to_in_progress(issue_number):
 #   command = f"gh issue edit {issue_number} --add-label 'InProgress' --remove-label 'Todo'"
 #   command = f"gh project item-edit --id issue_id --field-id "PVTSSF_lAHOBbg8Ns4AT02azgMqiD8" --project-id PVT_kwHOBbg8Ns4AT02a --single-select-option-id "47fc9ee4"
    subprocess.run(command, shell=True)

def main():
    assigned_issues = get_assigned_issues()
    
    for issue in assigned_issues:
        issue_number = issue["number"]
        move_to_in_progress(issue_number)
        print(f"Moved Issue #{issue_number} to 'InProgress'")

if __name__ == "__main__":
    main()
