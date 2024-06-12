import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get(url)

#automatically converts json to dictionary

if response.status_code == 200:
    pull_requests = response.json()

    pr_creaters = {}


    for request in pull_requests:
        element = request['user']['login']
        if element in pr_creaters:
            pr_creaters[element] += 1
        else:
            pr_creaters[element] = 1
    
for creater,count in pr_creaters.items():
    print(f"{creater}: {count}\n")


# listing ids of all pull requests

#for i in range(len(output)):
#    print(output[i]["id"])

#listing all login users 
#for element in output:
 #   print(output.count(element["user"]["login"]))
    


