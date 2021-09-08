Script convert.py converts structure like (from file data.txt):

```
a.b.c: "foo"
a.b.d: "bar"
a.e: "baz"
a.f.g: "qux"
```

into yaml (data.yml):

```
a:
  b:
    c: foo
    d: bar
  e: baz
  f:
    g: qux
```

It doesn't enclose values in yaml with parentheses.