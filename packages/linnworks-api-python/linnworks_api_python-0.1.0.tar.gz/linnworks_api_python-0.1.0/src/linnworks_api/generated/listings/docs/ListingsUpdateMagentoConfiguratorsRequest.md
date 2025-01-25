# ListingsUpdateMagentoConfiguratorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[MagentoConfig]**](MagentoConfig.md) | Configs to update | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_update_magento_configurators_request import ListingsUpdateMagentoConfiguratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsUpdateMagentoConfiguratorsRequest from a JSON string
listings_update_magento_configurators_request_instance = ListingsUpdateMagentoConfiguratorsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsUpdateMagentoConfiguratorsRequest.to_json())

# convert the object into a dict
listings_update_magento_configurators_request_dict = listings_update_magento_configurators_request_instance.to_dict()
# create an instance of ListingsUpdateMagentoConfiguratorsRequest from a dict
listings_update_magento_configurators_request_from_dict = ListingsUpdateMagentoConfiguratorsRequest.from_dict(listings_update_magento_configurators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


