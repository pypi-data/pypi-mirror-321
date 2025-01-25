# CustomerAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**town** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**post_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.customer_address import CustomerAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAddress from a JSON string
customer_address_instance = CustomerAddress.from_json(json)
# print the JSON string representation of the object
print(CustomerAddress.to_json())

# convert the object into a dict
customer_address_dict = customer_address_instance.to_dict()
# create an instance of CustomerAddress from a dict
customer_address_from_dict = CustomerAddress.from_dict(customer_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


