# OrderPackagingSplit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_bin_id** | **str** |  | [optional] 
**pk_postal_service_id** | **str** |  | [optional] 
**packaging_weight** | **float** |  | [optional] 
**fk_packaging_type_id** | **str** |  | [optional] 
**items** | [**List[OrderPackagingSplitItem]**](OrderPackagingSplitItem.md) |  | [optional] 
**total_weight** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**tracking_numbers** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.orders.models.order_packaging_split import OrderPackagingSplit

# TODO update the JSON string below
json = "{}"
# create an instance of OrderPackagingSplit from a JSON string
order_packaging_split_instance = OrderPackagingSplit.from_json(json)
# print the JSON string representation of the object
print(OrderPackagingSplit.to_json())

# convert the object into a dict
order_packaging_split_dict = order_packaging_split_instance.to_dict()
# create an instance of OrderPackagingSplit from a dict
order_packaging_split_from_dict = OrderPackagingSplit.from_dict(order_packaging_split_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


