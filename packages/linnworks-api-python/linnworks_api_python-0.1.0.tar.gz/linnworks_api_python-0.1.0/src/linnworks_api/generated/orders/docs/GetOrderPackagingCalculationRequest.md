# GetOrderPackagingCalculationRequest

Request class for GetOrderPackagingCalculationRequest method in Orders controller

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_ids** | **List[str]** | List of order ids for which the packaging information should be returned, recalculated, saved | [optional] 
**recalculate** | **bool** | Flag to indicate that recalculation is necessary | [optional] 
**save_recalculation** | **bool** | Flag to indicate that after recalculation the results should be saved back to the database | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.get_order_packaging_calculation_request import GetOrderPackagingCalculationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderPackagingCalculationRequest from a JSON string
get_order_packaging_calculation_request_instance = GetOrderPackagingCalculationRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrderPackagingCalculationRequest.to_json())

# convert the object into a dict
get_order_packaging_calculation_request_dict = get_order_packaging_calculation_request_instance.to_dict()
# create an instance of GetOrderPackagingCalculationRequest from a dict
get_order_packaging_calculation_request_from_dict = GetOrderPackagingCalculationRequest.from_dict(get_order_packaging_calculation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


