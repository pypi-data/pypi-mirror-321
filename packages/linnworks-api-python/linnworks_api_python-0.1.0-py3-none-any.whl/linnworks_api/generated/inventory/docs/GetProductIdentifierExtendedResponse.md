# GetProductIdentifierExtendedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[ProductIdentifierInformation]**](ProductIdentifierInformation.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_product_identifier_extended_response import GetProductIdentifierExtendedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductIdentifierExtendedResponse from a JSON string
get_product_identifier_extended_response_instance = GetProductIdentifierExtendedResponse.from_json(json)
# print the JSON string representation of the object
print(GetProductIdentifierExtendedResponse.to_json())

# convert the object into a dict
get_product_identifier_extended_response_dict = get_product_identifier_extended_response_instance.to_dict()
# create an instance of GetProductIdentifierExtendedResponse from a dict
get_product_identifier_extended_response_from_dict = GetProductIdentifierExtendedResponse.from_dict(get_product_identifier_extended_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


