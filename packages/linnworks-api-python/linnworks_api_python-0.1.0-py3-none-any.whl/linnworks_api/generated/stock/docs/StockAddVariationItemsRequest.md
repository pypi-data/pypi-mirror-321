# StockAddVariationItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_variation_item_id** | **str** | The variation group id | [optional] 
**pk_stock_item_ids** | **List[str]** | The list of item ids to add | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_add_variation_items_request import StockAddVariationItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockAddVariationItemsRequest from a JSON string
stock_add_variation_items_request_instance = StockAddVariationItemsRequest.from_json(json)
# print the JSON string representation of the object
print(StockAddVariationItemsRequest.to_json())

# convert the object into a dict
stock_add_variation_items_request_dict = stock_add_variation_items_request_instance.to_dict()
# create an instance of StockAddVariationItemsRequest from a dict
stock_add_variation_items_request_from_dict = StockAddVariationItemsRequest.from_dict(stock_add_variation_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


