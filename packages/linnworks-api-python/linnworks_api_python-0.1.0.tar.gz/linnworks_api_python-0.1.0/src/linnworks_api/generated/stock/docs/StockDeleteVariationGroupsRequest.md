# StockDeleteVariationGroupsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DeleteVariationGroupsRequest**](DeleteVariationGroupsRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_delete_variation_groups_request import StockDeleteVariationGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockDeleteVariationGroupsRequest from a JSON string
stock_delete_variation_groups_request_instance = StockDeleteVariationGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(StockDeleteVariationGroupsRequest.to_json())

# convert the object into a dict
stock_delete_variation_groups_request_dict = stock_delete_variation_groups_request_instance.to_dict()
# create an instance of StockDeleteVariationGroupsRequest from a dict
stock_delete_variation_groups_request_from_dict = StockDeleteVariationGroupsRequest.from_dict(stock_delete_variation_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


