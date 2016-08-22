print("Starting request from client")

import myclient

client = myclient.MyClient()
resp = client.send_to_server('generate_names.py')

print(resp)


resp = client.send_to_server('generate_data.py', {"which_athlete" : "Mikey McManus"})
print(resp)

