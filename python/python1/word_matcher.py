__author__ = 'chris'
"""Find matching words in two input strings.
   Because the sets are not sorted, the program prints them in unpredictable order.
"""
words1 = set(input("Sentence 1: ").lower().split())
words2 = set(input("Sentence 2: ").lower().split())
print("Words in both strings", words1 & words2)
print("Words unique to setence 1: ", words1 - words2)
print("Words unique to setence 2: ", words2 - words1)