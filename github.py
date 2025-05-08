import requests 

def BuscarDadosnoGithub(username):
    UrlUser = f"https://api.github.com/users/{username}"
    UrlRepos = f"https://api.github.com/users/{username}/repos?per_page=100"
    
    UserResponse = requests.get(UrlUser)
    ReposResponse = requests.get(UrlRepos)
    
    if UserResponse.status_code != 200 or ReposResponse.status_code != 200:
        return None
        
    UserData = UserResponse.json()
    ReposData = ReposResponse.json()
    
    return {
        "user": {
            "name": UserData.get("name"),
            "followers": UserData.get("followers"),
            "following": UserData.get("following"),
            "public_repos": UserData.get("public_repos")
        },
        "repos": [
            { 
                "name": repo["name"],
                "stars": repo["stargazers_count"],
                "created_at": repo["created_at"],
                "updated_at": repo["updated_at"]
            } for repo in ReposData
        ]
    }