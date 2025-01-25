# GetPaymentStatementResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CommonPurchaseOrderPaymentStatement]**](CommonPurchaseOrderPaymentStatement.md) | List of payment statements | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.get_payment_statement_response import GetPaymentStatementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentStatementResponse from a JSON string
get_payment_statement_response_instance = GetPaymentStatementResponse.from_json(json)
# print the JSON string representation of the object
print(GetPaymentStatementResponse.to_json())

# convert the object into a dict
get_payment_statement_response_dict = get_payment_statement_response_instance.to_dict()
# create an instance of GetPaymentStatementResponse from a dict
get_payment_statement_response_from_dict = GetPaymentStatementResponse.from_dict(get_payment_statement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


