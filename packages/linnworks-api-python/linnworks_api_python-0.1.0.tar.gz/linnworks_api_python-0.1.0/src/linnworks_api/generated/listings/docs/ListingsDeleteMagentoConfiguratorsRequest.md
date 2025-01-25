# ListingsDeleteMagentoConfiguratorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | **List[str]** | Configs guid | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_delete_magento_configurators_request import ListingsDeleteMagentoConfiguratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsDeleteMagentoConfiguratorsRequest from a JSON string
listings_delete_magento_configurators_request_instance = ListingsDeleteMagentoConfiguratorsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsDeleteMagentoConfiguratorsRequest.to_json())

# convert the object into a dict
listings_delete_magento_configurators_request_dict = listings_delete_magento_configurators_request_instance.to_dict()
# create an instance of ListingsDeleteMagentoConfiguratorsRequest from a dict
listings_delete_magento_configurators_request_from_dict = ListingsDeleteMagentoConfiguratorsRequest.from_dict(listings_delete_magento_configurators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


