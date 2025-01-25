# FindStockItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codes** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.find_stock_item_request import FindStockItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FindStockItemRequest from a JSON string
find_stock_item_request_instance = FindStockItemRequest.from_json(json)
# print the JSON string representation of the object
print(FindStockItemRequest.to_json())

# convert the object into a dict
find_stock_item_request_dict = find_stock_item_request_instance.to_dict()
# create an instance of FindStockItemRequest from a dict
find_stock_item_request_from_dict = FindStockItemRequest.from_dict(find_stock_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


