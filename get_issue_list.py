import requests

# Replace with your GitHub Personal Access Token and repository details
ACCESS_TOKEN = "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"
REPO_OWNER = "RhoderickGalero"
REPO_NAME = "Practice"

def get_repository_issues():
    url = "https://api.github.com/graphql"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    query = """
    {
        repository(owner: "%s", name: "%s") {
            issues(first: 10) {
                nodes {
                    title
                    state
                    createdAt
                }
            }
        }
    }
    """ % (REPO_OWNER, REPO_NAME)

    response = requests.post(url, json={"query": query}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        issues = data["data"]["repository"]["issues"]["nodes"]
        return issues
    else:
        print("Failed to retrieve issues:", response.text)
        return None

if __name__ == "__main__":
    issues = get_repository_issues()
    if issues:
        for issue in issues:
            title = issue["title"]
            state = issue["state"]
            created_at = issue["createdAt"]
            print(f"Title: {title}\nState: {state}\nCreated At: {created_at}\n")
