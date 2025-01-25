# UpdateSkuGroupIdentifierRequestItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku_group_id** | **int** |  | [optional] 
**sku_group_identifier_type** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.update_sku_group_identifier_request_items import UpdateSkuGroupIdentifierRequestItems

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSkuGroupIdentifierRequestItems from a JSON string
update_sku_group_identifier_request_items_instance = UpdateSkuGroupIdentifierRequestItems.from_json(json)
# print the JSON string representation of the object
print(UpdateSkuGroupIdentifierRequestItems.to_json())

# convert the object into a dict
update_sku_group_identifier_request_items_dict = update_sku_group_identifier_request_items_instance.to_dict()
# create an instance of UpdateSkuGroupIdentifierRequestItems from a dict
update_sku_group_identifier_request_items_from_dict = UpdateSkuGroupIdentifierRequestItems.from_dict(update_sku_group_identifier_request_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


