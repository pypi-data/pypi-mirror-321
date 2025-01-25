# GetStockItemTypeInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_info** | [**List[StockItemTypeInfo]**](StockItemTypeInfo.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_stock_item_type_info_response import GetStockItemTypeInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemTypeInfoResponse from a JSON string
get_stock_item_type_info_response_instance = GetStockItemTypeInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetStockItemTypeInfoResponse.to_json())

# convert the object into a dict
get_stock_item_type_info_response_dict = get_stock_item_type_info_response_instance.to_dict()
# create an instance of GetStockItemTypeInfoResponse from a dict
get_stock_item_type_info_response_from_dict = GetStockItemTypeInfoResponse.from_dict(get_stock_item_type_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


