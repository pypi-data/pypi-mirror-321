# OpenOrderLowFidelity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[OpenOrderItem]**](OpenOrderItem.md) |  | [optional] 
**order_id** | **int** |  | [optional] 
**pk_order_id** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**reference_num** | **str** |  | [optional] 
**external_reference** | **str** |  | [optional] 
**postal_tracking_number** | **str** |  | [optional] 
**order_date** | **datetime** |  | [optional] 
**dispatch_by** | **datetime** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.open_order_low_fidelity import OpenOrderLowFidelity

# TODO update the JSON string below
json = "{}"
# create an instance of OpenOrderLowFidelity from a JSON string
open_order_low_fidelity_instance = OpenOrderLowFidelity.from_json(json)
# print the JSON string representation of the object
print(OpenOrderLowFidelity.to_json())

# convert the object into a dict
open_order_low_fidelity_dict = open_order_low_fidelity_instance.to_dict()
# create an instance of OpenOrderLowFidelity from a dict
open_order_low_fidelity_from_dict = OpenOrderLowFidelity.from_dict(open_order_low_fidelity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


