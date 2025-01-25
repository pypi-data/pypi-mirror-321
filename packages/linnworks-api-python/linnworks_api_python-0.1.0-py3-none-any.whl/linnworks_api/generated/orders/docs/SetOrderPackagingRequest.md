# SetOrderPackagingRequest

Request class for SetOrderPackaging method in Orders controller

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_packaging_group_id** | **str** | Packaging group Id | [optional] 
**fk_packaging_type_id** | **str** | Packaging Type Id. It has to be one of types available for selected Group Id | [optional] 
**pk_order_id** | **str** | Order Id to set the order packaging data | [optional] 
**total_weight** | **float** | Total weight of order packaging | [optional] 
**manual_adjust** | **bool** | Indicate if this data is manually adjusted with the rest of fields or is auto calculated | [optional] 
**is_auto_split** | **bool** | Indicates whether the order should be auto split. Usually via the 3D packaging methods. | [optional] 
**total_depth** | **float** | Total packaging depth | [optional] 
**total_height** | **float** | Total Height | [optional] 
**total_width** | **float** | Total Width | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.set_order_packaging_request import SetOrderPackagingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetOrderPackagingRequest from a JSON string
set_order_packaging_request_instance = SetOrderPackagingRequest.from_json(json)
# print the JSON string representation of the object
print(SetOrderPackagingRequest.to_json())

# convert the object into a dict
set_order_packaging_request_dict = set_order_packaging_request_instance.to_dict()
# create an instance of SetOrderPackagingRequest from a dict
set_order_packaging_request_from_dict = SetOrderPackagingRequest.from_dict(set_order_packaging_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


