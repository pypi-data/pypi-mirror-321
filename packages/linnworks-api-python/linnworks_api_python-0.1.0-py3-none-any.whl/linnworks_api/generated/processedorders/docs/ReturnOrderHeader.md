# ReturnOrderHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** |  | [optional] 
**n_order_id** | **int** |  | [optional] 
**source** | **str** |  | [optional] 
**sub_source** | **str** |  | [optional] 
**postal_service_name** | **str** |  | [optional] 
**c_shipping_address** | **str** |  | [optional] 
**c_currency** | **str** |  | [optional] 
**d_received_date** | **datetime** |  | [optional] 
**d_processed_on** | **datetime** |  | [optional] 
**f_total_charge** | **float** |  | [optional] 
**refund_link** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.return_order_header import ReturnOrderHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnOrderHeader from a JSON string
return_order_header_instance = ReturnOrderHeader.from_json(json)
# print the JSON string representation of the object
print(ReturnOrderHeader.to_json())

# convert the object into a dict
return_order_header_dict = return_order_header_instance.to_dict()
# create an instance of ReturnOrderHeader from a dict
return_order_header_from_dict = ReturnOrderHeader.from_dict(return_order_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


