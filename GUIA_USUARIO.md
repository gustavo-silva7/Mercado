# 👥 GUIA DO USUÁRIO - SISTEMA DE MERCADO

## 🎯 INÍCIO RÁPIDO

### Passo 1: Abra o Terminal
```
cd "c:\Mercado\Sistema de mercado"
python main.py
```

### Passo 2: Escolha uma opção
```
╔════════════════════════════════╗
║      MENU PRINCIPAL             ║
╠════════════════════════════════╣
║ 1 - Gerenciar Clientes          ║
║ 2 - Gerenciar Produtos          ║
║ 0 - Sair                        ║
╚════════════════════════════════╝
```

---

## 👥 GERENCIAR CLIENTES

### 1. CADASTRAR CLIENTE

**O que você precisa:**
- Nome completo (mínimo 3 caracteres)
- Telefone (10+ números)
- Email (único, não pode repetir)
- Data de nascimento (formato: AAAA-MM-DD)

**Exemplo:**
```
Nome: João Silva
Telefone: 11999999999
Email: joao@email.com
Data de nascimento: 1995-04-10
```

**Resultado:**
```
✅ Cliente cadastrado com sucesso! (ID: 1)
Pressione ENTER para continuar...
```

---

### 2. LISTAR CLIENTES

Mostra **todos** os clientes com:
- ID único
- Nome completo
- Telefone
- Email
- **Idade calculada automaticamente**

**Exemplo de saída:**
```
ID    Nome                      Telefone        Email                         Idade 
─────────────────────────────────────────────────────────────────────────────────
1     João Silva                11999999999     joao@email.com                30   
2     Maria Santos              21988888888     maria@email.com               27   
3     Pedro Oliveira            85987654321     pedro@email.com               35   
```

---

### 3. BUSCAR CLIENTE

Tem **2 opções:**

**Opção 1: Buscar por nome (parcial)**
```
Digite o nome (ou parte dele): silva
→ Mostra todos com "silva" no nome
```

**Opção 2: Buscar por telefone**
```
Digite o telefone: 119
→ Mostra todos com telefone começando com "119"
```

---

### 4. REMOVER CLIENTE

**Passo a passo:**
1. Sistema lista todos os clientes
2. Você digita o ID a remover
3. Sistema mostra os dados do cliente
4. Você confirma: `s` para sim, `n` para não
5. Pronto! Cliente excluído (ou cancelado)

**Exemplo:**
```
Digite o ID do cliente a remover: 2
⚠️ Confirmar remoção do cliente:
2;Maria Santos;21988888888;maria@email.com;1998-07-15
Remover? (s/n): s
✅ Cliente removido com sucesso!
```

---

## 🛍️ GERENCIAR PRODUTOS

### 1. CADASTRAR PRODUTO

**O que você precisa:**
- Nome do produto (mínimo 3 caracteres)
- Preço em reais (use `.` para decimal)
- Quantidade em estoque (número inteiro > 0)

**Exemplo:**
```
Nome: Arroz 5kg
Preço: 25.90
Estoque: 50
```

**Resultado:**
```
✅ Produto cadastrado com sucesso! (ID: 1)
```

---

### 2. LISTAR PRODUTOS

Mostra **todos** os produtos com:
- ID
- Nome
- Preço formatado em reais
- Quantidade em estoque

**Exemplo:**
```
ID    Nome                           Preço        Estoque     
──────────────────────────────────────────────────────────────
1     Arroz 5kg                      R$ 25.90     50          
2     Feijão Carioca                 R$ 12.50     30          
3     Açúcar 1kg                     R$ 8.00      5           
4     Sal Refinado                   R$ 3.50      100         
5     Óleo de Soja                   R$ 7.80      8           
```

---

### 3. ATUALIZAR ESTOQUE

Muda a quantidade sem perder o preço.

**Passo a passo:**
1. Sistema lista todos os produtos
2. Você digita o ID do produto
3. Sistema mostra dados atuais
4. Você digita **nova quantidade**
5. Pronto! Estoque atualizado

**Exemplo:**
```
Digite o ID do produto: 3
📦 Produto atual: 3;Açúcar 1kg;8.00;5
Novo estoque (quantidade): 15
✅ Estoque atualizado com sucesso!
```

**Resultado:**
- Preço continua 8.00 ✅
- Estoque muda de 5 para 15 ✅

---

### 4. REMOVER PRODUTO

Funciona igual ao remover cliente.

**Passo a passo:**
1. Sistema lista todos os produtos
2. Você digita o ID a remover
3. Sistema mostra os dados
4. Você confirma: `s` ou `n`
5. Pronto!

---

### 5. RELATÓRIO DE ESTOQUE BAIXO

Mostra **automaticamente** todos os produtos com **menos de 10 unidades**.

