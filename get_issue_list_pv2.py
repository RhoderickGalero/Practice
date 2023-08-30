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
            projectV2(number: 6) {
                id
                items(first: 10) {
                    edges {
                        node {
                            id
                            content {
                                ... on Issue {
                                    id
                                    assignees(first: 10) {
                                        edges {
                                            node {
                                                id
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            } 
        }
    }
    """ % (REPO_OWNER, REPO_NAME)

    response = requests.post(url, json={"query": query}, headers=headers)
#    print (response)

    if response.status_code == 200:
        data = response.json()
#        print (data)
        issues = data["data"]["repository"]["projectV2"]["items"]["edges"]
        
        print (issues)
        return issues
    else:
        print("Failed to retrieve issues:", response.text)
        return None

if __name__ == "__main__":
    issues = get_repository_issues()

    for item in issues:
        assignees_edges = item['node']['content']['assignees']['edges']
        if assignees_edges:
            node_id = item['node']['id']
            print (node_id)
#            empty_assignees_node_ids.append(node_id)

#print(empty_assignees_node_ids)
