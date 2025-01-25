# DeleteProductIdentifiersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_identifier_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.delete_product_identifiers_request import DeleteProductIdentifiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteProductIdentifiersRequest from a JSON string
delete_product_identifiers_request_instance = DeleteProductIdentifiersRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteProductIdentifiersRequest.to_json())

# convert the object into a dict
delete_product_identifiers_request_dict = delete_product_identifiers_request_instance.to_dict()
# create an instance of DeleteProductIdentifiersRequest from a dict
delete_product_identifiers_request_from_dict = DeleteProductIdentifiersRequest.from_dict(delete_product_identifiers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


