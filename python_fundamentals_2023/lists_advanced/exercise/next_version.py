version_list = input().split('.')
version = list(map(int, version_list))

if version[2] < 9:
    version[2] += 1
else:
    version[2] = 0
    if version[1] < 9:
        version[1] += 1
    else:
        version[1] = 0
        version[0] += 1

version_to_str = list(map(str, version))

print('.'.join(version_to_str))
