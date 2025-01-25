# EbaySpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec_name** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 
**linnworks_property** | **str** |  | [optional] 
**possible_values** | **List[str]** |  | [optional] 
**association_table** | [**AssociationTable**](AssociationTable.md) |  | [optional] 
**category_ids** | **List[int]** |  | [optional] 
**is_user_defined** | **bool** |  | [optional] 
**is_required** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.ebay_specification import EbaySpecification

# TODO update the JSON string below
json = "{}"
# create an instance of EbaySpecification from a JSON string
ebay_specification_instance = EbaySpecification.from_json(json)
# print the JSON string representation of the object
print(EbaySpecification.to_json())

# convert the object into a dict
ebay_specification_dict = ebay_specification_instance.to_dict()
# create an instance of EbaySpecification from a dict
ebay_specification_from_dict = EbaySpecification.from_dict(ebay_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


