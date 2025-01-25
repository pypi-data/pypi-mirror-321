# TransportationContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.transportation_contact import TransportationContact

# TODO update the JSON string below
json = "{}"
# create an instance of TransportationContact from a JSON string
transportation_contact_instance = TransportationContact.from_json(json)
# print the JSON string representation of the object
print(TransportationContact.to_json())

# convert the object into a dict
transportation_contact_dict = transportation_contact_instance.to_dict()
# create an instance of TransportationContact from a dict
transportation_contact_from_dict = TransportationContact.from_dict(transportation_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


