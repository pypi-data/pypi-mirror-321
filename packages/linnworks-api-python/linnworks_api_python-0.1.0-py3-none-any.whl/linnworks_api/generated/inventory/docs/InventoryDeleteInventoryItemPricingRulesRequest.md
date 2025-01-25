# InventoryDeleteInventoryItemPricingRulesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_rule_ids** | **List[int]** | List of stock item pricing rule ids to delete | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_inventory_item_pricing_rules_request import InventoryDeleteInventoryItemPricingRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteInventoryItemPricingRulesRequest from a JSON string
inventory_delete_inventory_item_pricing_rules_request_instance = InventoryDeleteInventoryItemPricingRulesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteInventoryItemPricingRulesRequest.to_json())

# convert the object into a dict
inventory_delete_inventory_item_pricing_rules_request_dict = inventory_delete_inventory_item_pricing_rules_request_instance.to_dict()
# create an instance of InventoryDeleteInventoryItemPricingRulesRequest from a dict
inventory_delete_inventory_item_pricing_rules_request_from_dict = InventoryDeleteInventoryItemPricingRulesRequest.from_dict(inventory_delete_inventory_item_pricing_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


