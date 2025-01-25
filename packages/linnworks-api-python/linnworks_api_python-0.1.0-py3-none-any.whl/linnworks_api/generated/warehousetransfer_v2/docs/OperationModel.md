# OperationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**entity_id** | **int** |  | [optional] 
**status** | [**OperationStatus**](OperationStatus.md) |  | [optional] 
**type** | [**OperationType**](OperationType.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**problems** | [**List[OperationProblemModel]**](OperationProblemModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.operation_model import OperationModel

# TODO update the JSON string below
json = "{}"
# create an instance of OperationModel from a JSON string
operation_model_instance = OperationModel.from_json(json)
# print the JSON string representation of the object
print(OperationModel.to_json())

# convert the object into a dict
operation_model_dict = operation_model_instance.to_dict()
# create an instance of OperationModel from a dict
operation_model_from_dict = OperationModel.from_dict(operation_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


