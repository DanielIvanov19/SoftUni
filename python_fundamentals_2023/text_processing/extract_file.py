path = input().split("\\")
path_name_extension = path[-1]

name_parts = path_name_extension.split('.')
extension = name_parts.pop()
name = '.'.join(name_parts)
print(f"File name: {name}")
print(f"File extension: {extension}")