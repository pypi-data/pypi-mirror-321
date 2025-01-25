# ListingsSetListingStrikeOffStateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SetListingStrikeOffStateRequest**](SetListingStrikeOffStateRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_set_listing_strike_off_state_request import ListingsSetListingStrikeOffStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsSetListingStrikeOffStateRequest from a JSON string
listings_set_listing_strike_off_state_request_instance = ListingsSetListingStrikeOffStateRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsSetListingStrikeOffStateRequest.to_json())

# convert the object into a dict
listings_set_listing_strike_off_state_request_dict = listings_set_listing_strike_off_state_request_instance.to_dict()
# create an instance of ListingsSetListingStrikeOffStateRequest from a dict
listings_set_listing_strike_off_state_request_from_dict = ListingsSetListingStrikeOffStateRequest.from_dict(listings_set_listing_strike_off_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


