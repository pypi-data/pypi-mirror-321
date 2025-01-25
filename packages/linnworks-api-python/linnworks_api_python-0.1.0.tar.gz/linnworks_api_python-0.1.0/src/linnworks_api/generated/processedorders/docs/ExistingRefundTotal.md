# ExistingRefundTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**total_charge** | **float** |  | [optional] 
**refundable** | **float** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.processedorders.models.existing_refund_total import ExistingRefundTotal

# TODO update the JSON string below
json = "{}"
# create an instance of ExistingRefundTotal from a JSON string
existing_refund_total_instance = ExistingRefundTotal.from_json(json)
# print the JSON string representation of the object
print(ExistingRefundTotal.to_json())

# convert the object into a dict
existing_refund_total_dict = existing_refund_total_instance.to_dict()
# create an instance of ExistingRefundTotal from a dict
existing_refund_total_from_dict = ExistingRefundTotal.from_dict(existing_refund_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


