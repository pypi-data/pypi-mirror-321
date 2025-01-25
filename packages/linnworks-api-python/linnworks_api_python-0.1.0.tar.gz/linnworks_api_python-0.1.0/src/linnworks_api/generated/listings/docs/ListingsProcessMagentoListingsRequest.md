# ListingsProcessMagentoListingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MagentoListing]**](MagentoListing.md) | Magento listings | [optional] 
**force** | **bool** | force | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_process_magento_listings_request import ListingsProcessMagentoListingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsProcessMagentoListingsRequest from a JSON string
listings_process_magento_listings_request_instance = ListingsProcessMagentoListingsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsProcessMagentoListingsRequest.to_json())

# convert the object into a dict
listings_process_magento_listings_request_dict = listings_process_magento_listings_request_instance.to_dict()
# create an instance of ListingsProcessMagentoListingsRequest from a dict
listings_process_magento_listings_request_from_dict = ListingsProcessMagentoListingsRequest.from_dict(listings_process_magento_listings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


