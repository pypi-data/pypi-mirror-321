# PostageService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_postal_service_id** | **str** |  | [optional] 
**postal_service_name** | **str** |  | [optional] 
**tracking_number_required** | **bool** |  | [optional] 
**vendor** | **str** |  | [optional] 
**integrated_service_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.postage_service import PostageService

# TODO update the JSON string below
json = "{}"
# create an instance of PostageService from a JSON string
postage_service_instance = PostageService.from_json(json)
# print the JSON string representation of the object
print(PostageService.to_json())

# convert the object into a dict
postage_service_dict = postage_service_instance.to_dict()
# create an instance of PostageService from a dict
postage_service_from_dict = PostageService.from_dict(postage_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


