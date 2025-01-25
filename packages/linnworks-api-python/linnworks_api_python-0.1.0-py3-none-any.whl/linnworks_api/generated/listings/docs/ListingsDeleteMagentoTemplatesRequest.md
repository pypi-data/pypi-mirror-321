# ListingsDeleteMagentoTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_delete_magento_templates_request import ListingsDeleteMagentoTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsDeleteMagentoTemplatesRequest from a JSON string
listings_delete_magento_templates_request_instance = ListingsDeleteMagentoTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsDeleteMagentoTemplatesRequest.to_json())

# convert the object into a dict
listings_delete_magento_templates_request_dict = listings_delete_magento_templates_request_instance.to_dict()
# create an instance of ListingsDeleteMagentoTemplatesRequest from a dict
listings_delete_magento_templates_request_from_dict = ListingsDeleteMagentoTemplatesRequest.from_dict(listings_delete_magento_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


