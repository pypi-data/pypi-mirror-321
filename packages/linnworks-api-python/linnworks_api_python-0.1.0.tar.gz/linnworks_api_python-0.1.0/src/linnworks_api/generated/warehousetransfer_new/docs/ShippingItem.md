# ShippingItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_id** | **int** |  | [optional] 
**stock_item_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**pack_quantity** | **int** |  | [optional] 
**pack_size** | **int** |  | [optional] 
**quantity_to_ship** | **int** |  | [optional] 
**received_qty** | **int** |  | [optional] 
**shipment_id** | **int** |  | [optional] 
**seller_sku** | **str** |  | [optional] 
**shipped_qty** | **int** |  | [optional] 
**sku** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipping_item import ShippingItem

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


