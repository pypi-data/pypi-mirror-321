# StockDeleteVariationItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DeleteVariationItemsRequest**](DeleteVariationItemsRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_delete_variation_items_request import StockDeleteVariationItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockDeleteVariationItemsRequest from a JSON string
stock_delete_variation_items_request_instance = StockDeleteVariationItemsRequest.from_json(json)
# print the JSON string representation of the object
print(StockDeleteVariationItemsRequest.to_json())

# convert the object into a dict
stock_delete_variation_items_request_dict = stock_delete_variation_items_request_instance.to_dict()
# create an instance of StockDeleteVariationItemsRequest from a dict
stock_delete_variation_items_request_from_dict = StockDeleteVariationItemsRequest.from_dict(stock_delete_variation_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


