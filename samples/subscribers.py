***REMOVED***

auth = {
***REMOVED***'access_token': 'YOUR_ACCESS_TOKEN',
***REMOVED***'refresh_token': 'YOUR_REFRESH_TOKEN' }
listId = 'YOUR_LIST_ID'
emailAddress = 'YOUR_SUBSCRIBER_EMAIL_ADDRESS'

subscriberName = "YOUR_SUBSCRIBER_NAME"
subscriberCustomFields = []
subscriberResubscribed = False
subscriberConsentToTrack = 'Unchanged'
subscriberMobileNumber = "+61491570006" # This is a reserved mobile number by the Australian Communications and Media Authority
subscriberConsentToSendSms = "Yes"

subscriber = Subscriber(auth, listId, emailAddress)

# Get the details for a subscriber
***REMOVED***
***REMOVED***
***REMOVED***print(property, ":", value)
***REMOVED***
# Adding a subscriber
***REMOVED***#This implemntation defaults the value of 'restart_subscription_based_autoresponders' to false
subscriber.add(listId, emailAddress, subscriberName, subscriberCustomFields, subscriberResubscribed, subscriberConsentToTrack)

# Adding a subscriber with a mobile number
***REMOVED***#This implemntation defaults the value of 'restart_subscription_based_autoresponders' to false
***REMOVED***#This also sets the default value of 'consent_to_track_sms' to 'unchanged', meaning new users will not receive SMS communications by default."
subscriber.add(listId, emailAddress, subscriberName, subscriberCustomFields, subscriberConsentToTrack, mobile_Number=subscriberMobileNumber)

#Alternative to set SMS tracking permissions 
***REMOVED***# This implemntation defaults the value of 'restart_subscription_based_autoresponders' to false
subscriber.add(listId, emailAddress, subscriberName, subscriberCustomFields, subscriberConsentToTrack, mobile_Number=subscriberMobileNumber, consent_to_track_sms=subscriberConsentToSendSms)
