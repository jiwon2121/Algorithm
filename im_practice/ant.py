
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p += t
q += t

x = (p%w) -((p//w)%2)*(2*(p%w) - w)
y = (q%h) -((q//h)%2)*(2*(q%h) - h)

print(x, y)
