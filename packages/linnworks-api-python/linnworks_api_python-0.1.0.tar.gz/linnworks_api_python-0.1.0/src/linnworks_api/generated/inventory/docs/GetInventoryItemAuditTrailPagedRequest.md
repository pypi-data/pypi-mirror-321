# GetInventoryItemAuditTrailPagedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_number** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_inventory_item_audit_trail_paged_request import GetInventoryItemAuditTrailPagedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetInventoryItemAuditTrailPagedRequest from a JSON string
get_inventory_item_audit_trail_paged_request_instance = GetInventoryItemAuditTrailPagedRequest.from_json(json)
# print the JSON string representation of the object
print(GetInventoryItemAuditTrailPagedRequest.to_json())

# convert the object into a dict
get_inventory_item_audit_trail_paged_request_dict = get_inventory_item_audit_trail_paged_request_instance.to_dict()
# create an instance of GetInventoryItemAuditTrailPagedRequest from a dict
get_inventory_item_audit_trail_paged_request_from_dict = GetInventoryItemAuditTrailPagedRequest.from_dict(get_inventory_item_audit_trail_paged_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


