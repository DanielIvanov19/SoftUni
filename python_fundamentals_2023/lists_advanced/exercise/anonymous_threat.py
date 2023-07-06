input_string = input().split(" ")

command = input()


def merge_elements(elements, start, end):
    merge_res = ''
    for idx in range(start, end + 1):
        merge_res += elements[idx]
    return merge_res


while True:
    line = input()

    if line == "3:1":
        break
    command, first_arg, second_arg = line.split()

    if command == "merge":
        start_index = int(first_arg)
        end_index = int(second_arg)

        start_index = max(0, start_index)
        end_index = min(len(input_string) - 1, end_index)

        if end_index <= start_index:
            continue

        merged = merge_elements(input_string, start_index, end_index)
        remove_count_ops = end_index - start_index + 1
        for _ in range(remove_count_ops):
            input_string.pop(start_index)
        input_string.insert(start_index, merged)
    elif command == "divide":
        index = int(first_arg)
        partitions = int(second_arg)

        # abcd, efgh, ijkl
        # divide 0 3
        element = input_string[index]
        element_parts = []
        partition_size = len(element) // partitions

        current_partition = ''
        for part in range((partitions - 1) * partition_size):
            current_partition += element[index]
            if len(current_partition == partition_size):
                element_parts.append(current_partition)
                current_partition == ''
        current_partition = ''
        for i in range((partitions - 1) * partition_size, len(element)):
            current_partition += element[i]

        element_parts.append(current_partition)

        input_string.pop(index)

        for partition in range(len(element_parts)):
            input_string.insert(index + partition, element_parts[partition])

        print()


print(' '.join(input_string))
