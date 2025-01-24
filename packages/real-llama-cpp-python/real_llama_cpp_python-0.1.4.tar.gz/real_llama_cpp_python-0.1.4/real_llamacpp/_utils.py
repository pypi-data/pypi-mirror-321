import re

def strip_echo(echo:bool, prompt: str, output: str) -> str:
    if echo:
        return output[len(prompt):].strip()
    return output
    
