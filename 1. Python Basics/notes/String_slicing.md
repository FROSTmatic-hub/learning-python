# What is String Slicing?
- String slicing is the process of extracting certain portion of a string
- It follows the syntax `variable[start:stop:step]`

| Start | Tells where to start   | Default is `0`                         |
| ----- | ---------------------- | -------------------------------------- |
| Stop  | Tells where to stop    | Default is the end of the string index |
| Step  | How many steps to take | Default is `1`                         |
```python
name = "shaafi"
name2 = name[0:3]
# THe output will be shaa
```

> [!IMPORTANT]
>The `stop` index DOES NOT GET INCLUDED