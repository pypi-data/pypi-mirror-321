# InventoryUpdateInventoryItemPricingRulesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[StockItemPricingRule]**](StockItemPricingRule.md) | List of stock item pricing rules to update | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_inventory_item_pricing_rules_request import InventoryUpdateInventoryItemPricingRulesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateInventoryItemPricingRulesRequest from a JSON string
inventory_update_inventory_item_pricing_rules_request_instance = InventoryUpdateInventoryItemPricingRulesRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateInventoryItemPricingRulesRequest.to_json())

# convert the object into a dict
inventory_update_inventory_item_pricing_rules_request_dict = inventory_update_inventory_item_pricing_rules_request_instance.to_dict()
# create an instance of InventoryUpdateInventoryItemPricingRulesRequest from a dict
inventory_update_inventory_item_pricing_rules_request_from_dict = InventoryUpdateInventoryItemPricingRulesRequest.from_dict(inventory_update_inventory_item_pricing_rules_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


