# UpdateQuantityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_location_id** | **str** |  | 
**quantity_to_ship** | **int** |  | 
**shipment_item_id** | **int** |  | 
**shipping_plan_id** | **int** |  | 
**stock_item_int_id** | **int** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_quantity_request import UpdateQuantityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuantityRequest from a JSON string
update_quantity_request_instance = UpdateQuantityRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateQuantityRequest.to_json())

# convert the object into a dict
update_quantity_request_dict = update_quantity_request_instance.to_dict()
# create an instance of UpdateQuantityRequest from a dict
update_quantity_request_from_dict = UpdateQuantityRequest.from_dict(update_quantity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


