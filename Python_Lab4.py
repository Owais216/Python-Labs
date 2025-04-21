#   Stack:----

# class Stack:
#     def __init__(self):
#         self.stack = []
    
#     def push(self, element):
#         self.stack.append(element)
    
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack.pop()
    
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.stack[-1]
    
#     def isEmpty(self):
#         return len(self.stack) == 0
    
#     def size(self):
#         return len(self.stack)




# # Create a stack

# myStack = Stack()

# myStack.push('A')
# myStack.push('B')
# myStack.push('C')

# print("Stack: ", myStack.stack)

# print("Pop: ", myStack.pop())

# print("Peek: ", myStack.peek())

# print("Is Stack Empty? ", myStack.isEmpty())

# print("Size: ", myStack.size())

#   Queue:-----

# class Queue:
#     def __init__(self):
#         self.queue = []
    
#     def enqueue(self, element):
#         self.queue.append(element)
    
#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.queue.pop(0)
    
#     def peek(self):
#         if self.isEmpty():
#             return "Queue is empty"
#         return self.queue[0]
    
#     def isEmpty(self):
#         return len(self.queue) == 0
    
#     def size(self):
#         return len(self.queue)



# # Create a queue

# myQueue = Queue()

# myQueue.enqueue('A')
# myQueue.enqueue('B')
# myQueue.enqueue('C')

# print("Queue: ", myQueue.queue)

# print("Dequeue: ", myQueue.dequeue())

# print("Peek: ", myQueue.peek())

# print("Is Stack Empty? ", myQueue.isEmpty())

# print("Size: ", myQueue.size())


#P

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
if __name__ == "__main__":
    sorted_array = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    targets = [23, 5, 91, 100]
    
    for target in targets:
        result = binary_search(sorted_array, target)
        if result != -1:
            print(f"Element {target} found at index {result}")
        else:
            print(f"Element {target} not found in the array")
    
    print("\nStep-by-step demonstration for target = 23:")
    arr = sorted_array
    target = 23
    left = 0
    right = len(arr) - 1
    
    step = 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"Found target {target} at index {mid}")
            break
        elif arr[mid] < target:
            print(f"arr[mid]={arr[mid]} < target={target}, search right half")
            left = mid + 1
        else:
            print(f"arr[mid]={arr[mid]} > target={target}, search left half")
            right = mid - 1
            
        step+=1
