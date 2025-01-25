# ListingsUpdateeBayConfiguratorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[EbayConfig]**](EbayConfig.md) | Configs to update | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_updatee_bay_configurators_request import ListingsUpdateeBayConfiguratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsUpdateeBayConfiguratorsRequest from a JSON string
listings_updatee_bay_configurators_request_instance = ListingsUpdateeBayConfiguratorsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsUpdateeBayConfiguratorsRequest.to_json())

# convert the object into a dict
listings_updatee_bay_configurators_request_dict = listings_updatee_bay_configurators_request_instance.to_dict()
# create an instance of ListingsUpdateeBayConfiguratorsRequest from a dict
listings_updatee_bay_configurators_request_from_dict = ListingsUpdateeBayConfiguratorsRequest.from_dict(listings_updatee_bay_configurators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


