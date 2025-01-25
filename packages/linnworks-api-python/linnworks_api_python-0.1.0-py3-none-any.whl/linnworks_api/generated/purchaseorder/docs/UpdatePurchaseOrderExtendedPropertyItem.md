# UpdatePurchaseOrderExtendedPropertyItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **int** |  | [optional] 
**property_name** | **str** |  | [optional] 
**property_value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.update_purchase_order_extended_property_item import UpdatePurchaseOrderExtendedPropertyItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePurchaseOrderExtendedPropertyItem from a JSON string
update_purchase_order_extended_property_item_instance = UpdatePurchaseOrderExtendedPropertyItem.from_json(json)
# print the JSON string representation of the object
print(UpdatePurchaseOrderExtendedPropertyItem.to_json())

# convert the object into a dict
update_purchase_order_extended_property_item_dict = update_purchase_order_extended_property_item_instance.to_dict()
# create an instance of UpdatePurchaseOrderExtendedPropertyItem from a dict
update_purchase_order_extended_property_item_from_dict = UpdatePurchaseOrderExtendedPropertyItem.from_dict(update_purchase_order_extended_property_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


