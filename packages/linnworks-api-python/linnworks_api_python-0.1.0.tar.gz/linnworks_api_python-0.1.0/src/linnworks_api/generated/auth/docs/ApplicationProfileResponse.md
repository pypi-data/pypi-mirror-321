# ApplicationProfileResponse

Represents Linnworks.net application subscription profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_tag** | **str** | Plan Tag as defined in your Application Configuration | [optional] 
**plan_name** | **str** | Plan Name as defined in your application Configuration | [optional] 
**activation_date** | **datetime** | Date when the profile was signed up for, or resubscribed | [optional] 
**last_payment_date** | **datetime** | Last Payment date | [optional] 
**next_payment_date** | **datetime** | Next payment date | [optional] 
**profile_expires** | **datetime** | When profile is due to expire | [optional] 
**is_profile_active** | **bool** | Indicates whether the payment profile is active for the application, if this is set to false it means the customer canceled the profile but the profile is still active due last payment made in the last month. | [optional] 

## Example

```python
from linnworks_api.generated.auth.models.application_profile_response import ApplicationProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationProfileResponse from a JSON string
application_profile_response_instance = ApplicationProfileResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationProfileResponse.to_json())

# convert the object into a dict
application_profile_response_dict = application_profile_response_instance.to_dict()
# create an instance of ApplicationProfileResponse from a dict
application_profile_response_from_dict = ApplicationProfileResponse.from_dict(application_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


