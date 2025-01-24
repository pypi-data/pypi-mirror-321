# coding: utf-8
# %load type_kwargs
def detect_type(**kwargs):
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k, "est", type(k))
        print(v, "est", type(v))
        print()
        
