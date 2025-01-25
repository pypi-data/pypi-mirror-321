# GetStockItemsLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_locations** | [**List[StockLocationStockItemId]**](StockLocationStockItemId.md) |  | [optional] 
**auth_token** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**vendor_friendly_name** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_stock_items_location_request import GetStockItemsLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemsLocationRequest from a JSON string
get_stock_items_location_request_instance = GetStockItemsLocationRequest.from_json(json)
# print the JSON string representation of the object
print(GetStockItemsLocationRequest.to_json())

# convert the object into a dict
get_stock_items_location_request_dict = get_stock_items_location_request_instance.to_dict()
# create an instance of GetStockItemsLocationRequest from a dict
get_stock_items_location_request_from_dict = GetStockItemsLocationRequest.from_dict(get_stock_items_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


