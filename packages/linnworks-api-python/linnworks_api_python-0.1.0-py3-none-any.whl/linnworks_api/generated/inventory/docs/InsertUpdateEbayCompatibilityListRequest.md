# InsertUpdateEbayCompatibilityListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ebay_compatibility_list** | [**List[StockItemEbayCompatibility]**](StockItemEbayCompatibility.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.insert_update_ebay_compatibility_list_request import InsertUpdateEbayCompatibilityListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InsertUpdateEbayCompatibilityListRequest from a JSON string
insert_update_ebay_compatibility_list_request_instance = InsertUpdateEbayCompatibilityListRequest.from_json(json)
# print the JSON string representation of the object
print(InsertUpdateEbayCompatibilityListRequest.to_json())

# convert the object into a dict
insert_update_ebay_compatibility_list_request_dict = insert_update_ebay_compatibility_list_request_instance.to_dict()
# create an instance of InsertUpdateEbayCompatibilityListRequest from a dict
insert_update_ebay_compatibility_list_request_from_dict = InsertUpdateEbayCompatibilityListRequest.from_dict(insert_update_ebay_compatibility_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


