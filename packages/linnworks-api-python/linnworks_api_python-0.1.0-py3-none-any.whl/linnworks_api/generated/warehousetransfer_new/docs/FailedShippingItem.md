# FailedShippingItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** |  | [optional] 
**stock_item_id** | **int** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**fail_message** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.failed_shipping_item import FailedShippingItem

# TODO update the JSON string below
json = "{}"
# create an instance of FailedShippingItem from a JSON string
failed_shipping_item_instance = FailedShippingItem.from_json(json)
# print the JSON string representation of the object
print(FailedShippingItem.to_json())

# convert the object into a dict
failed_shipping_item_dict = failed_shipping_item_instance.to_dict()
# create an instance of FailedShippingItem from a dict
failed_shipping_item_from_dict = FailedShippingItem.from_dict(failed_shipping_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


