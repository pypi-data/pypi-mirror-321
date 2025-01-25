# AmazonPrepInstructionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prep_instruction** | [**SkuPrepInstruction**](SkuPrepInstruction.md) |  | [optional] 
**currency_code** | **str** |  | [optional] 
**currency_value** | **float** |  | [optional] 
**prep_owner** | [**PrepOwners**](PrepOwners.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.amazon_prep_instruction_item import AmazonPrepInstructionItem

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonPrepInstructionItem from a JSON string
amazon_prep_instruction_item_instance = AmazonPrepInstructionItem.from_json(json)
# print the JSON string representation of the object
print(AmazonPrepInstructionItem.to_json())

# convert the object into a dict
amazon_prep_instruction_item_dict = amazon_prep_instruction_item_instance.to_dict()
# create an instance of AmazonPrepInstructionItem from a dict
amazon_prep_instruction_item_from_dict = AmazonPrepInstructionItem.from_dict(amazon_prep_instruction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


