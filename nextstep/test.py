from proj.tasks import  add

# result=add.delay(4,4)
result=add.apply_async((4,4))
print(result.ready())
print(result.get(timeout=1))

s1=add.s(4,4)
result=s1.delay()
print(result.get())