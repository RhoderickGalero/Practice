data = {
    "items": [
        {
            "assignees": ["RhoderickGalero"],
            "content": {
                "type": "Issue",
                "body": "",
                "title": "issue new issue move to project",
                "number": 3,
                "repository": "RhoderickGalero/Practice",
                "url": "https://github.com/RhoderickGalero/Practice/issues/3"
            },
            "id": "PVTI_lAHOBbg8Ns4AT02azgIj6xo",
            "repository": "https://github.com/RhoderickGalero/Practice",
            "status": "Todo",
            "title": "issue new issue move to project"
        },
        {
            "assignees": ["RhoderickGalero"],
            "content": {
                "type": "Issue",
                "body": "import issue to project",
                "title": "Issue move import",
                "number": 2,
                "repository": "RhoderickGalero/Practice",
                "url": "https://github.com/RhoderickGalero/Practice/issues/2"
            },
            "id": "PVTI_lAHOBbg8Ns4AT02azgIkKF4",
            "repository": "https://github.com/RhoderickGalero/Practice",
            "status": "Todo",
            "title": "Issue move import"
        },
        {
            "assignees": ["RhoderickGalero"],
            "content": {
                "type": "Issue",
                "body": "assign and move to in progress",
                "title": "issue assign",
                "number": 4,
                "repository": "RhoderickGalero/Practice",
                "url": "https://github.com/RhoderickGalero/Practice/issues/4"
            },
            "id": "PVTI_lAHOBbg8Ns4AT02azgIj620",
            "repository": "https://github.com/RhoderickGalero/Practice",
            "status": "InProgress",
            "title": "issue assign"
        }
    ],
    "totalCount": 3
}

# Extracting titles and assigning them to a variable
issue_titles = [item["content"] for item in data["items"]]
print(issue_titles)  # This will print a list of issue titles