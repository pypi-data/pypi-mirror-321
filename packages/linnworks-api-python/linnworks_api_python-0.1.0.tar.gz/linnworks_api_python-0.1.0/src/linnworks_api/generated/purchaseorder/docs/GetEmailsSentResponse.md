# GetEmailsSentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EmailSent]**](EmailSent.md) |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.get_emails_sent_response import GetEmailsSentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailsSentResponse from a JSON string
get_emails_sent_response_instance = GetEmailsSentResponse.from_json(json)
# print the JSON string representation of the object
print(GetEmailsSentResponse.to_json())

# convert the object into a dict
get_emails_sent_response_dict = get_emails_sent_response_instance.to_dict()
# create an instance of GetEmailsSentResponse from a dict
get_emails_sent_response_from_dict = GetEmailsSentResponse.from_dict(get_emails_sent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


