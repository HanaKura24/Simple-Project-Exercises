#Measures of Variability

#Get input
data = input("Values: ").split(",")
values = list(map(int, data))
values.sort()
print(values)

#Get mean
ave_sum = sum(values)
n = len(values)
mean =ave_sum/n
print(f"sum: {ave_sum}")
print(f"n: {n}")
print(f"mean: {mean}\n")

#X-mean and square it
var_list = []
for i in values:
    x = i - mean
    y = x**2
    var_list.append(y)
    print(f"{i} = {x} = {y}")

#Variance
var_sum = sum(var_list)
var_n = len(var_list) - 1
variance = var_sum/var_n
print(f"\nvariance sum: {var_sum}")
print(f"variance n-1: {var_n}")
print(f"variance: {variance}")

#Standard Deviation
s = variance**0.5
print(f"standard deviation: {s}")

