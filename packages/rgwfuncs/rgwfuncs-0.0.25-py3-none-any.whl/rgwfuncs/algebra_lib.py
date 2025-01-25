import re
import math
from sympy import symbols, latex, simplify, solve, diff, Expr
from sympy.parsing.sympy_parser import parse_expr
from typing import Tuple, List, Dict, Optional

def compute_algebraic_expression(expression: str) -> float:
    try:
        # Direct numerical evaluation
        # Safely evaluate the expression using the math module
        numeric_result = eval(expression, {"__builtins__": None, "math": math})

        # Convert to float if possible
        return float(numeric_result)
    except Exception as e:
        raise ValueError(f"Error computing expression: {e}")

def simplify_algebraic_expression(expression: str) -> str:


    def recursive_parse_function_call(func_call: str, prefix: str, sym_vars: Dict[str, Expr]) -> Tuple[str, List[Expr]]:
        # print(f"Parsing function call: {func_call}")

        # Match the function name and arguments
        match = re.match(fr'{prefix}\.(\w+)\((.*)\)', func_call, re.DOTALL)
        if not match:
            raise ValueError(f"Invalid function call: {func_call}")

        func_name = match.group(1)
        args_str = match.group(2)

        # Check if it's a list for np
        if prefix == 'np' and args_str.startswith("[") and args_str.endswith("]"):
            parsed_args = [ast.literal_eval(args_str.strip())]
        else:
            parsed_args = []
            raw_args = re.split(r',(?![^{]*\})', args_str)
            for arg in raw_args:
                arg = arg.strip()
                if re.match(r'\w+\.\w+\(', arg):
                    # Recursively evaluate the argument if it's another function call
                    arg_val = recursive_eval_func(re.match(r'\w+\.\w+\(.*\)', arg), sym_vars)
                    parsed_args.append(parse_expr(arg_val, local_dict=sym_vars))
                else:
                    parsed_args.append(parse_expr(arg, local_dict=sym_vars))

        # print(f"Function name: {func_name}, Parsed arguments: {parsed_args}")
        return func_name, parsed_args


    def recursive_eval_func(match: re.Match, sym_vars: Dict[str, Expr]) -> str:
        # print("152", match)
        func_call = match.group(0)
        # print(f"153 Evaluating function call: {func_call}")

        if func_call.startswith("np."):
            func_name, args = recursive_parse_function_call(func_call, 'np', sym_vars)
            if func_name == 'diff':
                expr = args[0]
                if isinstance(expr, list):
                    # Calculate discrete difference
                    diff_result = [expr[i] - expr[i - 1] for i in range(1, len(expr))]
                    return str(diff_result)
                # Perform symbolic differentiation
                diff_result = diff(expr)
                return str(diff_result)

        if func_call.startswith("math."):
            func_name, args = recursive_parse_function_call(func_call, 'math', sym_vars)
            if hasattr(math, func_name):
                result = getattr(math, func_name)(*args)
                return str(result)

        if func_call.startswith("sym."):
            initial_method_match = re.match(r'(sym\.\w+\([^()]*\))(\.(\w+)\((.*?)\))*', func_call, re.DOTALL)
            if initial_method_match:
                base_expr_str = initial_method_match.group(1)
                base_func_name, base_args = recursive_parse_function_call(base_expr_str, 'sym', sym_vars)
                if base_func_name == 'solve':
                    solutions = solve(base_args[0], base_args[1])
                    # print(f"Solutions found: {solutions}")

                method_chain = re.findall(r'\.(\w+)\((.*?)\)', func_call, re.DOTALL)
                final_solutions = [execute_chained_methods(sol, [(m, [method_args.strip()]) for m, method_args in method_chain], sym_vars) for sol in solutions]

                return "[" + ",".join(latex(simplify(sol)) for sol in final_solutions) + "]"

        raise ValueError(f"Unknown function call: {func_call}")

    def execute_chained_methods(sym_expr: Expr, method_chain: List[Tuple[str, List[str]]], sym_vars: Dict[str, Expr]) -> Expr:
        for method_name, method_args in method_chain:
            # print(f"Executing method: {method_name} with arguments: {method_args}")
            method = getattr(sym_expr, method_name, None)
            if method:
                if method_name == 'subs' and isinstance(method_args[0], dict):
                    kwargs = method_args[0]
                    kwargs = {parse_expr(k, local_dict=sym_vars): parse_expr(v, local_dict=sym_vars) for k, v in kwargs.items()}
                    sym_expr = method(kwargs)
                else:
                    args = [parse_expr(arg.strip(), local_dict=sym_vars) for arg in method_args]
                    sym_expr = method(*args)
            # print(f"Result after {method_name}: {sym_expr}")
        return sym_expr



    variable_names = set(re.findall(r'\b[a-zA-Z]\w*\b', expression))
    sym_vars = {var: symbols(var) for var in variable_names}

    patterns = {
        #"numpy_diff_brackets": r"np\.diff\(\[.*?\]\)",
        "numpy_diff_no_brackets": r"np\.diff\([^()]*\)",
        "math_functions": r"math\.\w+\((?:[^()]*(?:\([^()]*\)[^()]*)*)\)",
        # "sympy_functions": r"sym\.\w+\([^()]*\)(?:\.\w+\([^()]*\))?",
    }

    function_pattern = '|'.join(patterns.values())

    # Use a lambda function to pass additional arguments
    processed_expression = re.sub(function_pattern, lambda match: recursive_eval_func(match, sym_vars), expression)
    # print("Level 2 processed_expression:", processed_expression)

    try:
        if processed_expression.startswith('[') and processed_expression.endswith(']'):
            return processed_expression

        expr = parse_expr(processed_expression, local_dict=sym_vars)
        final_result = simplify(expr)

        if final_result.free_symbols:
            latex_result = latex(final_result)
            return latex_result
        else:
            return str(final_result)

    except Exception as e:
        raise ValueError(f"Error simplifying expression: {e}")

def solve_algebraic_expression(expression: str, variable: str, subs: Optional[Dict[str, float]] = None) -> str:
    try:
        # Create symbols for the variables in the expression
        variable_symbols = set(re.findall(r'\b[a-zA-Z]\w*\b', expression))
        sym_vars = {var: symbols(var) for var in variable_symbols}

        # Parse the expression and solve it
        expr = parse_expr(expression, local_dict=sym_vars)
        var_symbol = symbols(variable)
        solutions = solve(expr, var_symbol)

        # Apply substitutions if provided
        if subs:
            subs_symbols = {symbols(k): v for k, v in subs.items()}
            solutions = [simplify(sol.subs(subs_symbols)) for sol in solutions]

        # Convert solutions to LaTeX strings if possible
        latex_solutions = [latex(simplify(sol)) if sol.free_symbols else str(sol) for sol in solutions]
        result = r"\left[" + ", ".join(latex_solutions) + r"\right]"
        print("158", result)
        return result

    except Exception as e:
        raise ValueError(f"Error solving the expression: {e}")



def get_prime_factors_latex(n: int) -> str:
    """
    Return the prime factors of a number as a LaTeX expression.
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)

    factor_counts = {factor: factors.count(factor) for factor in set(factors)}
    latex_factors = [f"{factor}^{{{count}}}" if count > 1 else str(factor) for factor, count in factor_counts.items()]
    return " \\cdot ".join(latex_factors)



