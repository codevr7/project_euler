def classtree(cls,indent):
    print('.' * indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls,indent+3)


def instance_tree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)

def test():
    class a: pass
    class b(a): pass
    class c(a): pass
    class d(b,c): pass
    class e: pass
    class f(d,e): pass

    instance_tree(b())
    instance_tree(f())

if __name__ == '__main__': test()
