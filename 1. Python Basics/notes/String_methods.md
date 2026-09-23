# What are some String Methods?
- Some String Methods are:
1. `.upper()`: converts the string into UPPERCASE
```python
name = "shaafi"
upper_name = name.upper()
```
2. `.lower()`: converts the string into lowercase
```python
name = 'SHAAFI'
lower_name = name.lower()
```
3. `.find()`: finds the index value of the first occurence of the text
```python
name = "Shaafi is a boy"
boy1 = name.find("boy")
#output returns 12 which is the first occurence of "b" in "boy"
```
4. `.replace()`: replaces a old text with new
```python
name = "Shaafi is a boy"
man1 = name.replace("boy", "man")
# boy gets replaced with man in a new string. NOT THE EXISITNG name STRING
```