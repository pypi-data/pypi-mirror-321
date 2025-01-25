# ProcessedOrdersCreateFullResendRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** |  | [optional] 
**despatch_location** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**additional_cost** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_create_full_resend_request import ProcessedOrdersCreateFullResendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersCreateFullResendRequest from a JSON string
processed_orders_create_full_resend_request_instance = ProcessedOrdersCreateFullResendRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersCreateFullResendRequest.to_json())

# convert the object into a dict
processed_orders_create_full_resend_request_dict = processed_orders_create_full_resend_request_instance.to_dict()
# create an instance of ProcessedOrdersCreateFullResendRequest from a dict
processed_orders_create_full_resend_request_from_dict = ProcessedOrdersCreateFullResendRequest.from_dict(processed_orders_create_full_resend_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


