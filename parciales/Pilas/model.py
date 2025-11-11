import operator as op

class Model:
    OPERATORS = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

    def __init__(self):
        self.pila_numeros = []
        self.pila_operadores = []

    def to_prefix(self, expr):
        # Convertir la expresión a tokens
        tokens = self._tokenize(expr)
        # Convertir a árbol usando precedencia
        tree = self._parse_expr(tokens)
        # Generar notación prefija
        prefix = self._to_prefix(tree)
        return prefix

    def evaluate(self, expr):
        tokens = self._tokenize(expr)
        tree = self._parse_expr(tokens)
        return str(self._eval_tree(tree))

    # -----------------
    # Funciones internas
    # -----------------
    def _tokenize(self, expr):
        tokens = []
        num = ''
        for c in expr:
            if c.isdigit():
                num += c
            else:
                if num:
                    tokens.append(num)
                    num = ''
                if c in '+-*/':
                    tokens.append(c)
        if num:
            tokens.append(num)
        return tokens

    def _parse_expr(self, tokens):
        # Usaremos algoritmo simple de Shunting-Yard para generar árbol
        output = []
        stack = []

        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

        class Node:
            def __init__(self, val, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        def pop_stack():
            op_node = stack.pop()
            right = output.pop()
            left = output.pop()
            output.append(Node(op_node, left, right))

        for t in tokens:
            if t.isdigit():
                output.append(Node(t))
            elif t in '+-*/':
                while stack and precedence.get(stack[-1], 0) >= precedence[t]:
                    pop_stack()
                stack.append(t)
        while stack:
            pop_stack()
        return output[0]

    def _to_prefix(self, node):
        if not node.left and not node.right:
            return node.val
        return node.val + self._to_prefix(node.left) + self._to_prefix(node.right)

    def _eval_tree(self, node):
        if not node.left and not node.right:
            return int(node.val)
        left = self._eval_tree(node.left)
        right = self._eval_tree(node.right)
        return self.OPERATORS[node.val](left, right)

