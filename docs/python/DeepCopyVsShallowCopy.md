# DeepCopy vs ShallowCopy vs Normal Copy

In Python, copying objects can be a bit tricky due to the difference between deepcopy, shallow copy, and normal assignment.

## Normal Copy

Normal assignment in Python creates a reference to the original object. Changes made in the new variable will affect the original object.

```python

original_list = [1, 2, 3]
copied_list = original_list
copied_list.append(4)

print(original_list)  # Output: [1, 2, 3, 4]

```

## Shallow Copy
Shallow copy creates a new object but does not create copies of nested objects. Changes made to nested objects will affect both the original and the shallow copy.

```python
import copy

original_list = [1, [2, 3], 4]
shallow_copy = copy.copy(original_list)
shallow_copy[1].append(5)

print(original_list)  # Output: [1, [2, 3, 5], 4]
```

## DeepCopy
Deepcopy creates a new object and recursively adds copies of nested objects. Changes made to the deep copy do not affect the original object or its nested objects.

```python
import copy

original_list = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original_list)
deep_copy[1].append(5)

print(original_list)  # Output: [1, [2, 3], 4]
```

In summary:

**Normal Copy:** Shares references. Changes in the copy reflect in the original.
**Shallow Copy:** Creates a new object, but nested objects are shared. Changes in the nested objects reflect in both the original and the copy.
**Deep Copy:** Creates a new object and recursively creates copies of all nested objects. Changes in the deep copy do not affect the original object.