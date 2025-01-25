# GetEmailsSentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.get_emails_sent_request import GetEmailsSentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailsSentRequest from a JSON string
get_emails_sent_request_instance = GetEmailsSentRequest.from_json(json)
# print the JSON string representation of the object
print(GetEmailsSentRequest.to_json())

# convert the object into a dict
get_emails_sent_request_dict = get_emails_sent_request_instance.to_dict()
# create an instance of GetEmailsSentRequest from a dict
get_emails_sent_request_from_dict = GetEmailsSentRequest.from_dict(get_emails_sent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


