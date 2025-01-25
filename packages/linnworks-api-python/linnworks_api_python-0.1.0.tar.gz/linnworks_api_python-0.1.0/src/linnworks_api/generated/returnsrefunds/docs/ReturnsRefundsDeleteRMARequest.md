# ReturnsRefundsDeleteRMARequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DeleteRMARequest**](DeleteRMARequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.returns_refunds_delete_rma_request import ReturnsRefundsDeleteRMARequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsRefundsDeleteRMARequest from a JSON string
returns_refunds_delete_rma_request_instance = ReturnsRefundsDeleteRMARequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsRefundsDeleteRMARequest.to_json())

# convert the object into a dict
returns_refunds_delete_rma_request_dict = returns_refunds_delete_rma_request_instance.to_dict()
# create an instance of ReturnsRefundsDeleteRMARequest from a dict
returns_refunds_delete_rma_request_from_dict = ReturnsRefundsDeleteRMARequest.from_dict(returns_refunds_delete_rma_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


