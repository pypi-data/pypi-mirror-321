# LinnworksCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**structure_category_id** | **int** |  | [optional] 
**product_category_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.linnworks_category import LinnworksCategory

# TODO update the JSON string below
json = "{}"
# create an instance of LinnworksCategory from a JSON string
linnworks_category_instance = LinnworksCategory.from_json(json)
# print the JSON string representation of the object
print(LinnworksCategory.to_json())

# convert the object into a dict
linnworks_category_dict = linnworks_category_instance.to_dict()
# create an instance of LinnworksCategory from a dict
linnworks_category_from_dict = LinnworksCategory.from_dict(linnworks_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


