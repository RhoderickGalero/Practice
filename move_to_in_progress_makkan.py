import subprocess


def list_projects():
    cmd = 'gh project list --owner RhoderickGalero'
    return run_cmd(cmd)


def list_items():
    cmd = 'gh project item-list 6 --owner RhoderickGalero --format json'
    return run_cmd(cmd)


def move_to_in_progress(issue_id):
    cmd = 'gh project item-edit --id {0} --field-id "PVTSSF_lAHOBbg8Ns4AT02azgMqiD8" --project-id PVT_kwHOBbg8Ns4AT02a --single-select-option-id "47fc9ee4"'.format(issue_id)
    return run_cmd(cmd)
    

def run_cmd(cmd):
    print('Running cmd "{0}"'.format(cmd))
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, text=True)
    out, err = result.stdout, result.stderr
    #print("Out: {0}".format(out))
    #print("Err: {0}".format(err))
    return out


def print_auth_info():
    run_cmd('gh auth status')


def print_gh_version():
    run_cmd('gh version')


def main():
    print_gh_version()
    print_auth_info()
    projects = list_projects()
    #print("Projects: {0}".format(projects))
    project_items = list_items()
    print("Project items: {0}".format(project_items))
    #issue_nr = os.getenv("ISSUE_NR")
    #TODO get issue_id from issue_nr
    #move_to_in_progress(issue_nr)
    #print(f"Moved Issue #{issue_nr} to 'InProgress'")


if __name__ == "__main__":
    main()
