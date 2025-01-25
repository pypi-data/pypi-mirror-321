# ListingsCreateMagentoTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**ProcessTemplatesParameters**](ProcessTemplatesParameters.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_create_magento_templates_request import ListingsCreateMagentoTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsCreateMagentoTemplatesRequest from a JSON string
listings_create_magento_templates_request_instance = ListingsCreateMagentoTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsCreateMagentoTemplatesRequest.to_json())

# convert the object into a dict
listings_create_magento_templates_request_dict = listings_create_magento_templates_request_instance.to_dict()
# create an instance of ListingsCreateMagentoTemplatesRequest from a dict
listings_create_magento_templates_request_from_dict = ListingsCreateMagentoTemplatesRequest.from_dict(listings_create_magento_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


