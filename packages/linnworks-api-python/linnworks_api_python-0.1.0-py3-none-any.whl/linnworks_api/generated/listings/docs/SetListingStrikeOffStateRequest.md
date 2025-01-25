# SetListingStrikeOffStateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_audits** | [**List[EbayListingAudit]**](EbayListingAudit.md) | Listing audit details | [optional] 
**listings** | [**List[EBayItem]**](EBayItem.md) | Channel Listings | [optional] 
**strike_reason** | **str** | Reason of strike off | [optional] 
**strike_off_state** | **bool** | Listing strike off state | [optional] 
**listings_status** | **str** | Status of listings search | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.set_listing_strike_off_state_request import SetListingStrikeOffStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetListingStrikeOffStateRequest from a JSON string
set_listing_strike_off_state_request_instance = SetListingStrikeOffStateRequest.from_json(json)
# print the JSON string representation of the object
print(SetListingStrikeOffStateRequest.to_json())

# convert the object into a dict
set_listing_strike_off_state_request_dict = set_listing_strike_off_state_request_instance.to_dict()
# create an instance of SetListingStrikeOffStateRequest from a dict
set_listing_strike_off_state_request_from_dict = SetListingStrikeOffStateRequest.from_dict(set_listing_strike_off_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