**Exemplo:**
```
⚠️  3 produto(s) com estoque baixo:

ID    Nome                           Preço        Estoque     
──────────────────────────────────────────────────────────────
3     Açúcar 1kg                     R$ 8.00      5           
5     Óleo de Soja                   R$ 7.80      8           
```

**Use para:**
- Saber o que precisa repor ✅
- Priorizar compras ✅
- Evitar falta de estoque ✅

---

## ⚠️ REGRAS IMPORTANTES

### Emails
- ❌ Não pode duplicar (um cliente por email)
- ✅ Formato: `nome@dominio.com`

### Telefone
- ✅ Apenas números
- ✅ Mínimo 10 dígitos
- ✅ Exemplos válidos: `11999999999`, `2188888888`

### Data de Nascimento
- ✅ Formato: `AAAA-MM-DD`
- ✅ Exemplos: `1995-04-10`, `2000-12-25`
- ✅ A idade é calculada automaticamente

### Preço
- ✅ Use ponto `.` para decimal
- ✅ Exemplos: `25.90`, `8.00`, `3.50`
- ✅ Não pode ser negativo ou zero

### Estoque
- ✅ Número inteiro
- ✅ Não pode ser zero ou negativo
- ✅ Exemplos: `50`, `100`, `8`

---

## 🔍 DICAS E TRUQUES

### Dica 1: Busca Parcial
```
Digite o nome (ou parte dele): silva
→ Encontra: Silva, silva, SILVA
→ Encontra em qualquer posição
```

### Dica 2: Busca por Telefone Incompleto
```
Digite o telefone: 11
→ Encontra todos com DDD 11
```

### Dica 3: IDs são Sequenciais
- Primeiro cliente/produto: ID 1
- Próximo: ID 2
- Mesmo se deletar um, o próximo novo será o próximo número
- Exemplo: Delete ID 2, próximo será ID 3 (não 2 novamente)

### Dica 4: Não há limite
- Cadastre quantos clientes e produtos quiser
- Sistema nunca bate limites

### Dica 5: Dados Persistem
- Feche o programa: dados salvos ✅
- Abra novamente: tudo continua lá ✅

---

## ❌ ERROS COMUNS

### Erro 1: "Email inválido!"
```
❌ Você digitou: joao.email.com (sem @)
✅ Correto: joao@email.com (com @)
```

### Erro 2: "Telefone inválido!"
```
❌ Você digitou: (11) 9999-9999 (com caracteres especiais)
✅ Correto: 11999999999 (apenas números)
```

### Erro 3: "Data inválida"
```
❌ Você digitou: 10/04/1995 (formato errado)
✅ Correto: 1995-04-10 (formato AAAA-MM-DD)
```

### Erro 4: "Preço inválido"
```
❌ Você digitou: 25,90 (vírgula)
✅ Correto: 25.90 (ponto)
```

### Erro 5: "Estoque inválido"
```
❌ Você digitou: 0 ou -5 (zero ou negativo)
✅ Correto: 5, 10, 100 (positivo)
```

### Erro 6: "Email já está cadastrado"
```
❌ Você tentou cadastrar: joao@email.com
✅ Já existe alguém com este email
→ Use outro email ou busque e atualize o cliente existente
```

---

## 📊 EXEMPLO COMPLETO DE USO

### Cenário: Abrir loja nova

**Passo 1: Cadastrar cliente**
```
Menu > 1 (Gerenciar Clientes) > 1 (Cadastrar)
Nome: Ana Silva
Telefone: 21987654321
Email: ana@email.com
Data: 1992-06-15
✅ ID: 1 criado
```

**Passo 2: Cadastrar produtos**
```
Menu > 2 (Gerenciar Produtos) > 1 (Cadastrar)
Nome: Feijão 1kg
Preço: 12.50
Estoque: 50
✅ ID: 1 criado

(Repita para mais produtos)
```

**Passo 3: Conferir dados**
```
Menu > 1 > 2 (Listar)
→ Confirma cliente Ana, 32 anos ✅

Menu > 2 > 2 (Listar)
→ Confirma produtos com preços ✅
```

**Passo 4: Atividade diária**
```
Menu > 2 > 3 (Atualizar Estoque)
→ Vendeu um feijão? Estoque 49
→ Repôs? Voltou para 80
```

**Passo 5: Relatório**
```
Menu > 2 > 5 (Relatório Estoque Baixo)
→ "Óleo está com 8 unidades, precisa repor!"
```

---

## 🎯 PRÓXIMOS PASSOS

1. **Experimente:**
   - Cadastre clientes com seus dados
   - Cadastre produtos reais
   - Teste todas as funções

2. **Explore:**
   - Tente buscar por partes de nomes
   - Veja o relatório de estoque baixo
   - Teste remoção com confirmação

3. **Confie:**
   - Dados nunca se perdem
   - IDs nunca duplicam
   - Validação sempre funciona
   - Sistema é seguro

---

**Sucesso! Sistema pronto para uso.** 🚀
