package_of_pens = 5.8
package_of_markers = 7.2
detergent = 1.2
packages_pens = int(input())
packages_markers = int(input())
liters = int(input())
discount = int(input())
total_sum = packages_markers*package_of_markers + packages_pens*package_of_pens + liters*detergent
discounted_sum = total_sum - total_sum*discount/100
print(discounted_sum)