import sys
import os
from mistake.tokenizer.lexer import Lexer
from mistake.parser.parser import Parser
from mistake.runtime.interpreter import Interpreter
import time
from typing import Tuple, List
from dotenv import load_dotenv

ENV_PATH = None

def print_help():
    print("Usage: mistake-lang <filename> [--time] [--tokens] [--ast] [--no-exe] [--env <path>] [--vulkan]")

def get_args() -> Tuple[str, List[str]]:
    if "--help" in sys.argv:
        print_help()
        sys.exit(0)
    
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f"File '{sys.argv[1]}' not found")
        sys.exit(1)

    return sys.argv[1], sys.argv[2:]

def run_script(program: str, lex=Lexer(),parser=Parser(),rt=Interpreter(),standalone=True) -> List:
    tokens = lex.tokenize(program)
    ast = parser.parse(tokens)
    return rt.execute(ast, standalone=standalone)

def main():
    global ENV_PATH
    fname, args = get_args()
    p_time = "--time" in args

    lexer = Lexer()
    parser = Parser()
    runtime = Interpreter("--unsafe" in args)

    get_env =  args.index("--env") if "--env" in args else -1
    ENV_PATH = None if get_env == -1 else args[get_env + 1] 
    if ENV_PATH is not None: load_dotenv(ENV_PATH)
    else: load_dotenv()
    
    with open(fname, "r", encoding='utf-8') as f:
        if p_time:
            print("Read file:", time.process_time())
        start = time.time()

        os.chdir(os.path.dirname(os.path.abspath(fname)))
        code = f.read()

        tokens = lexer.tokenize(code)
        if p_time:
            print("Tokenized:", time.process_time())

        if "--tokens" in args:
            print(tokens)

        ast = parser.parse(tokens)
        if p_time:
            print("Parsed:", time.process_time())

        if "--ast" in args:
            open("ast.txt", "w").write(str(ast))
            print(ast)

        if "--no-exe" not in args:
            runtime.execute(ast, filename=fname)

        if p_time:
            print(f"Total runtime: {time.time() - start} seconds")


if __name__ == "__main__":
    main()
