# StockRenameVariationGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_variation_item_id** | **str** | The id of the group to rename | [optional] 
**variation_name** | **str** | The name of the variation | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.stock_rename_variation_group_request import StockRenameVariationGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StockRenameVariationGroupRequest from a JSON string
stock_rename_variation_group_request_instance = StockRenameVariationGroupRequest.from_json(json)
# print the JSON string representation of the object
print(StockRenameVariationGroupRequest.to_json())

# convert the object into a dict
stock_rename_variation_group_request_dict = stock_rename_variation_group_request_instance.to_dict()
# create an instance of StockRenameVariationGroupRequest from a dict
stock_rename_variation_group_request_from_dict = StockRenameVariationGroupRequest.from_dict(stock_rename_variation_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


