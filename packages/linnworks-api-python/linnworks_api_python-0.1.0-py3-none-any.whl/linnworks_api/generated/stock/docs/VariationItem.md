# VariationItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_row_id** | **str** |  | [optional] 
**pk_stock_item_id** | **str** |  | [optional] 
**item_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.variation_item import VariationItem

# TODO update the JSON string below
json = "{}"
# create an instance of VariationItem from a JSON string
variation_item_instance = VariationItem.from_json(json)
# print the JSON string representation of the object
print(VariationItem.to_json())

# convert the object into a dict
variation_item_dict = variation_item_instance.to_dict()
# create an instance of VariationItem from a dict
variation_item_from_dict = VariationItem.from_dict(variation_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


