# UpdateProductIdentifiersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_identifiers** | [**List[StockItemProductIdentifier]**](StockItemProductIdentifier.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.update_product_identifiers_request import UpdateProductIdentifiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductIdentifiersRequest from a JSON string
update_product_identifiers_request_instance = UpdateProductIdentifiersRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProductIdentifiersRequest.to_json())

# convert the object into a dict
update_product_identifiers_request_dict = update_product_identifiers_request_instance.to_dict()
# create an instance of UpdateProductIdentifiersRequest from a dict
update_product_identifiers_request_from_dict = UpdateProductIdentifiersRequest.from_dict(update_product_identifiers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


