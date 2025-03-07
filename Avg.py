n = int(input())
total_sum = 0
for _ in range(n):
    num = int(input()) 
    total_sum += num 
average = total_sum / n
print(f"The average is: {average:.2f}")
