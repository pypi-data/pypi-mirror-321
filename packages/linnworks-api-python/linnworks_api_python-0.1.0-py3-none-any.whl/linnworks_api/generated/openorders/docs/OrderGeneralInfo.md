# OrderGeneralInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**label_printed** | **bool** |  | [optional] 
**label_error** | **str** |  | [optional] 
**invoice_printed** | **bool** |  | [optional] 
**invoice_print_error** | **str** |  | [optional] 
**pick_list_printed** | **bool** |  | [optional] 
**pick_list_print_error** | **str** |  | [optional] 
**is_rule_run** | **bool** |  | [optional] 
**notes** | **int** |  | [optional] 
**part_shipped** | **bool** |  | [optional] 
**marker** | **int** |  | [optional] 
**is_parked** | **bool** |  | [optional] 
**identifiers** | [**List[Identifier]**](Identifier.md) |  | [optional] 
**reference_num** | **str** |  | [optional] 
**secondary_reference** | **str** |  | [optional] 
**external_reference_num** | **str** |  | [optional] 
**received_date** | **datetime** |  | [optional] 
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**site_code** | **str** |  | [optional] 
**hold_or_cancel** | **bool** |  | [optional] 
**despatch_by_date** | **datetime** |  | [optional] 
**scheduled_delivery** | [**ScheduledDelivery**](ScheduledDelivery.md) |  | [optional] 
**has_scheduled_delivery** | **bool** |  | [optional] [readonly] 
**location** | **str** |  | [optional] 
**num_items** | **int** |  | [optional] 
**pickwave_ids** | **List[int]** |  | [optional] 
**stock_allocation_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.order_general_info import OrderGeneralInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderGeneralInfo from a JSON string
order_general_info_instance = OrderGeneralInfo.from_json(json)
# print the JSON string representation of the object
print(OrderGeneralInfo.to_json())

# convert the object into a dict
order_general_info_dict = order_general_info_instance.to_dict()
# create an instance of OrderGeneralInfo from a dict
order_general_info_from_dict = OrderGeneralInfo.from_dict(order_general_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


