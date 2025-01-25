# StockDeleteVariationItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_variation_item_id** | **str** | The variation group id | [optional] 
**pk_stock_item_id** | **str** | The stock item id to add | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_delete_variation_item_request import StockDeleteVariationItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockDeleteVariationItemRequest from a JSON string
stock_delete_variation_item_request_instance = StockDeleteVariationItemRequest.from_json(json)
# print the JSON string representation of the object
print(StockDeleteVariationItemRequest.to_json())

# convert the object into a dict
stock_delete_variation_item_request_dict = stock_delete_variation_item_request_instance.to_dict()
# create an instance of StockDeleteVariationItemRequest from a dict
stock_delete_variation_item_request_from_dict = StockDeleteVariationItemRequest.from_dict(stock_delete_variation_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


