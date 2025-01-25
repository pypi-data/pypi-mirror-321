# ListingsProcesseBayListingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EbayListing]**](EbayListing.md) | eBay listings | [optional] 
**force** | **bool** | force | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_processe_bay_listings_request import ListingsProcesseBayListingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsProcesseBayListingsRequest from a JSON string
listings_processe_bay_listings_request_instance = ListingsProcesseBayListingsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsProcesseBayListingsRequest.to_json())

# convert the object into a dict
listings_processe_bay_listings_request_dict = listings_processe_bay_listings_request_instance.to_dict()
# create an instance of ListingsProcesseBayListingsRequest from a dict
listings_processe_bay_listings_request_from_dict = ListingsProcesseBayListingsRequest.from_dict(listings_processe_bay_listings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


