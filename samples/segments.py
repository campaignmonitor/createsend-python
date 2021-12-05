***REMOVED***

auth = {
***REMOVED***'access_token': 'YOUR_ACCESS_TOKEN',
***REMOVED***'refresh_token': 'YOUR_REFRESH_TOKEN' }
segmentId = 'YOUR_SEGMENT_ID'

segment = Segment(auth, segmentId)

# Get list of active subscribers in a segment
print("List of active subscribers:")
for cm in segment.subscribers().Results:
***REMOVED***print("***REMOVED***- %s" % cm.EmailAddress)