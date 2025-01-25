# GetStockItemTypeInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skus** | **List[str]** |  | [optional] 
**stock_item_int_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_stock_item_type_info_request import GetStockItemTypeInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemTypeInfoRequest from a JSON string
get_stock_item_type_info_request_instance = GetStockItemTypeInfoRequest.from_json(json)
# print the JSON string representation of the object
print(GetStockItemTypeInfoRequest.to_json())

# convert the object into a dict
get_stock_item_type_info_request_dict = get_stock_item_type_info_request_instance.to_dict()
# create an instance of GetStockItemTypeInfoRequest from a dict
get_stock_item_type_info_request_from_dict = GetStockItemTypeInfoRequest.from_dict(get_stock_item_type_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


