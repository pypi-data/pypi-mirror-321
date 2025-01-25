# GenericListingsSaveTemplateFieldsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**SaveTemplateFieldsRequest**](SaveTemplateFieldsRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.generic_listings_save_template_fields_request import GenericListingsSaveTemplateFieldsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenericListingsSaveTemplateFieldsRequest from a JSON string
generic_listings_save_template_fields_request_instance = GenericListingsSaveTemplateFieldsRequest.from_json(json)
# print the JSON string representation of the object
print(GenericListingsSaveTemplateFieldsRequest.to_json())

# convert the object into a dict
generic_listings_save_template_fields_request_dict = generic_listings_save_template_fields_request_instance.to_dict()
# create an instance of GenericListingsSaveTemplateFieldsRequest from a dict
generic_listings_save_template_fields_request_from_dict = GenericListingsSaveTemplateFieldsRequest.from_dict(generic_listings_save_template_fields_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


