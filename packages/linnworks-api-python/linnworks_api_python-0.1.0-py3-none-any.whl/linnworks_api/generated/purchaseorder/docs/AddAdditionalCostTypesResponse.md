# AddAdditionalCostTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_additional_cost_type** | [**PurchaseOrderAdditionalCostType**](PurchaseOrderAdditionalCostType.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.add_additional_cost_types_response import AddAdditionalCostTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddAdditionalCostTypesResponse from a JSON string
add_additional_cost_types_response_instance = AddAdditionalCostTypesResponse.from_json(json)
# print the JSON string representation of the object
print(AddAdditionalCostTypesResponse.to_json())

# convert the object into a dict
add_additional_cost_types_response_dict = add_additional_cost_types_response_instance.to_dict()
# create an instance of AddAdditionalCostTypesResponse from a dict
add_additional_cost_types_response_from_dict = AddAdditionalCostTypesResponse.from_dict(add_additional_cost_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


