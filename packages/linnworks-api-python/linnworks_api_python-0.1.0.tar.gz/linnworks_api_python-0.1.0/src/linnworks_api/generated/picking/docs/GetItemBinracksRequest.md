# GetItemBinracksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | Stock item Id | [optional] 
**stock_location_id** | **str** | Linnworks stock location Id | [optional] 
**current_bin_rack_suggestion** | **str** | The name of the location that is currently set to pick from | [optional] 
**include_non_pick_locations** | **bool** | If true, the response will also contain binracks that cannot be selected to pick from | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.get_item_binracks_request import GetItemBinracksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetItemBinracksRequest from a JSON string
get_item_binracks_request_instance = GetItemBinracksRequest.from_json(json)
# print the JSON string representation of the object
print(GetItemBinracksRequest.to_json())

# convert the object into a dict
get_item_binracks_request_dict = get_item_binracks_request_instance.to_dict()
# create an instance of GetItemBinracksRequest from a dict
get_item_binracks_request_from_dict = GetItemBinracksRequest.from_dict(get_item_binracks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


