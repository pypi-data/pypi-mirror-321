# UpdatePackQuantityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_location_id** | **str** |  | 
**pack_quantity** | **int** |  | 
**pack_size** | **int** |  | 
**shipment_item_id** | **int** |  | 
**shipping_plan_id** | **int** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_pack_quantity_request import UpdatePackQuantityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePackQuantityRequest from a JSON string
update_pack_quantity_request_instance = UpdatePackQuantityRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePackQuantityRequest.to_json())

# convert the object into a dict
update_pack_quantity_request_dict = update_pack_quantity_request_instance.to_dict()
# create an instance of UpdatePackQuantityRequest from a dict
update_pack_quantity_request_from_dict = UpdatePackQuantityRequest.from_dict(update_pack_quantity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


