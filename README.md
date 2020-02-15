# ylisp
Build a lisp dialect as short as possible

# spec
```lisp
(print ((lambda (a b) (+ (- a 3) b)) 5 5))
## debug output ##
Tokenized:['print', [['lambda', ['a', 'b'], ['+', ['-', 'a', '3'], 'b']], '5', '5']]
Stacktrace: <built-in function print> ['print', [['lambda', ['a', 'b'], ['+', ['-', 'a', '3'], 'b']], '5', '5']]
Stacktrace: {'body': ['+', ['-', 'a', '3'], 'b'], 'param': ['a', 'b']} [['lambda', ['a', 'b'], ['+', ['-', 'a', '3'], 'b']], '5', '5']
Stacktrace: <function <lambda> at 0x106295410> ['+', ['-', '5', '3'], '5']
Stacktrace: <function <lambda> at 0x106295578> ['-', '5', '3']
```

```lisp
(print (+ 232 32))
## debug output ##
Tokenized:['print', ['+', '232', '32']]
Stacktrace: <built-in function print> ['print', ['+', '232', '32']]
Stacktrace: <function <lambda> at 0x10b56b410> ['+', '232', '32']
264
```