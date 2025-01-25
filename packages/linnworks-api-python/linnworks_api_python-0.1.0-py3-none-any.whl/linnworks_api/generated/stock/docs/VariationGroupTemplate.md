# VariationGroupTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_group_name** | **str** |  | [optional] 
**parent_sku** | **str** |  | [optional] 
**parent_stock_item_id** | **str** |  | [optional] 
**variation_item_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.variation_group_template import VariationGroupTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of VariationGroupTemplate from a JSON string
variation_group_template_instance = VariationGroupTemplate.from_json(json)
# print the JSON string representation of the object
print(VariationGroupTemplate.to_json())

# convert the object into a dict
variation_group_template_dict = variation_group_template_instance.to_dict()
# create an instance of VariationGroupTemplate from a dict
variation_group_template_from_dict = VariationGroupTemplate.from_dict(variation_group_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


