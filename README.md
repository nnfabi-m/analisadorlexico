# analisadorlexico
# Protótipo do Analisador da DSL (Front‑end)

Este é um **protótipo funcional** do analisador (front‑end) de uma DSL simples.  
O programa lê um script (arquivo `.txt`), **valida** linha a linha e **indica sucesso ou erro**.

## Gramática mínima aceita
Uma instrução por linha, sempre terminando com `;`:

1. **Declaração**: `let <ident> = <numero>;`  
   Ex.: `let vida = 100;` ou `let velocidade_max = -3.5;`

2. **Impressão**: `print "<texto>";`  
   Ex.: `print "iniciando...";`

3. **Movimento**: `move <north|south|east|west> steps <inteiro>;`  
   Ex.: `move north steps 10;`

Linhas em branco e comentários iniciados por `#` são **ignorados**.

---

## Requisitos
- Python **3.10+** (sem dependências externas).

## Como executar
Clone o repositório e rode o analisador passando o caminho do arquivo de script:

```bash
python analyzer.py teste_sucesso.txt
python analyzer.py teste_falha.txt
```

**Saídas esperadas:**
- Para `teste_sucesso.txt`: algo como `SUCESSO: script válido (N instruções válidas).`
- Para `teste_falha.txt`: mensagem `ERRO na linha X: ...`

> Dica: em Windows, use `py analyzer.py teste_sucesso.txt` se `python` não estiver mapeado.

## Estrutura do projeto
```text
analyzer.py
README.md
teste_sucesso.txt
teste_falha.txt
```

## Link do repositório (substitua pelo seu)
(https://github.com/nnfabi-m/analisadorlexico)


## Testes rápidos
```bash
# Saída de sucesso
python analyzer.py teste_sucesso.txt

# Saída de erro (retorno de processo != 0)
python analyzer.py teste_falha.txt && echo OK || echo FALHOU COMO ESPERADO
```

## Observações
- O protótipo não executa o script; apenas **valida a sintaxe**.
- Para expansão (futuro): validar tipos, tabela de símbolos, condições, etc.
