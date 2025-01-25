# PrintingKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_inventory_id** | **int** |  | [optional] 
**key** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.printservice.models.printing_key import PrintingKey

# TODO update the JSON string below
json = "{}"
# create an instance of PrintingKey from a JSON string
printing_key_instance = PrintingKey.from_json(json)
# print the JSON string representation of the object
print(PrintingKey.to_json())

# convert the object into a dict
printing_key_dict = printing_key_instance.to_dict()
# create an instance of PrintingKey from a dict
printing_key_from_dict = PrintingKey.from_dict(printing_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


