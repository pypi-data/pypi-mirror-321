# AddProductIdentifiersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_identifiers** | [**List[StockItemProductIdentifier]**](StockItemProductIdentifier.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.add_product_identifiers_request import AddProductIdentifiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddProductIdentifiersRequest from a JSON string
add_product_identifiers_request_instance = AddProductIdentifiersRequest.from_json(json)
# print the JSON string representation of the object
print(AddProductIdentifiersRequest.to_json())

# convert the object into a dict
add_product_identifiers_request_dict = add_product_identifiers_request_instance.to_dict()
# create an instance of AddProductIdentifiersRequest from a dict
add_product_identifiers_request_from_dict = AddProductIdentifiersRequest.from_dict(add_product_identifiers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


