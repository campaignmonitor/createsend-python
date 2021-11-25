***REMOVED***

auth = {
***REMOVED***'access_token': 'YOUR_ACCESS_TOKEN',
***REMOVED***'refresh_token': 'YOUR_REFRESH_TOKEN' }
clientId = 'YOUR_CLIENT_ID'


cs = CreateSend(auth)
client = Client(auth, clientId)

# Get list of sent campaigns
print("List of sent campaigns:")
pageNumber = 1
pagedCampaigns = client.campaigns(page = 1)
numberOfPages = pagedCampaigns.NumberOfPages
while pageNumber <= numberOfPages:
***REMOVED***if (pageNumber > 1):
***REMOVED******REMOVED***pagedCampaigns = client.campaigns(page = pageNumber)
***REMOVED***
***REMOVED***print("***REMOVED***Page: %d" % pageNumber)
***REMOVED***for cm in pagedCampaigns.Results:
***REMOVED******REMOVED***print("***REMOVED******REMOVED***- %s" % cm.Subject)
***REMOVED***
***REMOVED***pageNumber = pageNumber + 1

***REMOVED***
# Get list of sent campaigns filtered by tags and date
print("List of sent campaigns at 2021 with ABTest tag:")
pageNumber = 1
pagedCampaigns = client.campaigns(page = 1, sent_from_date="2021-01-01", sent_to_date="2022-01-01", tags="ABTest")
numberOfPages = pagedCampaigns.NumberOfPages
while pageNumber <= numberOfPages:
***REMOVED***if (pageNumber > 1):
***REMOVED******REMOVED***pagedCampaigns = client.campaigns(page = pageNumber, sent_from_date="2021-01-01", sent_to_date="2022-01-01", tags="ABTest")
***REMOVED***
***REMOVED***print("***REMOVED***Page: %d" % pageNumber)
***REMOVED***for cm in pagedCampaigns.Results:
***REMOVED******REMOVED***print("***REMOVED******REMOVED***- %s" % cm.Subject)
***REMOVED***
***REMOVED***pageNumber = pageNumber + 1

# Get list of drafts campaigns
print("List of drafts campaigns:")
for cm in client.drafts():
***REMOVED***print("***REMOVED***- %s" % cm.Subject)

# Get list of scheduled campaigns
print("List of scheduled campaigns:")
for cm in client.scheduled():
***REMOVED***print("***REMOVED***- %s" % cm.Subject)

# Get list of tags
print("List of tags:")
for tag in client.tags():
***REMOVED***print("***REMOVED***Tag: %s - NumberOfCampaigns: %d" % (tag.Name, tag.NumberOfCampaigns))