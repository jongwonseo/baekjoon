import sys

input = sys.stdin.readline

name = input().strip()
print(name)
n = int(input())
arr = [[0 for i in range(26)] for i in range(len(name))]
arr[0][ord(name[0]) - 97] = 1

print(name)
print(ord(name[0]))