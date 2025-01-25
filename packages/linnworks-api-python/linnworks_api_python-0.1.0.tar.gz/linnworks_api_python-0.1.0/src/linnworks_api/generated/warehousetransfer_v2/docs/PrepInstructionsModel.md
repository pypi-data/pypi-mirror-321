# PrepInstructionsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | [**CurrencyModel**](CurrencyModel.md) |  | [optional] 
**prep_owner** | [**PrepOwner**](PrepOwner.md) |  | [optional] 
**prep_type** | [**PrepType**](PrepType.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.prep_instructions_model import PrepInstructionsModel

# TODO update the JSON string below
json = "{}"
# create an instance of PrepInstructionsModel from a JSON string
prep_instructions_model_instance = PrepInstructionsModel.from_json(json)
# print the JSON string representation of the object
print(PrepInstructionsModel.to_json())

# convert the object into a dict
prep_instructions_model_dict = prep_instructions_model_instance.to_dict()
# create an instance of PrepInstructionsModel from a dict
prep_instructions_model_from_dict = PrepInstructionsModel.from_dict(prep_instructions_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


