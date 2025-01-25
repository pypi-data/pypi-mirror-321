# ListingsCreateMagentoConfiguratorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[MagentoConfig]**](MagentoConfig.md) | Configs to create | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_create_magento_configurators_request import ListingsCreateMagentoConfiguratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsCreateMagentoConfiguratorsRequest from a JSON string
listings_create_magento_configurators_request_instance = ListingsCreateMagentoConfiguratorsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsCreateMagentoConfiguratorsRequest.to_json())

# convert the object into a dict
listings_create_magento_configurators_request_dict = listings_create_magento_configurators_request_instance.to_dict()
# create an instance of ListingsCreateMagentoConfiguratorsRequest from a dict
listings_create_magento_configurators_request_from_dict = ListingsCreateMagentoConfiguratorsRequest.from_dict(listings_create_magento_configurators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


