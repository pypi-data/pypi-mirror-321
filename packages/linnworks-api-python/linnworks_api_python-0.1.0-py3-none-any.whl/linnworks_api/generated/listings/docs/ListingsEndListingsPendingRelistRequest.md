# ListingsEndListingsPendingRelistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**EndListingsPendingRelistRequest**](EndListingsPendingRelistRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_end_listings_pending_relist_request import ListingsEndListingsPendingRelistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsEndListingsPendingRelistRequest from a JSON string
listings_end_listings_pending_relist_request_instance = ListingsEndListingsPendingRelistRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsEndListingsPendingRelistRequest.to_json())

# convert the object into a dict
listings_end_listings_pending_relist_request_dict = listings_end_listings_pending_relist_request_instance.to_dict()
# create an instance of ListingsEndListingsPendingRelistRequest from a dict
listings_end_listings_pending_relist_request_from_dict = ListingsEndListingsPendingRelistRequest.from_dict(listings_end_listings_pending_relist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


