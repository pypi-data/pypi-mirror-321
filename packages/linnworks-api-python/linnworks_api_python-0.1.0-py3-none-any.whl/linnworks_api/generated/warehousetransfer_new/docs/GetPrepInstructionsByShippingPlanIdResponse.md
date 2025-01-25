# GetPrepInstructionsByShippingPlanIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku_prep_instructions_list** | [**List[SkuPrepInstructionItem]**](SkuPrepInstructionItem.md) |  | [optional] 
**shipping_plan_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.get_prep_instructions_by_shipping_plan_id_response import GetPrepInstructionsByShippingPlanIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPrepInstructionsByShippingPlanIdResponse from a JSON string
get_prep_instructions_by_shipping_plan_id_response_instance = GetPrepInstructionsByShippingPlanIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetPrepInstructionsByShippingPlanIdResponse.to_json())

# convert the object into a dict
get_prep_instructions_by_shipping_plan_id_response_dict = get_prep_instructions_by_shipping_plan_id_response_instance.to_dict()
# create an instance of GetPrepInstructionsByShippingPlanIdResponse from a dict
get_prep_instructions_by_shipping_plan_id_response_from_dict = GetPrepInstructionsByShippingPlanIdResponse.from_dict(get_prep_instructions_by_shipping_plan_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


