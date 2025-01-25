# PackingGroupModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packing_group_id** | **str** |  | [optional] 
**items** | [**List[ItemModel]**](ItemModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.packing_group_model import PackingGroupModel

# TODO update the JSON string below
json = "{}"
# create an instance of PackingGroupModel from a JSON string
packing_group_model_instance = PackingGroupModel.from_json(json)
# print the JSON string representation of the object
print(PackingGroupModel.to_json())

# convert the object into a dict
packing_group_model_dict = packing_group_model_instance.to_dict()
# create an instance of PackingGroupModel from a dict
packing_group_model_from_dict = PackingGroupModel.from_dict(packing_group_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


