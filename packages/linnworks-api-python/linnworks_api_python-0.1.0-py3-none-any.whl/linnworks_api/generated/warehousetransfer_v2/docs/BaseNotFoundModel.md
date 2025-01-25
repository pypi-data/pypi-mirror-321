# BaseNotFoundModel

Not found model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message | [optional] 
**link** | **str** |  | [optional] 
**link_text** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.base_not_found_model import BaseNotFoundModel

# TODO update the JSON string below
json = "{}"
# create an instance of BaseNotFoundModel from a JSON string
base_not_found_model_instance = BaseNotFoundModel.from_json(json)
# print the JSON string representation of the object
print(BaseNotFoundModel.to_json())

# convert the object into a dict
base_not_found_model_dict = base_not_found_model_instance.to_dict()
# create an instance of BaseNotFoundModel from a dict
base_not_found_model_from_dict = BaseNotFoundModel.from_dict(base_not_found_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


