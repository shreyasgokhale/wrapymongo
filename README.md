# WraPyMongo

Wrapper modlue to handle our mongodb requests using pymongodb driver

## Usage

```python
import wrapymongo
wObj = wrapymongo.driver()
wObj.<operation>()
```

## Operations

- ``` defineDB```
   
    Defines a databse


- ``` defineCollection ```

    Defines a collection (Table equivalant of MySQL)


- ```insertOneRecord```

    Insert record in collection.


