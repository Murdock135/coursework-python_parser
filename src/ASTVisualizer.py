#!/usr/bin/env python3
"""
AST Visualizer for minipython
Usage: python astvisualizer.py <input_file.py> [-o OUTPUT_PATH]

Generates:
  - ast.dot: DOT format representation
  - ast.png: PNG visualization
  - ast.svg: SVG visualization
"""

import sys
import argparse
import subprocess
from pathlib import Path
from antlr4 import InputStream, CommonTokenStream
from .IndentLexer import IndentLexer
from generated.minipythonParser import minipythonParser
from generated.minipythonVisitor import minipythonVisitor


class ASTVisualizer(minipythonVisitor):
    """
    Complete visitor implementation for minipython grammar
    Generates DOT format visualization with color-coded nodes
    """
    
    def __init__(self):
        self.node_count = 0
        self.dot_lines = ['digraph AST {']
        self.dot_lines.append('  rankdir=TB;')
        self.dot_lines.append('  node [shape=box, style="rounded,filled", fontname="Courier"];')
        self.dot_lines.append('  edge [fontname="Courier", fontsize=10];')
        
        # Color scheme
        self.colors = {
            'control': 'lightblue',
            'loop': 'lightgreen',
            'assignment': 'lightyellow',
            'expression': 'lightgray',
            'operator': 'lightcoral',
            'atom': 'lightcyan',
            'function': 'plum'
        }
    
    def get_node_id(self):
        """Generate unique node ID"""
        node_id = f"n{self.node_count}"
        self.node_count += 1
        return node_id
    
    def add_node(self, node_id, label, color='white'):
        """Add a node to the DOT graph"""
        escaped_label = label.replace('"', '\\"').replace('\n', '\\n')
        self.dot_lines.append(f'  {node_id} [label="{escaped_label}", fillcolor="{color}"];')
    
    def add_edge(self, parent_id, child_id, label=None):
        """Add an edge to the DOT graph"""
        if label:
            escaped_label = label.replace('"', '\\"')
            self.dot_lines.append(f'  {parent_id} -> {child_id} [label="{escaped_label}"];')
        else:
            self.dot_lines.append(f'  {parent_id} -> {child_id};')
    
    def get_dot(self):
        """Return complete DOT representation"""
        return '\n'.join(self.dot_lines + ['}'])
    
    # =========================================================================
    # PROGRAM STRUCTURE
    # =========================================================================
    
    def visitProg(self, ctx):
        """Visit program root"""
        node_id = self.get_node_id()
        self.add_node(node_id, "PROGRAM", self.colors['control'])
        
        if ctx.block():
            child_id = self.visit(ctx.block())
            self.add_edge(node_id, child_id)
        
        return node_id
    
    def visitBlock(self, ctx):
        """Visit block of statements"""
        node_id = self.get_node_id()
        self.add_node(node_id, "BLOCK", self.colors['control'])
        
        statements = ctx.statement()
        for i, stmt_ctx in enumerate(statements):
            child_id = self.visit(stmt_ctx)
            self.add_edge(node_id, child_id, f"stmt{i}")
        
        return node_id
    
    def visitStatement(self, ctx):
        """Visit statement - dispatch to specific type"""
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.compound_assignment():
            return self.visit(ctx.compound_assignment())
        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.while_loop():
            return self.visit(ctx.while_loop())
        elif ctx.for_loop():
            return self.visit(ctx.for_loop())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        elif ctx.expr():
            return self.visit(ctx.expr())
        
        node_id = self.get_node_id()
        self.add_node(node_id, "statement", self.colors['expression'])
        return node_id
    
    # =========================================================================
    # ASSIGNMENTS
    # =========================================================================
    
    def visitAssignment(self, ctx):
        """Visit assignment: ID = expr"""
        node_id = self.get_node_id()
        self.add_node(node_id, "ASSIGN\\n=", self.colors['assignment'])
        
        # Target
        id_node = self.get_node_id()
        id_text = ctx.ID().getText()
        self.add_node(id_node, f"ID\\n{id_text}", self.colors['atom'])
        self.add_edge(node_id, id_node, "target")
        
        # Value
        if ctx.expr():
            expr_id = self.visit(ctx.expr())
            self.add_edge(node_id, expr_id, "value")
        
        return node_id
    
    def visitCompound_assignment(self, ctx):
        """Visit compound assignment: ID += expr"""
        node_id = self.get_node_id()
        op = ctx.COMPOUND_OP().getText()
        self.add_node(node_id, f"COMPOUND\\n{op}", self.colors['assignment'])
        
        # Target
        id_node = self.get_node_id()
        id_text = ctx.ID().getText()
        self.add_node(id_node, f"ID\\n{id_text}", self.colors['atom'])
        self.add_edge(node_id, id_node, "target")
        
        # Value
        if ctx.expr():
            expr_id = self.visit(ctx.expr())
            self.add_edge(node_id, expr_id, "value")
        
        return node_id
    
    # =========================================================================
    # CONTROL FLOW
    # =========================================================================
    
    def visitIf_stmt(self, ctx):
        """Visit if statement"""
        node_id = self.get_node_id()
        self.add_node(node_id, "IF", self.colors['control'])
        
        # Condition
        if ctx.expr():
            cond_id = self.visit(ctx.expr())
            self.add_edge(node_id, cond_id, "condition")
        
        # Then suite
        if ctx.suite():
            suite_id = self.visit(ctx.suite())
            self.add_edge(node_id, suite_id, "then")
        
        # Elif clauses
        elif_clauses = ctx.elif_clause()
        for i, elif_ctx in enumerate(elif_clauses):
            elif_id = self.visit(elif_ctx)
            self.add_edge(node_id, elif_id, f"elif{i}")
        
        # Else clause
        if ctx.else_clause():
            else_id = self.visit(ctx.else_clause())
            self.add_edge(node_id, else_id, "else")
        
        return node_id
    
    def visitElif_clause(self, ctx):
        """Visit elif clause"""
        node_id = self.get_node_id()
        self.add_node(node_id, "ELIF", self.colors['control'])
        
        if ctx.expr():
            cond_id = self.visit(ctx.expr())
            self.add_edge(node_id, cond_id, "condition")
        
        if ctx.suite():
            suite_id = self.visit(ctx.suite())
            self.add_edge(node_id, suite_id, "then")
        
        return node_id
    
    def visitElse_clause(self, ctx):
        """Visit else clause"""
        node_id = self.get_node_id()
        self.add_node(node_id, "ELSE", self.colors['control'])
        
        if ctx.suite():
            suite_id = self.visit(ctx.suite())
            self.add_edge(node_id, suite_id, "body")
        
        return node_id
    
    # =========================================================================
    # LOOPS
    # =========================================================================
    
    def visitWhile_loop(self, ctx):
        """Visit while loop"""
        node_id = self.get_node_id()
        self.add_node(node_id, "WHILE", self.colors['loop'])
        
        if ctx.expr():
            cond_id = self.visit(ctx.expr())
            self.add_edge(node_id, cond_id, "condition")
        
        if ctx.suite():
            suite_id = self.visit(ctx.suite())
            self.add_edge(node_id, suite_id, "body")
        
        return node_id
    
    def visitFor_loop(self, ctx):
        """Visit for loop"""
        node_id = self.get_node_id()
        self.add_node(node_id, "FOR", self.colors['loop'])
        
        # Loop variable
        id_node = self.get_node_id()
        id_text = ctx.ID().getText()
        self.add_node(id_node, f"ID\\n{id_text}", self.colors['atom'])
        self.add_edge(node_id, id_node, "var")
        
        # Iterable
        if ctx.expr():
            iter_id = self.visit(ctx.expr())
            self.add_edge(node_id, iter_id, "iterable")
        elif ctx.func_call():
            iter_id = self.visit(ctx.func_call())
            self.add_edge(node_id, iter_id, "iterable")
        
        # Body
        if ctx.suite():
            suite_id = self.visit(ctx.suite())
            self.add_edge(node_id, suite_id, "body")
        
        return node_id
    
    # =========================================================================
    # FUNCTION CALLS
    # =========================================================================
    
    def visitFunc_call(self, ctx):
        """Visit function call"""
        node_id = self.get_node_id()
        func_name = ctx.ID().getText()
        self.add_node(node_id, f"CALL\\n{func_name}()", self.colors['function'])
        
        # Arguments
        exprs = ctx.expr()
        for i, expr_ctx in enumerate(exprs):
            arg_id = self.visit(expr_ctx)
            self.add_edge(node_id, arg_id, f"arg{i}")
        
        return node_id
    
    # =========================================================================
    # SUITE
    # =========================================================================
    
    def visitSuite(self, ctx):
        """Visit suite (indented block)"""
        node_id = self.get_node_id()
        self.add_node(node_id, "SUITE", self.colors['control'])
        
        if ctx.block():
            block_id = self.visit(ctx.block())
            self.add_edge(node_id, block_id)
        
        return node_id
    
    # =========================================================================
    # EXPRESSIONS
    # =========================================================================
    
    def visitExpr(self, ctx):
        """Visit expression"""
        node_id = self.get_node_id()
        child_count = ctx.getChildCount()
        
        # Binary operations
        if child_count >= 3 and ctx.expr(0) and ctx.expr(1):
            op_text = ctx.getChild(1).getText()
            
            if op_text in ['and', 'or']:
                self.add_node(node_id, f"LOGICAL\\n{op_text}", self.colors['operator'])
            elif op_text in ['==', '!=', '<', '<=', '>', '>=']:
                self.add_node(node_id, f"COMPARE\\n{op_text}", self.colors['operator'])
            else:
                self.add_node(node_id, f"BINOP\\n{op_text}", self.colors['operator'])
            
            left_id = self.visit(ctx.expr(0))
            self.add_edge(node_id, left_id, "left")
            
            right_id = self.visit(ctx.expr(1))
            self.add_edge(node_id, right_id, "right")
        
        # Unary NOT
        elif child_count == 2 and ctx.NOT():
            self.add_node(node_id, "UNARY\\nnot", self.colors['operator'])
            expr_id = self.visit(ctx.expr(0))
            self.add_edge(node_id, expr_id, "operand")
        
        # Parenthesized
        elif child_count == 3 and ctx.LPAREN() and ctx.RPAREN() and not ctx.COMMA():
            self.add_node(node_id, "PARENS", self.colors['expression'])
            expr_id = self.visit(ctx.expr(0))
            self.add_edge(node_id, expr_id)
        
        # Tuple
        elif ctx.LPAREN() and ctx.COMMA():
            self.add_node(node_id, "TUPLE", self.colors['expression'])
            exprs = ctx.expr()
            for i, expr_ctx in enumerate(exprs):
                elem_id = self.visit(expr_ctx)
                self.add_edge(node_id, elem_id, f"elem{i}")
        
        # List
        elif ctx.LBRACKET():
            self.add_node(node_id, "LIST", self.colors['expression'])
            exprs = ctx.expr()
            for i, expr_ctx in enumerate(exprs):
                elem_id = self.visit(expr_ctx)
                self.add_edge(node_id, elem_id, f"elem{i}")
        
        # Dictionary
        elif ctx.LBRACE():
            self.add_node(node_id, "DICT", self.colors['expression'])
            exprs = ctx.expr()
            for i in range(0, len(exprs), 2):
                if i + 1 < len(exprs):
                    key_id = self.visit(exprs[i])
                    val_id = self.visit(exprs[i + 1])
                    
                    pair_node = self.get_node_id()
                    self.add_node(pair_node, f"PAIR{i//2}", self.colors['expression'])
                    self.add_edge(node_id, pair_node)
                    self.add_edge(pair_node, key_id, "key")
                    self.add_edge(pair_node, val_id, "value")
        
        # Atom
        elif ctx.atom():
            return self.visit(ctx.atom())
        
        else:
            self.add_node(node_id, "EXPR", self.colors['expression'])
        
        return node_id
    
    def visitAtom(self, ctx):
        """Visit atomic value"""
        node_id = self.get_node_id()
        
        if ctx.NUMBER():
            value = ctx.NUMBER().getText()
            self.add_node(node_id, f"NUMBER\\n{value}", self.colors['atom'])
        elif ctx.ID():
            value = ctx.ID().getText()
            self.add_node(node_id, f"ID\\n{value}", self.colors['atom'])
        elif ctx.STRING():
            value = ctx.STRING().getText()
            if len(value) > 20:
                value = value[:17] + "..."
            self.add_node(node_id, f"STRING\\n{value}", self.colors['atom'])
        elif ctx.BOOL():
            value = ctx.BOOL().getText()
            self.add_node(node_id, f"BOOL\\n{value}", self.colors['atom'])
        else:
            self.add_node(node_id, "ATOM", self.colors['atom'])
        
        return node_id


