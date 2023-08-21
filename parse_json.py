import json

json_text = '''
{
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
'''

data = json.loads(json_text)

for item in data["items"]:
#    item_id = item["id"]
    print (item["type"])
    item_status = item["status"]
#    print("ID:", item_id)
    print("Status:", item_status)
    print("-" * 20)
