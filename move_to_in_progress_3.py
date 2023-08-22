import os
import subprocess
import json

def get_assigned_issues():
    command = "gh issue list --json number,title,state,assignees"
    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)
    output_lines = result.stdout.strip().split('\n')
    assigned_issues = []

    for line in output_lines:
        issue_data = json.loads(line)
        if issue_data.get("assignees"):
            assigned_issues.append(issue_data)

    return assigned_issues
    print (assigned_issues)

def move_to_in_progress(issue_number):
    command = f"gh issue edit {issue_number} --add-label 'In Progress' --remove-label 'To Do'"
    subprocess.run(command, shell=True)

def main():
    assigned_issues = get_assigned_issues()

    for issue in assigned_issues:
        issue_number = issue["number"]
        move_to_in_progress(issue_number)
        print(f"Moved Issue #{issue_number} to 'In Progress'")

if __name__ == "__main__":
    main()