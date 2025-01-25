# PostalServicesCreatePostalServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postal_service_details** | [**PostalServiceWithChannelAndShippingLinks**](PostalServiceWithChannelAndShippingLinks.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.postalservices.models.postal_services_create_postal_service_request import PostalServicesCreatePostalServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostalServicesCreatePostalServiceRequest from a JSON string
postal_services_create_postal_service_request_instance = PostalServicesCreatePostalServiceRequest.from_json(json)
# print the JSON string representation of the object
print(PostalServicesCreatePostalServiceRequest.to_json())

# convert the object into a dict
postal_services_create_postal_service_request_dict = postal_services_create_postal_service_request_instance.to_dict()
# create an instance of PostalServicesCreatePostalServiceRequest from a dict
postal_services_create_postal_service_request_from_dict = PostalServicesCreatePostalServiceRequest.from_dict(postal_services_create_postal_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


