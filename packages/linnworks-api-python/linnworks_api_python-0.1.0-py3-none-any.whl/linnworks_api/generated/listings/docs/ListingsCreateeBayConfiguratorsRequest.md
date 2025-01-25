# ListingsCreateeBayConfiguratorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[EbayConfig]**](EbayConfig.md) | Configs to create | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_createe_bay_configurators_request import ListingsCreateeBayConfiguratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsCreateeBayConfiguratorsRequest from a JSON string
listings_createe_bay_configurators_request_instance = ListingsCreateeBayConfiguratorsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsCreateeBayConfiguratorsRequest.to_json())

# convert the object into a dict
listings_createe_bay_configurators_request_dict = listings_createe_bay_configurators_request_instance.to_dict()
# create an instance of ListingsCreateeBayConfiguratorsRequest from a dict
listings_createe_bay_configurators_request_from_dict = ListingsCreateeBayConfiguratorsRequest.from_dict(listings_createe_bay_configurators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


