# UpdateAdditionalCostTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_additional_cost_type** | [**PurchaseOrderAdditionalCostType**](PurchaseOrderAdditionalCostType.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.update_additional_cost_types_response import UpdateAdditionalCostTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdditionalCostTypesResponse from a JSON string
update_additional_cost_types_response_instance = UpdateAdditionalCostTypesResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAdditionalCostTypesResponse.to_json())

# convert the object into a dict
update_additional_cost_types_response_dict = update_additional_cost_types_response_instance.to_dict()
# create an instance of UpdateAdditionalCostTypesResponse from a dict
update_additional_cost_types_response_from_dict = UpdateAdditionalCostTypesResponse.from_dict(update_additional_cost_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


