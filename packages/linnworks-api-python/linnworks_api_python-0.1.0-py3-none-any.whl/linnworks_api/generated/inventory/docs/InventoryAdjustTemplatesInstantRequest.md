# InventoryAdjustTemplatesInstantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_ids** | **List[str]** | Inventory item ids | [optional] 
**source** | **str** | Channel type (&#39;EBAY&#39;, &#39;AMAZON&#39;, &#39;BIGCOMMERCE&#39;, &#39;MAGENTO&#39;) | [optional] 
**sub_source** | **str** | Channel Name | [optional] 
**adjustment_options** | [**AdjustmentOptions**](AdjustmentOptions.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_adjust_templates_instant_request import InventoryAdjustTemplatesInstantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAdjustTemplatesInstantRequest from a JSON string
inventory_adjust_templates_instant_request_instance = InventoryAdjustTemplatesInstantRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryAdjustTemplatesInstantRequest.to_json())

# convert the object into a dict
inventory_adjust_templates_instant_request_dict = inventory_adjust_templates_instant_request_instance.to_dict()
# create an instance of InventoryAdjustTemplatesInstantRequest from a dict
inventory_adjust_templates_instant_request_from_dict = InventoryAdjustTemplatesInstantRequest.from_dict(inventory_adjust_templates_instant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


