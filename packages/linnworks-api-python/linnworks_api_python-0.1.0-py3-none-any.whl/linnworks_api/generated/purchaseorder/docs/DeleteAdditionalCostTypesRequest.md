# DeleteAdditionalCostTypesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_cost_type_id** | **int** | Additional cost type Ids to delete | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.delete_additional_cost_types_request import DeleteAdditionalCostTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAdditionalCostTypesRequest from a JSON string
delete_additional_cost_types_request_instance = DeleteAdditionalCostTypesRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteAdditionalCostTypesRequest.to_json())

# convert the object into a dict
delete_additional_cost_types_request_dict = delete_additional_cost_types_request_instance.to_dict()
# create an instance of DeleteAdditionalCostTypesRequest from a dict
delete_additional_cost_types_request_from_dict = DeleteAdditionalCostTypesRequest.from_dict(delete_additional_cost_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


