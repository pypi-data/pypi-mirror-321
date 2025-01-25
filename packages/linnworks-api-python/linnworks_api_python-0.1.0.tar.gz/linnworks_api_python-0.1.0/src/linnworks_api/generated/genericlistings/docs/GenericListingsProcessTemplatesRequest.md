# GenericListingsProcessTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ProcessTemplatesRequest**](ProcessTemplatesRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.generic_listings_process_templates_request import GenericListingsProcessTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenericListingsProcessTemplatesRequest from a JSON string
generic_listings_process_templates_request_instance = GenericListingsProcessTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(GenericListingsProcessTemplatesRequest.to_json())

# convert the object into a dict
generic_listings_process_templates_request_dict = generic_listings_process_templates_request_instance.to_dict()
# create an instance of GenericListingsProcessTemplatesRequest from a dict
generic_listings_process_templates_request_from_dict = GenericListingsProcessTemplatesRequest.from_dict(generic_listings_process_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


