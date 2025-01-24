# Information
	using this package requires rust and cargo to be installed, as this is a rust binding made with maturin for use in python projects

# Usage
```python
	from rjson import loads, dumps
	text = '["sup", "lol", "haha"]'
	data = loads(text)
	print(data)
	dumped = dumps(data)
	print(dumped)
```

