# ShippingItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **int** |  | 
**quantity_to_ship** | **int** |  | [optional] 
**received_qty** | **int** |  | [optional] 
**shipped_qty** | **int** |  | [optional] 
**shipment_id** | **int** |  | 
**seller_sku** | **str** |  | 
**sku** | **str** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.shipping_item import ShippingItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingItem from a JSON string
shipping_item_instance = ShippingItem.from_json(json)
# print the JSON string representation of the object
print(ShippingItem.to_json())

# convert the object into a dict
shipping_item_dict = shipping_item_instance.to_dict()
# create an instance of ShippingItem from a dict
shipping_item_from_dict = ShippingItem.from_dict(shipping_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


