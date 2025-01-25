# AddPurchaseOrderExtendedPropertyItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** |  | [optional] 
**property_value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.add_purchase_order_extended_property_item import AddPurchaseOrderExtendedPropertyItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddPurchaseOrderExtendedPropertyItem from a JSON string
add_purchase_order_extended_property_item_instance = AddPurchaseOrderExtendedPropertyItem.from_json(json)
# print the JSON string representation of the object
print(AddPurchaseOrderExtendedPropertyItem.to_json())

# convert the object into a dict
add_purchase_order_extended_property_item_dict = add_purchase_order_extended_property_item_instance.to_dict()
# create an instance of AddPurchaseOrderExtendedPropertyItem from a dict
add_purchase_order_extended_property_item_from_dict = AddPurchaseOrderExtendedPropertyItem.from_dict(add_purchase_order_extended_property_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


