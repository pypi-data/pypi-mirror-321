# PostalServicesDeletePostalServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_to_delete** | **str** | Postal service ID to delete | [optional] 

## Example

```python
from linnworks_api.generated.postalservices.models.postal_services_delete_postal_service_request import PostalServicesDeletePostalServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostalServicesDeletePostalServiceRequest from a JSON string
postal_services_delete_postal_service_request_instance = PostalServicesDeletePostalServiceRequest.from_json(json)
# print the JSON string representation of the object
print(PostalServicesDeletePostalServiceRequest.to_json())

# convert the object into a dict
postal_services_delete_postal_service_request_dict = postal_services_delete_postal_service_request_instance.to_dict()
# create an instance of PostalServicesDeletePostalServiceRequest from a dict
postal_services_delete_postal_service_request_from_dict = PostalServicesDeletePostalServiceRequest.from_dict(postal_services_delete_postal_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


