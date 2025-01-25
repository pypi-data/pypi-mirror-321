# PurchaseOrderExtendedProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_id** | **int** |  | [optional] 
**purchase_id** | **str** |  | [optional] 
**added_date_time** | **datetime** |  | [optional] 
**user_name** | **str** |  | [optional] 
**property_name** | **str** |  | [optional] 
**property_value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_extended_property import PurchaseOrderExtendedProperty

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderExtendedProperty from a JSON string
purchase_order_extended_property_instance = PurchaseOrderExtendedProperty.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderExtendedProperty.to_json())

# convert the object into a dict
purchase_order_extended_property_dict = purchase_order_extended_property_instance.to_dict()
# create an instance of PurchaseOrderExtendedProperty from a dict
purchase_order_extended_property_from_dict = PurchaseOrderExtendedProperty.from_dict(purchase_order_extended_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


