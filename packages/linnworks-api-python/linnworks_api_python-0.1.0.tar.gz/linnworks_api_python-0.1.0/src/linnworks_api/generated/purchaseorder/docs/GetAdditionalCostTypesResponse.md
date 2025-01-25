# GetAdditionalCostTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_types** | [**List[PurchaseOrderAdditionalCostType]**](PurchaseOrderAdditionalCostType.md) | List of additional costs types | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.get_additional_cost_types_response import GetAdditionalCostTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdditionalCostTypesResponse from a JSON string
get_additional_cost_types_response_instance = GetAdditionalCostTypesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAdditionalCostTypesResponse.to_json())

# convert the object into a dict
get_additional_cost_types_response_dict = get_additional_cost_types_response_instance.to_dict()
# create an instance of GetAdditionalCostTypesResponse from a dict
get_additional_cost_types_response_from_dict = GetAdditionalCostTypesResponse.from_dict(get_additional_cost_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


