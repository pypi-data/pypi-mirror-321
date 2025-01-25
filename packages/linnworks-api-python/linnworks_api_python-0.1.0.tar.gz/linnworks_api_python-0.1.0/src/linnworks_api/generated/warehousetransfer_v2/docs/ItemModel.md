# ItemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | **str** |  | [optional] 
**fnsku** | **str** |  | [optional] 
**label_owner** | **str** |  | [optional] 
**manufacturing_lot_code** | **str** |  | [optional] 
**msku** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**thumbnail_source** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**prep_instructions** | [**List[PrepInstructionsModel]**](PrepInstructionsModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.item_model import ItemModel

# TODO update the JSON string below
json = "{}"
# create an instance of ItemModel from a JSON string
item_model_instance = ItemModel.from_json(json)
# print the JSON string representation of the object
print(ItemModel.to_json())

# convert the object into a dict
item_model_dict = item_model_instance.to_dict()
# create an instance of ItemModel from a dict
item_model_from_dict = ItemModel.from_dict(item_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


