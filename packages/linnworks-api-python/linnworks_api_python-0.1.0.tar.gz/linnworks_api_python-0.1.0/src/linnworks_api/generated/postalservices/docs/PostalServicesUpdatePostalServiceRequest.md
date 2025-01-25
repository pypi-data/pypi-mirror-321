# PostalServicesUpdatePostalServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_service_details** | [**PostalService**](PostalService.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.postalservices.models.postal_services_update_postal_service_request import PostalServicesUpdatePostalServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostalServicesUpdatePostalServiceRequest from a JSON string
postal_services_update_postal_service_request_instance = PostalServicesUpdatePostalServiceRequest.from_json(json)
# print the JSON string representation of the object
print(PostalServicesUpdatePostalServiceRequest.to_json())

# convert the object into a dict
postal_services_update_postal_service_request_dict = postal_services_update_postal_service_request_instance.to_dict()
# create an instance of PostalServicesUpdatePostalServiceRequest from a dict
postal_services_update_postal_service_request_from_dict = PostalServicesUpdatePostalServiceRequest.from_dict(postal_services_update_postal_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


