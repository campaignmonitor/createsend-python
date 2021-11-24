***REMOVED***

auth = {
***REMOVED***'access_token': 'YOUR_ACCESS_TOKEN',
***REMOVED***'refresh_token': 'YOUR_REFRESH_TOKEN' }
campaignId = 'YOUR_CAMPAIGN_ID'

campaign = Campaign(auth, campaignId)

# Get the summary info for a campaign
summary = campaign.summary()
for property, value in vars(summary).items():
***REMOVED***print(property, ":", value)