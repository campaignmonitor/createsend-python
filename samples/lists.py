from createsend import *

auth = {
  'access_token': 'YOUR_ACCESS_TOKEN',
  'refresh_token': 'YOUR_REFRESH_TOKEN' }
listId = 'YOUR_LIST_ID'

list = List(auth, listId)

# Get list of active subscribers in a list
print("List of active subscribers:")
for cm in list.active().Results:
  print("  - %s" % cm.EmailAddress)

# Get list of bounced subscribers in a list
print("List of bounced subscribers:")
for cm in list.bounced().Results:
  print("  - %s" % cm.EmailAddress)

# Get list of unconfirmed subscribers in a list
print("List of unconfirmed subscribers:")
for cm in list.unconfirmed().Results:
  print("  - %s" % cm.EmailAddress)
  
# Get list of unsubscribed subscribers in a list
print("List of unsubscribed subscribers:")
for cm in list.unsubscribed().Results:
  print("  - %s" % cm.EmailAddress)

# Get list of deleted subscribers in a list
print("List of deleted subscribers:")
for cm in list.deleted().Results:
  print("  - %s" % cm.EmailAddress)