# DeleteEbayCompatibilityListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ebay_compatibility_list** | [**List[StockItemEbayCompatibility]**](StockItemEbayCompatibility.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.delete_ebay_compatibility_list_response import DeleteEbayCompatibilityListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteEbayCompatibilityListResponse from a JSON string
delete_ebay_compatibility_list_response_instance = DeleteEbayCompatibilityListResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteEbayCompatibilityListResponse.to_json())

# convert the object into a dict
delete_ebay_compatibility_list_response_dict = delete_ebay_compatibility_list_response_instance.to_dict()
# create an instance of DeleteEbayCompatibilityListResponse from a dict
delete_ebay_compatibility_list_response_from_dict = DeleteEbayCompatibilityListResponse.from_dict(delete_ebay_compatibility_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


