# ListingsCancelListingBulkOperationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_operation_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_cancel_listing_bulk_operation_request import ListingsCancelListingBulkOperationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsCancelListingBulkOperationRequest from a JSON string
listings_cancel_listing_bulk_operation_request_instance = ListingsCancelListingBulkOperationRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsCancelListingBulkOperationRequest.to_json())

# convert the object into a dict
listings_cancel_listing_bulk_operation_request_dict = listings_cancel_listing_bulk_operation_request_instance.to_dict()
# create an instance of ListingsCancelListingBulkOperationRequest from a dict
listings_cancel_listing_bulk_operation_request_from_dict = ListingsCancelListingBulkOperationRequest.from_dict(listings_cancel_listing_bulk_operation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


