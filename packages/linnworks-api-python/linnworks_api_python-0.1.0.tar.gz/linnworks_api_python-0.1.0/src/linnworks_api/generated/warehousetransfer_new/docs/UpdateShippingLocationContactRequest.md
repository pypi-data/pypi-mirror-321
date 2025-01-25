# UpdateShippingLocationContactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_location_id** | **str** |  | [optional] 
**name** | **str** |  | 
**company** | **str** |  | [optional] 
**country** | **str** |  | 
**region** | **str** |  | [optional] 
**city** | **str** |  | 
**address1** | **str** |  | 
**address2** | **str** |  | [optional] 
**postcode** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_shipping_location_contact_request import UpdateShippingLocationContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShippingLocationContactRequest from a JSON string
update_shipping_location_contact_request_instance = UpdateShippingLocationContactRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShippingLocationContactRequest.to_json())

# convert the object into a dict
update_shipping_location_contact_request_dict = update_shipping_location_contact_request_instance.to_dict()
# create an instance of UpdateShippingLocationContactRequest from a dict
update_shipping_location_contact_request_from_dict = UpdateShippingLocationContactRequest.from_dict(update_shipping_location_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


