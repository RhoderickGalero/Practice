import os
import subprocess
import json

def get_assigned_issues():
#    command = "gh issue list --json number,title,state,assignees"
    command = "gh project item-list --owner RhoderickGalero 6 --format json "
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)
#    print (result)
#    print("-" * 20)
    output = result.stdout.strip()
#    print (output)
#    print("-" * 20)

    data = json.loads(output)
 #   print (data)
 #   assigned_issues = ['id' for item in issue['items'] if 'assignees' in item is not None]
    assigned_issues = [item for item in data['items'] if 'assignees' not in item]
    return assigned_issues
    

def move_to_in_progress(issue_number):
#    command = f"gh issue edit {issue_number} --add-label 'In Progress' --remove-label 'To Do'"
    command = f"gh project item-edit --id {issue_number} --field-id PVTSSF_lAHOBbg8Ns4AT02azgMqiD8 --project-id PVT_kwHOBbg8Ns4AT02a --single-select-option-id 47fc9ee4"
    subprocess.run(command, shell=True)

def main():
    assigned_issues = get_assigned_issues()
    
    for issue in assigned_issues:
        issue_number = issue['id']
#        move_to_in_progress(issue_number)
        print(f"Moved Issue # {issue_number} to 'In Progress'")

if __name__ == "__main__":
    main()
