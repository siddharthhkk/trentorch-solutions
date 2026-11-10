def append_all(lst: list, items: list) -> None:
    """
    Add every element of `items` to the end of `lst`, in place,
    so that each element becomes its own new element of `lst`.
    Use extend(). Return nothing.
    """
    lst.extend(items)
    pass


def insert_sorted(lst: list, value) -> None:
    """
    `lst` is sorted in ascending order. Insert `value` in place
    so that the list stays sorted, placing it AFTER any existing
    elements equal to `value`. Use a loop to find the position
    and insert() to add it. Return nothing.

    Example: lst = [1, 3, 3, 5]; insert_sorted(lst, 3)
             -> lst is now [1, 3, 3, 3, 5]
    """
    insert_index = len(lst)
    for i in range(len(lst)):
        if lst[i] > value:
            insert_index = i
            break
    lst.insert(insert_index, value)
    pass


def flatten_one_level(list_of_lists: list) -> list:
    """
    Return a NEW list made of the elements of each inner list,
    in order. Do not change `list_of_lists` or its inner lists.
    Use extend() on a fresh list.

    Example: flatten_one_level([[1, 2], [], [3]]) -> [1, 2, 3]
    """
    ans = []
    for i in list_of_lists:
        ans.extend(i)
    return ans
    pass


def concat_identity_report(lst: list, extra: list) -> list:
    """
    Using the list `lst` given by the caller:
      1. Record id(lst). Perform `lst += extra`. Record whether
         id(lst) is unchanged (call this same_after_iadd).
      2. Record id(lst) again. Perform `lst = lst + extra`.
         Record whether id(lst) is unchanged (same_after_plus).
    Return a list [same_after_iadd, same_after_plus].
    (The caller's original list is changed by step 1 only.)
    """
    id1 = id(lst)
    lst += extra
    same_after_iadd = id(lst) == id1

    id2 = id(lst)
    lst = lst + extra
    same_after_plus = id(lst) == id2
    return [same_after_iadd, same_after_plus]
    pass


def remove_all(lst: list, value) -> None:
    """
    Remove EVERY element equal to `value` from `lst`, in place
    (the caller's list object must keep its id()). Consecutive
    duplicates must all be removed. Return nothing.

    Example: lst = [1, 1, 2, 1]; remove_all(lst, 1)
             -> lst is now [2]
    """
    while value in lst:
        lst.remove(value)
    pass


def pop_last_n(lst: list, n: int) -> list:
    """
    Remove the last `n` elements of `lst` in place and return
    them in their ORIGINAL order as a new list. If n <= 0,
    remove nothing and return []. If n >= len(lst), remove
    everything.

    Example: lst = [1, 2, 3, 4]; pop_last_n(lst, 2) -> [3, 4]
             and lst is now [1, 2]
    """
    if n <= 0: return []
    if n > len(lst): 
        ans = lst[:]
        lst.clear()
        return ans
    ans = lst[-n:]
    del lst[-n:]
    return ans
    pass


def delete_every_other(lst: list) -> None:
    """
    Remove the elements at positions 0, 2, 4, ... from `lst`,
    in place, using del with an extended slice. Return nothing.

    Example: lst = [1, 2, 3, 4, 5] -> lst is now [2, 4]
    """
    del lst[0::2]
    pass


def remove_first_or_report(lst: list, value) -> bool:
    """
    If `value` is in `lst`, remove its first occurrence in place
    and return True. If it is not present, leave `lst` unchanged
    and return False. Check with `in` before removing; do not
    let remove() fail.
    """
    if value in lst:
        lst.remove(value)
        return True
    return False
    pass
