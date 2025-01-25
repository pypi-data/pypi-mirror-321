# ChangeOrderIdentifierRequest

Add/remove from all orders in the request body to the provided tag

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | Primary key of the orders to assign/unassign the identifier to. | [optional] 
**tag** | **str** | Identifier tag to assign/unassign. E.g. AMAZON_PRIME | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.change_order_identifier_request import ChangeOrderIdentifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeOrderIdentifierRequest from a JSON string
change_order_identifier_request_instance = ChangeOrderIdentifierRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeOrderIdentifierRequest.to_json())

# convert the object into a dict
change_order_identifier_request_dict = change_order_identifier_request_instance.to_dict()
# create an instance of ChangeOrderIdentifierRequest from a dict
change_order_identifier_request_from_dict = ChangeOrderIdentifierRequest.from_dict(change_order_identifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


