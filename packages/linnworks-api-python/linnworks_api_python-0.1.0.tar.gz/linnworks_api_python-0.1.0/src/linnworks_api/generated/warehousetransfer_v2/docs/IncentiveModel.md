# IncentiveModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**CurrencyModel**](CurrencyModel.md) |  | [optional] 
**target** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.incentive_model import IncentiveModel

# TODO update the JSON string below
json = "{}"
# create an instance of IncentiveModel from a JSON string
incentive_model_instance = IncentiveModel.from_json(json)
# print the JSON string representation of the object
print(IncentiveModel.to_json())

# convert the object into a dict
incentive_model_dict = incentive_model_instance.to_dict()
# create an instance of IncentiveModel from a dict
incentive_model_from_dict = IncentiveModel.from_dict(incentive_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


