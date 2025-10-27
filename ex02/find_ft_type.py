def	all_thing_is_obj(object: any) -> int:
	ret = None
	try:
		match object:
			case list():
				ret = f'List: {object}'
			case tuple():
				ret = f'Tuple: {object}'
			case set():
				ret = f'Set: {object}'
			case dict():
				ret = f'Dict: {object}'
			case str():
				ret = f'{object} is in the kitchen : {object}'
			case _:
				ret = "Type not found"
		if ret is not None:
			print(ret)
	except Exception as e:
		print(f"Error: {e}")
	return 42
