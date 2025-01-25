# AddAdditionalCostTypesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | Additional cost name | [optional] 
**is_shipping_type** | **bool** | Type of additional cost is shipping cost | [optional] 
**is_partial_allocation** | **bool** | Type must be 100% allocated to PO items | [optional] 
**var_print** | **bool** | Type must appear on prints and emails | [optional] 
**allocation_method** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.add_additional_cost_types_request import AddAdditionalCostTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddAdditionalCostTypesRequest from a JSON string
add_additional_cost_types_request_instance = AddAdditionalCostTypesRequest.from_json(json)
# print the JSON string representation of the object
print(AddAdditionalCostTypesRequest.to_json())

# convert the object into a dict
add_additional_cost_types_request_dict = add_additional_cost_types_request_instance.to_dict()
# create an instance of AddAdditionalCostTypesRequest from a dict
add_additional_cost_types_request_from_dict = AddAdditionalCostTypesRequest.from_dict(add_additional_cost_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


