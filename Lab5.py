# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
   result = ""
   row = 1
   while row <= n:
      if row == 1 or row == n:
         result += "*" * n + "\n"
      else:
         result += "*" + " " * (n-2) + "*" + "\n"
      row += 1
   return result.strip()
   # needed help
# 1
# 12
# 123
# 1234
def number_pattern(n):
   result = ""
   row = 1
   while row <= n:
     number = 1
     line = ""
     while number <= row:
      result += line + "\n"
     row += 1
     # do not know what to do
   return result.stip()
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
   result = ""
   row = 1
   while row <= n:
    spaces = " " * (n - row)
    stars = "*" * (2 * row - 1)
    line = spaces + stars
    result += line
    if row != n:  
         result += "\n"
    row += 1
   return result
# needed help