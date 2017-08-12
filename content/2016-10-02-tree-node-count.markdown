---
Title: BST node count
Date: 2016-10-02 14:39:10 +0900
Tags: algorithm
---
# BST 에서 node 갯수 세기 
left/right sub tree 의 children 숫자가 미리 주어졌을 때, 입력된 node 보다 큰 수 or 작은 수의 갯수 구하기  

## 입력 node 보다 작은 숫자 구하기  
1. start root  
2. 만약 입력 데이터보다 해당 노드의 숫자가 크다면(if input < node.value), 왼쪽 노드로 이동  
3. 만약 입력 데이터보다 해당 노드의 숫자가 작다면(if input >= node.value), count 변수에 해당 node 의 left sub tree 의 node 숫자 + 1(해당 node) 을 더하고, 오른쪽으로 이동.  
4. 이동한 node 가 null 인 경우까지 반복  
```python 
def count_less(node, input, count):
    if node is None:
        return count
    if node.value > input:
        count += count_less(node.left, input, count)
    elif node.value < input:
        count += node.leftchildren + 1 + count_less(node.right, input, count)
    elif node.value == input:
        count += node.leftchildren
    return count
```
    
## 입력 node 보다 큰 숫자 구하기  
1. start root 
2. 만약 입력 데이터보다 해당 노드의 숫자가 크다면(if input < node.value), count 변수에 해당 node 의 right sub tree 의 node 숫자 + 1(해당 node) 을 더하고, 왼쪽 자식으로 이동. 
3. 만약 입력 데이터보다 해당 노드의 숫자가 작다면(if input >= node.value), 오른쪽 자식으로 이동 
4. 이동한 node 가 null 인 경우까지 반복 

```python
def count_more(node, input, count):
    if node is None:
        return count
    if node.value < input:
        count += count_more(node.right, input, count)
    elif node.value > input:
        count += node.rightchildren + 1 + count_more(node.left, input, count)
    elif node.value == input:
        count += node.rightchildren
    return count

```

전체 코드  
https://github.com/freeeebie/algorithm-study/blob/master/tree/count_less_greater_nodes.py

---
reference  
https://www.careercup.com/question?id=5165570324430848
