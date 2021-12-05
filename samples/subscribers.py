from createsend import *

auth = {
  'access_token': 'YOUR_ACCESS_TOKEN',
  'refresh_token': 'YOUR_REFRESH_TOKEN' }
listId = 'YOUR_LIST_ID'
emailAddress = 'YOUR_SUBSCRIBER_EMAIL_ADDRESS'

subscriber = Subscriber(auth, listId, emailAddress)

# Get the details for a subscriber
subscriberDetail = subscriber.get()
for property, value in vars(subscriberDetail).items():
  print(property, ":", value)
