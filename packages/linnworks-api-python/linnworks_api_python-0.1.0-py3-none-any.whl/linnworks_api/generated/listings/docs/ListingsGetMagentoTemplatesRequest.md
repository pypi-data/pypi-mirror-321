# ListingsGetMagentoTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**GetTemplatesParameters**](GetTemplatesParameters.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_get_magento_templates_request import ListingsGetMagentoTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsGetMagentoTemplatesRequest from a JSON string
listings_get_magento_templates_request_instance = ListingsGetMagentoTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsGetMagentoTemplatesRequest.to_json())

# convert the object into a dict
listings_get_magento_templates_request_dict = listings_get_magento_templates_request_instance.to_dict()
# create an instance of ListingsGetMagentoTemplatesRequest from a dict
listings_get_magento_templates_request_from_dict = ListingsGetMagentoTemplatesRequest.from_dict(listings_get_magento_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


