# VariationGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_sku** | **str** |  | [optional] 
**pk_variation_item_id** | **str** |  | [optional] 
**variation_group_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.variation_group import VariationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of VariationGroup from a JSON string
variation_group_instance = VariationGroup.from_json(json)
# print the JSON string representation of the object
print(VariationGroup.to_json())

# convert the object into a dict
variation_group_dict = variation_group_instance.to_dict()
# create an instance of VariationGroup from a dict
variation_group_from_dict = VariationGroup.from_dict(variation_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


