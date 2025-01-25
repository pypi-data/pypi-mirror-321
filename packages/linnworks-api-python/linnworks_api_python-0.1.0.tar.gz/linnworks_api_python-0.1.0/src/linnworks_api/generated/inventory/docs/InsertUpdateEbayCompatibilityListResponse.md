# InsertUpdateEbayCompatibilityListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ebay_compatibility_list** | [**List[StockItemEbayCompatibility]**](StockItemEbayCompatibility.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.insert_update_ebay_compatibility_list_response import InsertUpdateEbayCompatibilityListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsertUpdateEbayCompatibilityListResponse from a JSON string
insert_update_ebay_compatibility_list_response_instance = InsertUpdateEbayCompatibilityListResponse.from_json(json)
# print the JSON string representation of the object
print(InsertUpdateEbayCompatibilityListResponse.to_json())

# convert the object into a dict
insert_update_ebay_compatibility_list_response_dict = insert_update_ebay_compatibility_list_response_instance.to_dict()
# create an instance of InsertUpdateEbayCompatibilityListResponse from a dict
insert_update_ebay_compatibility_list_response_from_dict = InsertUpdateEbayCompatibilityListResponse.from_dict(insert_update_ebay_compatibility_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


