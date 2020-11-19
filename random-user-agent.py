import urllib.request
import random

gist_url = "https://gist.githubusercontent.com/xenobyte/f878502c3bffb5cf54672145994cdcfa/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt"

user_agents = []

for line in urllib.request.urlopen(gist_url):
    user_agents.append(line)
print(random.choice(user_agents).decode('UTF-8'))
