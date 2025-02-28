# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
   return ""

# 1
# 12
# 123
# 1234
def number_pattern(n):
   return ""

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
 total = 0
 i = 1
 while i <= n:
  total += i
  i += 1
 return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
  for i in range(0,n):
   for j in range(0,n-i-1):
    print(end= " ")
   for j in range(0,i):
    print ("*", end="")
  return centered_star_pyramid