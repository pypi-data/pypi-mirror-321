# GetAdditionalCostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CommonPurchaseOrderAdditionalCost]**](CommonPurchaseOrderAdditionalCost.md) | List of additional cost items | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.get_additional_cost_response import GetAdditionalCostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdditionalCostResponse from a JSON string
get_additional_cost_response_instance = GetAdditionalCostResponse.from_json(json)
# print the JSON string representation of the object
print(GetAdditionalCostResponse.to_json())

# convert the object into a dict
get_additional_cost_response_dict = get_additional_cost_response_instance.to_dict()
# create an instance of GetAdditionalCostResponse from a dict
get_additional_cost_response_from_dict = GetAdditionalCostResponse.from_dict(get_additional_cost_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