def parse_and_visualize(input_file, output_path=None):
    """Parse input file and generate AST visualizations"""
    
    # Read input
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)
    
    with open(input_path, 'r') as f:
        input_text = f.read()
    
    # Determine output directory and base name
    if output_path:
        output_dir = Path(output_path)
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)
        # Use input filename stem as the base filename inside the directory
        base_name = input_path.stem
        output_base = str(output_dir / base_name)
    else:
        # Default: current directory, use input filename stem
        output_base = input_path.stem
    
    print(f"Parsing: {input_file}")
    print(f"Output directory: {output_path if output_path else '.'}")
    print(f"Output files: {Path(output_base).name}.*")
    print(f"Size: {len(input_text)} characters")
    print("-" * 60)
    
    try:
        # Create lexer
        input_stream = InputStream(input_text)
        lexer = IndentLexer(input_stream)
        
        # Create token stream
        token_stream = CommonTokenStream(lexer)
        
        # Create parser
        parser = minipythonParser(token_stream)
        
        # Parse
        tree = parser.prog()
        
        # Create visualizer
        visualizer = ASTVisualizer()
        visualizer.visit(tree)
        
        # Generate DOT
        dot_output = visualizer.get_dot()
        
        # Write DOT file
        dot_file = f"{output_base}.dot"
        with open(dot_file, 'w') as f:
            f.write(dot_output)
        print(f"✓ Generated: {dot_file}")
        
        # Generate images with Graphviz
        formats = [
            ('png', 'PNG image'),
            ('svg', 'SVG image'),
            ('pdf', 'PDF document')
        ]
        
        for fmt, desc in formats:
            output_file = f"{output_base}.{fmt}"
            try:
                subprocess.run(
                    ['dot', f'-T{fmt}', dot_file, '-o', output_file],
                    check=True,
                    capture_output=True
                )
                print(f"✓ Generated: {output_file} ({desc})")
            except subprocess.CalledProcessError as e:
                print(f"✗ Failed to generate {fmt}: {e.stderr.decode()}")
            except FileNotFoundError:
                print(f"✗ Graphviz 'dot' command not found. Install with: apt-get install graphviz")
                break
        
        print("-" * 60)
        print("AST visualization complete!")
        print(f"\nNodes: {visualizer.node_count}")
        
    except Exception as e:
        print(f"Error during parsing: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Generate AST visualization for minipython code',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python astvisualizer.py test_code.py
    → test_code.{dot,png,svg,pdf} in current directory
  
  python astvisualizer.py test_code.py -o output/asts/ast_pd1
    → output/asts/ast_pd1/test_code.{dot,png,svg,pdf}
  
  python astvisualizer.py ../tests/my_test.py -o results
    → results/my_test.{dot,png,svg,pdf}

The -o option specifies the output DIRECTORY.
Files are named after the input file (without .py extension).
        """
    )
    
    parser.add_argument(
        'input_file',
        help='Input minipython file to parse'
    )
    
    parser.add_argument(
        '-o', '--output',
        dest='output_path',
        help='Output directory. Files named <input_stem>.{dot,png,svg,pdf}. Default: current directory',
        default=None
    )
    
    args = parser.parse_args()
    
    parse_and_visualize(args.input_file, args.output_path)


if __name__ == "__main__":
    main()