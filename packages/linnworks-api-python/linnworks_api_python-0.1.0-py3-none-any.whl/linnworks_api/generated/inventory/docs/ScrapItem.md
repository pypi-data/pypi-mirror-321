# ScrapItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**item_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**category_name** | **str** |  | [optional] 
**scrap_reason** | **str** |  | [optional] 
**total_cost** | **float** |  | [optional] 
**user_name** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**stock_location_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.scrap_item import ScrapItem

# TODO update the JSON string below
json = "{}"
# create an instance of ScrapItem from a JSON string
scrap_item_instance = ScrapItem.from_json(json)
# print the JSON string representation of the object
print(ScrapItem.to_json())

# convert the object into a dict
scrap_item_dict = scrap_item_instance.to_dict()
# create an instance of ScrapItem from a dict
scrap_item_from_dict = ScrapItem.from_dict(scrap_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


