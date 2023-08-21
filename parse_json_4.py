data = [
    {
        "assignees": [{"id": "U_kgDOBbg8Ng", "login": "RhoderickGalero", "name": ""}],
        "number": 4,
        "state": "OPEN",
        "title": "issue assign"
    },
    {
        "assignees": [{"id": "U_kgDOBbg8Ng", "login": "RhoderickGalero", "name": ""}],
        "number": 3,
        "state": "OPEN",
        "title": "issue new issue move to project"
    },
    {
        "assignees": [],
        "number": 2,
        "state": "OPEN",
        "title": "Issue move import"
    }
]

# Extracting assignees and assigning them to a variable
assignees = [item["number"] for item in data if item["assignees"] is not None ]
print(assignees)  # This will print a list of assignees lists
