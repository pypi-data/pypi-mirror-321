# GetPaymentStatementRequest

Request class for getting purchase order payment statements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_id** | **str** | Purchase order unique identifier of a PO | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.get_payment_statement_request import GetPaymentStatementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentStatementRequest from a JSON string
get_payment_statement_request_instance = GetPaymentStatementRequest.from_json(json)
# print the JSON string representation of the object
print(GetPaymentStatementRequest.to_json())

# convert the object into a dict
get_payment_statement_request_dict = get_payment_statement_request_instance.to_dict()
# create an instance of GetPaymentStatementRequest from a dict
get_payment_statement_request_from_dict = GetPaymentStatementRequest.from_dict(get_payment_statement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


