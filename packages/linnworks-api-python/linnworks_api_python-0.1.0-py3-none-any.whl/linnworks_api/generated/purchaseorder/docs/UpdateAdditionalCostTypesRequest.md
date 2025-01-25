# UpdateAdditionalCostTypesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_cost_type_id** | **int** | Additional Cost type id to update | [optional] 
**type_name** | **str** | Additional cost name, if null the field is not updated | [optional] 
**is_shipping_type** | **bool** | Type of additional cost is shipping cost, if null, the field is not updated | [optional] 
**is_partial_allocation** | **bool** | Type must be 100% allocated to PO items, if null, the field is not updated | [optional] 
**var_print** | **bool** | Type must appear on prints and emails | [optional] 
**allocation_method** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.update_additional_cost_types_request import UpdateAdditionalCostTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdditionalCostTypesRequest from a JSON string
update_additional_cost_types_request_instance = UpdateAdditionalCostTypesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdditionalCostTypesRequest.to_json())

# convert the object into a dict
update_additional_cost_types_request_dict = update_additional_cost_types_request_instance.to_dict()
# create an instance of UpdateAdditionalCostTypesRequest from a dict
update_additional_cost_types_request_from_dict = UpdateAdditionalCostTypesRequest.from_dict(update_additional_cost_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


