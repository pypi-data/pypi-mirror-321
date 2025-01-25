# Supplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_supplier_id** | **str** |  | [optional] 
**supplier_name** | **str** |  | [optional] 
**contact_name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**alternative_address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**post_code** | **str** |  | [optional] 
**telephone_number** | **str** |  | [optional] 
**secondary_tel_number** | **str** |  | [optional] 
**fax_number** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**web_page** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.supplier import Supplier

# TODO update the JSON string below
json = "{}"
# create an instance of Supplier from a JSON string
supplier_instance = Supplier.from_json(json)
# print the JSON string representation of the object
print(Supplier.to_json())

# convert the object into a dict
supplier_dict = supplier_instance.to_dict()
# create an instance of Supplier from a dict
supplier_from_dict = Supplier.from_dict(supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


