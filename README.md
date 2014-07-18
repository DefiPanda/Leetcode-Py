Leetcode  
===  
  
This is my solution to Leetcode Online Judge's problems. Currently I am revamping the problems all over again towards more idiomatic Python. Stay tuned for updates.  

Feel free to submit pull requests for submitting more elegant solution.

###List of idiomatic Python I prefer (as of now)  
---  
- Prefer list comprehension over map / filter.  
```
	# from Gray Code

	# Bad
	def grayCode(self, n):
        return map(lambda x: (x / 2) ^ x, range(1 << n))

	# Idiomatic
	def grayCode(self, n):
        return [(x / 2) ^ x for x in range(1 << n)]
```
- Prefer using `in` keyword over repetitive variable in conditional statement.  
```
	# from Post Order Traversal

	# Bad
	if parent.right == None or parent.right == prev

	# Idiomatic
	if parent.right in (None, prev):
```
- Prefer using docstring over single line comment when describing functionality of a method.
```
	# from Search Insert Position

	# Bad
	# Iterative solution is also fine.
	def searchInsert(self, A, target):

	# Idiomatic
	def searchInsert(self, A, target):
    	"""Iterative solution is also fine.
    	"""
```
- Prefer implicit evaluation of condition (e.g. `if`, `while`, etc.) over explicit comparison in condition.  
Notice empty list and dictionary will be evaluated to False, so that is very handy.  
```
	# from Binary Tree Preorder Traversal

	# Bad
	while len(stack) > 0:
		current = stack.pop()

	# Idiomatic
	while stack:
		current = stack.pop()
```
- Prefer `is None` over `== None`. Notice `is` looks for referential equality, and `None` is a singleton.  
The fundamental reason for this preference is much improved speed, and `==` can be overriden by `__eq__`.
```
	# from Binary Tree Preorder Traversal

	# Bad
	if root == None:

	# Idiomatic
	if root is None:
```
One interesting side note in Python regarding this is on [Stackoverflow](http://stackoverflow.com/questions/306313/python-is-operator-behaves-unexpectedly-with-integers/306347). Trust me, that is worth your 60 seconds of time. But that only works in REPL though, not on a executable python file.  
  
READ THIS or above two rules will only do you harm:  
Sometimes you have to use `if foo is not None` over `if foo`. For example, if foo is 0, then `if foo` will become False. But 0 is not None. Just watch out. A rule of the thumb is if you want to check if the default argument of a function is None, then use `if foo is not None`, otherwise you can most likely use `if foo` if you know what you are doing.  
- Consider using enumerate when index accessing looks verbose  
```
	# from Two Sum

	# Bad
	for i in range(len(nums)):
        if target - nums[i] in lookup:
            return (lookup[target - nums[i]] + 1, i + 1)
        lookup[nums[i]] = i

    # Idiomatic
    for i, num in enumerate(nums):
        if target - num in lookup:
            return (lookup[target - num] + 1, i + 1)
        lookup[num] = i
```  
- Readability counts.  
   
 "Any fool can write code that a computer can understand. Good programmers write code that humans can understand." Martin Fowler is right.
```
	# from Edit Distance

	# Bad
	def minDistance(self, word1, word2):
        distance = [[i] for i in range(len(word1) + 1)]
        distance[0] = [i for i in range(len(word2) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                distance[i].append(min(distance[i - 1][j] + 1, distance[i][j - 1] + 1, distance[i - 1][j - 1] + (word1[i - 1] != word2[j - 1])))
        return distance[-1][-1]

    # Idiomatic
    def minDistance(self, word1, word2):
        distance = [[i] for i in range(len(word1) + 1)]
        distance[0] = [i for i in range(len(word2) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                deletion = distance[i - 1][j] + 1
                addition = distance[i][j - 1] + 1
                substitution = distance[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    substitution += 1
                distance[i].append(min(deletion, addition, substitution))
        return distance[-1][-1]