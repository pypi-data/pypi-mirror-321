# UpdateSkuGroupIdentifierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**List[UpdateSkuGroupIdentifierRequestItems]**](UpdateSkuGroupIdentifierRequestItems.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.update_sku_group_identifier_request import UpdateSkuGroupIdentifierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSkuGroupIdentifierRequest from a JSON string
update_sku_group_identifier_request_instance = UpdateSkuGroupIdentifierRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSkuGroupIdentifierRequest.to_json())

# convert the object into a dict
update_sku_group_identifier_request_dict = update_sku_group_identifier_request_instance.to_dict()
# create an instance of UpdateSkuGroupIdentifierRequest from a dict
update_sku_group_identifier_request_from_dict = UpdateSkuGroupIdentifierRequest.from_dict(update_sku_group_identifier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


