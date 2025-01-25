# GetStockItemsLocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_locations** | [**List[StockItemLocation]**](StockItemLocation.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_stock_items_location_response import GetStockItemsLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemsLocationResponse from a JSON string
get_stock_items_location_response_instance = GetStockItemsLocationResponse.from_json(json)
# print the JSON string representation of the object
print(GetStockItemsLocationResponse.to_json())

# convert the object into a dict
get_stock_items_location_response_dict = get_stock_items_location_response_instance.to_dict()
# create an instance of GetStockItemsLocationResponse from a dict
get_stock_items_location_response_from_dict = GetStockItemsLocationResponse.from_dict(get_stock_items_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


