# CreatePOsFromInventoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_create** | [**List[MyInventoryPOCreationItems]**](MyInventoryPOCreationItems.md) | A list of items that should either be added to a PO, either new or existing, depending on data | [optional] 
**location_id** | **str** | Linnworks stock location id | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.create_pos_from_inventory_request import CreatePOsFromInventoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePOsFromInventoryRequest from a JSON string
create_pos_from_inventory_request_instance = CreatePOsFromInventoryRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePOsFromInventoryRequest.to_json())

# convert the object into a dict
create_pos_from_inventory_request_dict = create_pos_from_inventory_request_instance.to_dict()
# create an instance of CreatePOsFromInventoryRequest from a dict
create_pos_from_inventory_request_from_dict = CreatePOsFromInventoryRequest.from_dict(create_pos_from_inventory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


