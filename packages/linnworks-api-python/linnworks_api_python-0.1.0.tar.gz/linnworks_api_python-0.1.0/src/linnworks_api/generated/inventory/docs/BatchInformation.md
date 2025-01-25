# BatchInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | Stock item id | [optional] 
**item_batch_information** | [**List[StockItemBatch]**](StockItemBatch.md) | Stock item batch data | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.batch_information import BatchInformation

# TODO update the JSON string below
json = "{}"
# create an instance of BatchInformation from a JSON string
batch_information_instance = BatchInformation.from_json(json)
# print the JSON string representation of the object
print(BatchInformation.to_json())

# convert the object into a dict
batch_information_dict = batch_information_instance.to_dict()
# create an instance of BatchInformation from a dict
batch_information_from_dict = BatchInformation.from_dict(batch_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


