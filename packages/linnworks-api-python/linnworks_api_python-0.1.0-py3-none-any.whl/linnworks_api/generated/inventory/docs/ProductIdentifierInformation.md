# ProductIdentifierInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**scanned_at_dispatch** | **bool** |  | [optional] 
**sources** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.product_identifier_information import ProductIdentifierInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ProductIdentifierInformation from a JSON string
product_identifier_information_instance = ProductIdentifierInformation.from_json(json)
# print the JSON string representation of the object
print(ProductIdentifierInformation.to_json())

# convert the object into a dict
product_identifier_information_dict = product_identifier_information_instance.to_dict()
# create an instance of ProductIdentifierInformation from a dict
product_identifier_information_from_dict = ProductIdentifierInformation.from_dict(product_identifier_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


