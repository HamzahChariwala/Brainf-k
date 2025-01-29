import bf_interpreter.brainfuck as brainfuck

with open("brainf--k_code.bf", "r", encoding="utf-8") as f:
    sourcecode = f.read()

brainfuck.evaluate(sourcecode)
