from createsend import *

auth = {
  'access_token': 'YOUR_ACCESS_TOKEN',
  'refresh_token': 'YOUR_REFRESH_TOKEN' }
segmentId = 'YOUR_SEGMENT_ID'

segment = Segment(auth, segmentId)

# Get list of active subscribers in a segment
print("List of active subscribers:")
for cm in segment.subscribers().Results:
  print("  - %s" % cm.EmailAddress)