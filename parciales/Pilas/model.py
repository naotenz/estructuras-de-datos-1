import operator as op

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Model:
    OPERATORS = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

    def __init__(self):
        self.root = None
        self.pila_numeros = []
        self.pila_operadores = []

    # -------------------
    # Función principal
    # -------------------
    def to_prefix(self, expr):
        tokens = self._tokenize(expr)
        self.root = self._parse_expr(tokens)
        self.pila_numeros = []
        self.pila_operadores = []
        return self._to_prefix_with_pilas(self.root)

    def evaluate(self, expr):
        if not self.root:
            tokens = self._tokenize(expr)
            self.root = self._parse_expr(tokens)
        return str(self._eval_tree(self.root))

    def get_pilas(self):
        return list(self.pila_numeros), list(self.pila_operadores)

    # -------------------
    # Funciones internas
    # -------------------
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
        # Algoritmo simple para árbol usando precedencia
        output = []
        stack = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

        def pop_stack():
            op_node = stack.pop()
            right = output.pop()
            left = output.pop()
            output.append(Node(op_node, left, right))

        for t in tokens:
            if t.isdigit():
                output.append(Node(t))
            elif t in '+-*/':
                while stack and precedence.get(stack[-1],0) >= precedence[t]:
                    pop_stack()
                stack.append(t)
        while stack:
            pop_stack()
        return output[0]

    def _to_prefix_with_pilas(self, node):
        if not node.left and not node.right:
            self.pila_numeros.append(node.val)
            return node.val
        self.pila_operadores.append(node.val)
        return node.val + self._to_prefix_with_pilas(node.left) + self._to_prefix_with_pilas(node.right)

    def _eval_tree(self, node):
        if not node.left and not node.right:
            return int(node.val)
        left = self._eval_tree(node.left)
        right = self._eval_tree(node.right)
        return self.OPERATORS[node.val](left, right)

