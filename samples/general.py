from createsend import *

auth = {
  'access_token': 'YOUR_ACCESS_TOKEN',
  'refresh_token': 'YOUR_REFRESH_TOKEN' }

cs = CreateSend(auth)
clients = cs.clients()

# Get list of clients 
for cl in clients:
  print(f"Client: {cl.Name} - Id: {cl.ClientID}")