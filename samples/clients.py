from createsend import *

auth = {
  'access_token': 'YOUR_ACCESS_TOKEN',
  'refresh_token': 'YOUR_REFRESH_TOKEN' }
clientId = 'YOUR_CLIENT_ID'

cs = CreateSend(auth)
client = Client(auth, clientId)

# Get list of sent campaigns
print("List of sent campaigns:")
campaigns = []
pageNumber = 1
pagedCampaigns = client.campaigns(page = 1)
numberOfPages = pagedCampaigns.NumberOfPages
while pageNumber <= numberOfPages:
  if (pageNumber > 1):
    pagedCampaigns = client.campaigns(page = pageNumber)
  
  print("  Page: %d" % pageNumber)
  for cm in pagedCampaigns.Results:
    print("    - %s" % cm.Subject)
  
  pageNumber = pageNumber + 1

# Get list of drafts campaigns
print("List of drafts campaigns:")
for cm in client.drafts():
  print("  - %s" % cm.Subject)

# Get list of scheduled campaigns
print("List of scheduled campaigns:")
for cm in client.scheduled():
  print("  - %s" % cm.Subject)

# Get list of tags
print("List of tags:")
for tag in client.tags():
  print("  Tag: %s - NumberOfCampaigns: %d" % (tag.Name, tag.NumberOfCampaigns))