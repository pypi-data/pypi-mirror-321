# PostalService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_service_name** | **str** |  | [optional] 
**postal_service_tag** | **str** |  | [optional] 
**service_country** | **str** |  | [optional] 
**postal_service_code** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**print_module** | **str** |  | [optional] 
**print_module_title** | **str** |  | [optional] 
**pk_postal_service_id** | **str** |  | [optional] 
**tracking_number_required** | **bool** |  | [optional] 
**weight_required** | **bool** |  | [optional] 
**ignore_packaging_group** | **bool** |  | [optional] 
**fk_shipping_api_config_id** | **int** |  | [optional] 
**integrated_service_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.postalservices.models.postal_service import PostalService

# TODO update the JSON string below
json = "{}"
# create an instance of PostalService from a JSON string
postal_service_instance = PostalService.from_json(json)
# print the JSON string representation of the object
print(PostalService.to_json())

# convert the object into a dict
postal_service_dict = postal_service_instance.to_dict()
# create an instance of PostalService from a dict
postal_service_from_dict = PostalService.from_dict(postal_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


