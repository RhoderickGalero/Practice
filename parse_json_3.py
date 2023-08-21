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

# Extracting login values and assigning them to a variable
logins = [item["assignees"][0]["login"] for item in data if item["assignees"]]
print(logins)  # This will print a list of logins
