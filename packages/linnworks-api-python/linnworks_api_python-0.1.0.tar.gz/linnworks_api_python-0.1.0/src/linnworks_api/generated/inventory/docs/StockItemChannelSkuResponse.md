# StockItemChannelSkuResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** |  | [optional] 
**channel_skus** | [**List[StockItemChannelSKU]**](StockItemChannelSKU.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_channel_sku_response import StockItemChannelSkuResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemChannelSkuResponse from a JSON string
stock_item_channel_sku_response_instance = StockItemChannelSkuResponse.from_json(json)
# print the JSON string representation of the object
print(StockItemChannelSkuResponse.to_json())

# convert the object into a dict
stock_item_channel_sku_response_dict = stock_item_channel_sku_response_instance.to_dict()
# create an instance of StockItemChannelSkuResponse from a dict
stock_item_channel_sku_response_from_dict = StockItemChannelSkuResponse.from_dict(stock_item_channel_sku_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


