# AdjustmentOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **bool** | Product title | [optional] 
**price** | **bool** | Product price | [optional] 
**description** | **bool** | Product description | [optional] 
**add_extended_properties** | **bool** | If product extended properties needs to be added | [optional] 
**revise_extended_properties** | **bool** | Revise product extended properties | [optional] 
**update_images** | **bool** | Update product images | [optional] 
**variation_attributes** | **bool** | Product variation attributes | [optional] 
**reload_all_images** | **bool** | Reload all images for the template | [optional] 
**remove_old_attributes** | **bool** | Removes old attributes | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.adjustment_options import AdjustmentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentOptions from a JSON string
adjustment_options_instance = AdjustmentOptions.from_json(json)
# print the JSON string representation of the object
print(AdjustmentOptions.to_json())

# convert the object into a dict
adjustment_options_dict = adjustment_options_instance.to_dict()
# create an instance of AdjustmentOptions from a dict
adjustment_options_from_dict = AdjustmentOptions.from_dict(adjustment_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


