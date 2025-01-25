# RefundScreenOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_text_option** | **str** |  | [optional] 
**can_refund_shipping** | **bool** |  | [optional] 
**order_has_service_items** | **bool** |  | [optional] 
**is_shipping_refund_automated** | **bool** |  | [optional] 
**is_service_refund_automated** | **bool** |  | [optional] 
**supports_automated_refunds** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.refund_screen_options import RefundScreenOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RefundScreenOptions from a JSON string
refund_screen_options_instance = RefundScreenOptions.from_json(json)
# print the JSON string representation of the object
print(RefundScreenOptions.to_json())

# convert the object into a dict
refund_screen_options_dict = refund_screen_options_instance.to_dict()
# create an instance of RefundScreenOptions from a dict
refund_screen_options_from_dict = RefundScreenOptions.from_dict(refund_screen_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


