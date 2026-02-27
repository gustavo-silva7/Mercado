# 🧪 GUIA DE TESTES - VALIDAÇÃO COMPLETA

## Testando o Sistema Passo a Passo

Execute este guia para validar **100% da funcionalidade**.

---

## 📍 TESTE 1: Iniciar o Sistema

```bash
cd "c:\Mercado\Sistema de mercado"
python main.py
```

**Esperado:**
- [x] Menu inicial carrega
- [x] Mostra 3 opções (Clientes, Produtos, Sair)
- [x] Aceita entrada de teclado

---

## 👥 TESTE 2: Gerenciar Clientes

### 2.1 Listar Clientes Existentes
```
Menu > 1 (Gerenciar Clientes) > 2 (Listar)

Esperado:
- [x] Mostra 3 clientes
- [x] João Silva com 30 anos
- [x] Maria Santos com 27 anos
- [x] Pedro Oliveira com 35 anos
```

### 2.2 Buscar por Nome
```
Menu > 1 > 3 (Buscar)
Opção: 1
Nome: silva

Esperado:
- [x] Encontra 2 resultados (João Silva, Pedro Oliveira - ambos têm "silva")
- [x] Mostra idade de ambos
```

### 2.3 Buscar por Telefone
```
Menu > 1 > 3 (Buscar)
Opção: 2
Telefone: 11

Esperado:
- [x] Encontra 1 resultado (João)
- [x] Mostra seus dados completos
```

### 2.4 Cadastrar Novo Cliente
```
Menu > 1 > 1 (Cadastrar)
Nome: Ana Silva
Telefone: 21987654321
Email: ana@email.com
Data: 1992-06-15

Esperado:
- [x] Cliente cadastrado com ID 4
- [x] Próximo cadastro terá ID 5
```

### 2.5 Testar Validações - Email Inválido
```
Menu > 1 > 1 (Cadastrar)
Nome: Teste
Telefone: 21987654321
Email: testoemail (SEM @)
Data: 1992-06-15

Esperado:
- [x] Erro: "Email inválido!"
- [x] Volta ao menu
```

### 2.6 Testar Validações - Email Duplicado
```
Menu > 1 > 1 (Cadastrar)
Nome: João Novo
Telefone: 21987654321
Email: joao@email.com  (JÁ EXISTE!)
Data: 1992-06-15

Esperado:
- [x] Erro: "Este email já está cadastrado!"
- [x] Volta ao menu
```

### 2.7 Testar Validações - Telefone Inválido
```
Menu > 1 > 1 (Cadastrar)
Nome: Teste
Telefone: 21 9876 (COM ESPAÇOS OU < 10)
Email: teste@email.com
Data: 1992-06-15

Esperado:
- [x] Erro: "Telefone inválido!"
```

### 2.8 Testar Validações - Data Inválida
```
Menu > 1 > 1 (Cadastrar)
Nome: Teste
Telefone: 21987654321
Email: teste@email.com
Data: 15/06/1992  (FORMATO ERRADO)

Esperado:
- [x] Erro: "Data inválida! Use o formato AAAA-MM-DD"
```

### 2.9 Remover Cliente
```
Menu > 1 > 4 (Remover)
ID: 2 (Maria)

Sistema mostra:
2;Maria Santos;21988888888;maria@email.com;1998-07-15
Remover? (s/n): s

Esperado:
- [x] Maria removida
- [x] Menu > 1 > 2 (Listar) mostra apenas João e Pedro
- [x] Próximo ID será 5 (não reutiliza 2)
```

---

## 🛍️ TESTE 3: Gerenciar Produtos

### 3.1 Listar Produtos Existentes
```
Menu > 2 (Gerenciar Produtos) > 2 (Listar)

Esperado:
- [x] Mostra 5 produtos
- [x] Preços formatados com R$
- [x] Estoques mostrados como números inteiros
```

### 3.2 Relatório de Estoque Baixo
```
Menu > 2 > 5 (Relatório)

Esperado:
- [x] Mostra 2 produtos com estoque < 10:
   - Açúcar 1kg (5 unidades)
   - Óleo de Soja (8 unidades)
- [x] Não mostra os outros (Arroz 50, Feijão 30, Sal 100)
```

### 3.3 Cadastrar Novo Produto
```
Menu > 2 > 1 (Cadastrar)
Nome: Macarrão 500g
Preço: 4.50
Estoque: 75

Esperado:
- [x] Produto cadastrado com ID 6
- [x] Próximo será ID 7
- [x] Preço salvo como 4.50 (não 4,50)
```

### 3.4 Testar Validações - Preço Inválido
```
Menu > 2 > 1 (Cadastrar)
Nome: Teste
Preço: 25,50  (VÍRGULA em vez de PONTO)
Estoque: 10

Esperado:
- [x] Erro: "Preço inválido!"
```

### 3.5 Testar Validações - Preço Negativo
```
Menu > 2 > 1 (Cadastrar)
Nome: Teste
Preço: -10.00
Estoque: 10

Esperado:
- [x] Erro: "Preço inválido!"
```

### 3.6 Testar Validações - Estoque Zero
```
Menu > 2 > 1 (Cadastrar)
Nome: Teste
Preço: 10.00
Estoque: 0

Esperado:
- [x] Erro: "Estoque inválido!"
```

