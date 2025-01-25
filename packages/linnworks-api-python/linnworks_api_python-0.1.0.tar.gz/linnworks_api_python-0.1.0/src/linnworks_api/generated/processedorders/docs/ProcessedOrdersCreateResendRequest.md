# ProcessedOrdersCreateResendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | Order ID that needs to be resend | [optional] 
**resend_items** | [**List[RowQty]**](RowQty.md) | Resend items information | [optional] 
**despatch_location** | **str** | Location ID where from resend be despatched | [optional] 
**category** | **str** | Category | [optional] 
**reason** | **str** | Resond reason | [optional] 
**additional_cost** | **float** | Order-level additional cost | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_create_resend_request import ProcessedOrdersCreateResendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersCreateResendRequest from a JSON string
processed_orders_create_resend_request_instance = ProcessedOrdersCreateResendRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersCreateResendRequest.to_json())

# convert the object into a dict
processed_orders_create_resend_request_dict = processed_orders_create_resend_request_instance.to_dict()
# create an instance of ProcessedOrdersCreateResendRequest from a dict
processed_orders_create_resend_request_from_dict = ProcessedOrdersCreateResendRequest.from_dict(processed_orders_create_resend_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


