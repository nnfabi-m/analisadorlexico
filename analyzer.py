#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analisador (front-end) de uma DSL simples.

Regras aceitas (uma instrução por linha, terminar com ';'):
  1) let <ident> = <numero>;
  2) print "<texto>";
  3) move <north|south|east|west> steps <inteiro>;

Linhas em branco e comentários iniciados por '#' são ignorados.
Em caso de erro, exibe a linha e o motivo e sai com código != 0.
Em caso de sucesso, imprime uma mensagem de sucesso e sai com código 0.
"""
import re
import sys
from dataclasses import dataclass

# Compila regexes
IDENT = r"[a-zA-Z_][a-zA-Z0-9_]*"
NUMBER = r"-?\d+(?:\.\d+)?"

RULES = [
    (re.compile(rf"^\s*let\s+{IDENT}\s*=\s*{NUMBER}\s*;\s*$", re.IGNORECASE), "DECLARAÇÃO 'let'"),
    (re.compile(r"^\s*print\s+\"[^\"\n]*\"\s*;\s*$", re.IGNORECASE), "COMANDO 'print'"),
    (re.compile(r"^\s*move\s+(north|south|east|west)\s+steps\s+\d+\s*;\s*$", re.IGNORECASE), "COMANDO 'move'"),
]

@dataclass
class Result:
    ok: bool
    message: str
    errors: list

def validate_line(line: str) -> bool:
    for pattern, _desc in RULES:
        if pattern.match(line):
            return True
    return False

def analyze_script(text: str) -> Result:
    errors = []
    valid_count = 0
    lines = text.splitlines()
    for idx, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        # Ignora vazias e comentários
        if not line.strip() or line.strip().startswith('#'):
            continue
        if validate_line(line):
            valid_count += 1
        else:
            errors.append((idx, line))
    if errors:
        first = errors[0]
        msg = f"ERRO na linha {first[0]}: instrução inválida ou ponto e vírgula ausente. → '{first[1]}'"
        return Result(False, msg, errors)
    return Result(True, f"SUCESSO: script válido ({valid_count} instruções válidas).", [])

def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv:
        print("Uso: python analyzer.py <caminho/do/script.txt>")
        sys.exit(2)
    path = argv[0]
    try:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"ERRO: arquivo não encontrado: {path}")
        sys.exit(2)
    res = analyze_script(text)
    if res.ok:
        print(res.message)
        sys.exit(0)
    else:
        print(res.message)
        # Se desejar, imprime todos os erros encontrados (opcional)
        # for ln, content in res.errors:
        #     print(f"  Linha {ln}: {content}")
        sys.exit(1)

if __name__ == "__main__":
    main()
