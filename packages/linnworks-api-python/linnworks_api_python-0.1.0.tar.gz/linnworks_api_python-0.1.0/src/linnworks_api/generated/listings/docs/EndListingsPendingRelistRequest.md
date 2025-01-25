# EndListingsPendingRelistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listings** | [**List[EbayListingAudit]**](EbayListingAudit.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.end_listings_pending_relist_request import EndListingsPendingRelistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndListingsPendingRelistRequest from a JSON string
end_listings_pending_relist_request_instance = EndListingsPendingRelistRequest.from_json(json)
# print the JSON string representation of the object
print(EndListingsPendingRelistRequest.to_json())

# convert the object into a dict
end_listings_pending_relist_request_dict = end_listings_pending_relist_request_instance.to_dict()
# create an instance of EndListingsPendingRelistRequest from a dict
end_listings_pending_relist_request_from_dict = EndListingsPendingRelistRequest.from_dict(end_listings_pending_relist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