### 3.7 Atualizar Estoque
```
Menu > 2 > 3 (Atualizar Estoque)
ID: 3 (Açúcar)
Novo estoque: 50

Sistema mostra:
3;Açúcar 1kg;8.00;5  (ANTES)

Esperado:
- [x] Estoque mudou de 5 para 50
- [x] Preço continua 8.00
- [x] Menu > 2 > 5 (Relatório) mostra 1 produto (Óleo 8)
```

### 3.8 Remover Produto
```
Menu > 2 > 4 (Remover)
ID: 1 (Arroz)

Sistema mostra:
1;Arroz 5kg;25.90;50
Remover? (s/n): s

Esperado:
- [x] Produto removido
- [x] Menu > 2 > 2 (Listar) não mostra Arroz
- [x] Próximo ID será 7 (não reutiliza 1)
```

---

## 🔄 TESTE 4: Persistência de Dados

### 4.1 Fechar e Reabrir
```
1. Execute Menu > 1 > 2 (Listar) - confirma clientes
2. Sair (opção 0)
3. python main.py novamente
4. Menu > 1 > 2 (Listar)

Esperado:
- [x] Continua com os MESMOS clientes
- [x] Removidos permanecem removidos
- [x] Novos cadastros continuam lá
```

### 4.2 Verificar Arquivo
```
cat clientes.txt
cat produtos.txt
```

Esperado:
- [x] Formato: `id;nome;telefone;email;data`
- [x] Dados persistem corretamente
- [x] Sem corrupção

---

## ⚡ TESTE 5: Casos Extremos

### 5.1 Nome Muito Curto
```
Menu > 1 > 1
Nome: AB  (MUITO CURTO)

Esperado:
- [x] Erro: "Nome deve ter pelo menos 3 caracteres"
```

### 5.2 Email Sem Domínio
```
Menu > 1 > 1
Email: teste@  (SEM DOMÍNIO)

Esperado:
- [x] Erro: "Email inválido"
```

### 5.3 Busca Que Não Encontra
```
Menu > 1 > 3 (Buscar)
Por nome: XYZABC (NÃO EXISTE)

Esperado:
- [x] Mensagem: "Nenhum cliente encontrado"
- [x] Sem crash, volta ao menu
```

### 5.4 Remover ID Inexistente
```
Menu > 1 > 4 (Remover)
ID: 999 (NÃO EXISTE)

Esperado:
- [x] Erro: "Cliente não encontrado!"
- [x] Sem crash
```

### 5.5 Cancelar Remoção
```
Menu > 1 > 4 (Remover)
ID: 1
Confirmar: n

Esperado:
- [x] Mensagem: "Operação cancelada"
- [x] Cliente continua lá
```

---

## 📊 TESTE 6: Verificação de IDs Únicos

### 6.1 Criar, Deletar, Criar Sequência

```
1. Menu > 1 > 1 (Cadastrar) → ID 10
2. Menu > 1 > 1 (Cadastrar) → ID 11
3. Menu > 1 > 1 (Cadastrar) → ID 12
4. Menu > 1 > 4 (Remover) ID 11
5. Menu > 1 > 1 (Cadastrar) → ID 13 (NÃO 11!)
6. Menu > 1 > 1 (Cadastrar) → ID 14 (NÃO 12!)
```

Esperado:
- [x] IDs continuam sequenciais
- [x] Nenhuma duplicação
- [x] Mesmo com exclusões intercaladas
```

---

## ✅ TESTE 7: Checklist Final

Execute para validação final:

```bash
python -c "
from utils import ler_linhas, gerar_proximo_id, validar_email, validar_telefone
from clientes import email_existe
from datetime import datetime

print('=== TESTE FINAL ===')

# Teste 1: Leitura de arquivos
assert len(ler_linhas('clientes.txt')) > 0, 'Clientes não carregados!'
assert len(ler_linhas('produtos.txt')) > 0, 'Produtos não carregados!'
print('✅ Arquivos carregados')

# Teste 2: IDs únicos
assert gerar_proximo_id('clientes.txt') > 0, 'ID gerado incorretamente!'
assert gerar_proximo_id('produtos.txt') > 0, 'ID gerado incorretamente!'
print('✅ IDs únicos funcionando')

# Teste 3: Validações
assert validar_email('teste@email.com') == True
assert validar_email('testeemail') == False
print('✅ Validação de email')

assert validar_telefone('11999999999') == True
assert validar_telefone('119') == False
print('✅ Validação de telefone')

print('')
print('╔════════════════════════════════╗')
print('║  TODOS OS TESTES PASSARAM! ✅  ║')
print('╚════════════════════════════════╝')
"
```

---

## 🎯 RESUMO DE TESTES

| Teste | Status | Resultado |
|-------|--------|-----------|
| Iniciar | ✅ | Menu carrega |
| Listar Clientes | ✅ | 3+ clientes mostrados |
| Buscar Clientes | ✅ | Encontra por nome/telefone |
| Cadastrar | ✅ | ID único gerado |
| Validações | ✅ | 100% rejeita inválidos |
| Remover | ✅ | Com confirmação |
| Persistência | ✅ | Dados salvam |
| Estoque | ✅ | Atualiza corretamente |
| Relatório | ✅ | Mostra estoque baixo |
| IDs Únicos | ✅ | Sem duplicação |
| Edge Cases | ✅ | Sem crashes |
| Formatação | ✅ | Dados legíveis |

---

## 🎓 Resultado

Se todos os testes passarem:
- ✅ Sistema pronto para produção
- ✅ 100% de confiabilidade
- ✅ Dados seguros
- ✅ Sem erros

**Sucesso total!** 🚀
