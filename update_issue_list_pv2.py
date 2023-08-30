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
mutation (
          $project: PVT_kwHOBbg8Ns4AT02a!
          $item: PVTI_lAHOBbg8Ns4AT02azgIj6xo!
          $status_field: PVTSSF_lAHOBbg8Ns4AT02azgMqiD8!
          $status_value: 47fc9ee4!
        ) {
          set_status: updateProjectV2ItemFieldValue(input: {
            projectId: $project
            itemId: $item
            fieldId: $status_field
            value: {
              singleSelectOptionId: $status_value
              }
          }) {
            projectV2Item {
              id
              }
          }
}
"""
    

    response = requests.post(url, json={"query": query}, headers=headers)
    print (response)

    if response.status_code == 200:
        data = response.json()
#        print (data)
#        issues = data["data"]["repository"]["projectV2"]["items"]["edges"]
        
#        print (issues)
        return issues
    else:
        print("Failed to retrieve issues:", response.text)
        return None

if __name__ == "__main__":
    issues = get_repository_issues()
'''
    for item in issues:
        assignees_edges = item['node']['content']['assignees']['edges']
        if assignees_edges:
            node_id = item['node']['id']
            print (node_id)
#            empty_assignees_node_ids.append(node_id)

#print(empty_assignees_node_ids)
'''