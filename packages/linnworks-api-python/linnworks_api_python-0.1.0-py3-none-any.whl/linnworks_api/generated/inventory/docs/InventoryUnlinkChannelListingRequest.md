# InventoryUnlinkChannelListingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_ref_id** | **str** | ChannelRefId | [optional] 
**source** | **str** | Source | [optional] 
**sub_source** | **str** | Subsource | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_unlink_channel_listing_request import InventoryUnlinkChannelListingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUnlinkChannelListingRequest from a JSON string
inventory_unlink_channel_listing_request_instance = InventoryUnlinkChannelListingRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUnlinkChannelListingRequest.to_json())

# convert the object into a dict
inventory_unlink_channel_listing_request_dict = inventory_unlink_channel_listing_request_instance.to_dict()
# create an instance of InventoryUnlinkChannelListingRequest from a dict
inventory_unlink_channel_listing_request_from_dict = InventoryUnlinkChannelListingRequest.from_dict(inventory_unlink_channel_listing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


