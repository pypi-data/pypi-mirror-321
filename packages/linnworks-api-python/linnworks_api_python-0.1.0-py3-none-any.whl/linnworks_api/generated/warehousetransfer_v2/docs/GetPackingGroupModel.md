# GetPackingGroupModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**shipping_plan_id** | **int** |  | [optional] 
**amazon_packing_group_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.get_packing_group_model import GetPackingGroupModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetPackingGroupModel from a JSON string
get_packing_group_model_instance = GetPackingGroupModel.from_json(json)
# print the JSON string representation of the object
print(GetPackingGroupModel.to_json())

# convert the object into a dict
get_packing_group_model_dict = get_packing_group_model_instance.to_dict()
# create an instance of GetPackingGroupModel from a dict
get_packing_group_model_from_dict = GetPackingGroupModel.from_dict(get_packing_group_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


