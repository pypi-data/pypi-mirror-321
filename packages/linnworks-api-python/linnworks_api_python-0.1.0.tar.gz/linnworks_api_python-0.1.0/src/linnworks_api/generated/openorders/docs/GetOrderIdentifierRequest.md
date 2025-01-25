# GetOrderIdentifierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.get_order_identifier_request import GetOrderIdentifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderIdentifierRequest from a JSON string
get_order_identifier_request_instance = GetOrderIdentifierRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrderIdentifierRequest.to_json())

# convert the object into a dict
get_order_identifier_request_dict = get_order_identifier_request_instance.to_dict()
# create an instance of GetOrderIdentifierRequest from a dict
get_order_identifier_request_from_dict = GetOrderIdentifierRequest.from_dict(get_order_identifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


