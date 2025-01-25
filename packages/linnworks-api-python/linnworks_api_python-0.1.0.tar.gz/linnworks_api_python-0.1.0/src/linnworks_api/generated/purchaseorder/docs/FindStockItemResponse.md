# FindStockItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PurchaseItemFound]**](PurchaseItemFound.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.find_stock_item_response import FindStockItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindStockItemResponse from a JSON string
find_stock_item_response_instance = FindStockItemResponse.from_json(json)
# print the JSON string representation of the object
print(FindStockItemResponse.to_json())

# convert the object into a dict
find_stock_item_response_dict = find_stock_item_response_instance.to_dict()
# create an instance of FindStockItemResponse from a dict
find_stock_item_response_from_dict = FindStockItemResponse.from_dict(find_stock_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


