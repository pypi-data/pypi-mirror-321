# StockCreateVariationGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | [**VariationGroupTemplate**](VariationGroupTemplate.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_create_variation_group_request import StockCreateVariationGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockCreateVariationGroupRequest from a JSON string
stock_create_variation_group_request_instance = StockCreateVariationGroupRequest.from_json(json)
# print the JSON string representation of the object
print(StockCreateVariationGroupRequest.to_json())

# convert the object into a dict
stock_create_variation_group_request_dict = stock_create_variation_group_request_instance.to_dict()
# create an instance of StockCreateVariationGroupRequest from a dict
stock_create_variation_group_request_from_dict = StockCreateVariationGroupRequest.from_dict(stock_create_variation_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


