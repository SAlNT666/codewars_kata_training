# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863

def loop_size(node):
    p1 = node
    p2 = node.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next.next
    count = 1
    p1 = p1.next
    while p1 != p2:
        p1 = p1.next
        count += 1
    return count
