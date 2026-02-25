# 🛒 Sistema de Mercado

Um sistema completo de gerenciamento de mercado via terminal, desenvolvido em **Python puro**, sem banco de dados ou bibliotecas externas.

## 📋 Características

✅ **Gerenciamento de Clientes**
- Cadastrar clientes com validação de email único
- Listar clientes com cálculo automático de idade
- Buscar por nome ou telefone
- Remover cliente com confirmação

✅ **Gerenciamento de Produtos**
- Cadastrar produtos com validação de preço e estoque
- Listar produtos com indicador de estoque baixo
- Atualizar estoque de forma segura
- Remover produtos
- Relatório de produtos com estoque baixo

✅ **Recurso de Persistência**
- Dados salvos em arquivos `.txt` estruturados
- IDs gerados automaticamente sem duplicação
- Validação robusta de tipos de dados

## 🏗️ Arquitetura

```
Sistema de mercado/
├── main.py           # Menu principal e orquestração
├── clientes.py       # Lógica de gerenciamento de clientes
├── produtos.py       # Lógica de gerenciamento de produtos
├── utils.py          # Funções utilitárias
├── clientes.txt      # Persistência de clientes
└── produtos.txt      # Persistência de produtos
```

### Separação de Responsabilidades

- **main.py**: Apenas menu e coordenação
- **clientes.py**: Lógica exclusiva de clientes
- **produtos.py**: Lógica exclusiva de produtos
- **utils.py**: Validações e cálculos compartilhados

## 📊 Formato de Dados

### clientes.txt
```
id;nome;telefone;email;data_nascimento
1;João Silva;11987654321;joao@email.com;1995-04-10
2;Maria Santos;11912345678;maria@email.com;1998-07-15
```

### produtos.txt
```
id;nome;preco;estoque
1;Arroz Branco;25.90;50
2;Feijão Carioca;8.50;5
```

## 🚀 Como Usar

### Executar o Sistema

```bash
cd "Sistema de mercado"
python main.py
```

### Menu Principal

```
==================================================
🛒 SISTEMA DE MERCADO 🛒
==================================================
1 - Gerenciar Clientes
2 - Gerenciar Produtos
0 - Sair
==================================================
```

### Menu de Clientes

```
1 - Cadastrar Cliente
2 - Listar Clientes
3 - Buscar Cliente
4 - Remover Cliente
0 - Voltar ao Menu Principal
```

**Validações:**
- Email único (não permite duplicatas)
- Telefone com mínimo 10 dígitos
- Email com formato básico (contém @ e .)
- Data de nascimento no formato YYYY-MM-DD

### Menu de Produtos

```
1 - Cadastrar Produto
2 - Listar Produtos
3 - Atualizar Estoque
4 - Remover Produto
5 - Relatório de Estoque Baixo
0 - Voltar ao Menu Principal
```

**Validações:**
- Preço como número positivo (aceita . ou ,)
- Estoque como número inteiro positivo
- Estoque baixo: ≤ 10 unidades

## 🔑 Decisões de Design

### 1️⃣ Geração de ID Automática
```python
def _gerar_id():
    clientes = _ler_clientes()
    if not clientes:
        return 1
    return max(cliente["id"] for cliente in clientes) + 1
```
Garante que não há duplicação lendo todos os IDs e pegando o maior + 1.

### 2️⃣ Validação de Tipos
```python
def validar_preco(preco_str):
    try:
        preco = float(preco_str.replace(",", "."))
        return preco if preco > 0 else None
    except ValueError:
        return None
```
Conversão segura com tratamento de erro: string → float.

### 3️⃣ Controle de Estoque
```python
def atualizar_estoque():
    produtos = _ler_produtos()  # Lê todos
    produto["estoque"] = novo_estoque  # Modifica correto
    _salvar_produtos(produtos)  # Reescreve tudo
```
Estratégia simples: ler tudo, modificar, reescrever.

### 4️⃣ Menu Sem Lógica
```python
# main.py apenas chama funções
if opcao == "1":
    menu_clientes()
elif opcao == "2":
    menu_produtos()
```
Menu puro: só coordena, nunca contém lógica.

## ✨ Recursos Avançados

### Cálculo de Idade
O sistema calcula a idade automaticamente ao listar clientes:
```
ID   Nome                 Idade  Telefone        Email
1    João Silva           28     11987654321     joao@email.com
2    Maria Santos         25     11912345678     maria@email.com
```

### Indicador de Estoque
Produtos com estoque ≤ 10 aparecem marcados com ⚠️ BAIXO:
```
ID  Nome             Preço      Estoque  Status
1   Arroz Branco    R$ 25.90   50       ✅ OK
2   Feijão Carioca  R$  8.50   5        ⚠️ BAIXO
```

### Relatório de Estoque Baixo
Dashboard específico para produtos que precisam reposição:
```
⚠️ Feijão Carioca: 5 unidades
⚠️ Açúcar: 8 unidades

Total de produtos com estoque baixo: 2
```

## 🛡️ Tratamento de Erros

✅ Arquivo não existe? Cria automaticamente.
✅ Dados malformados? Ignora e continua.
✅ Email duplicado? Previne cadastro.
✅ Operação cancelada? Retorna ao menu.
✅ ID inválido? Mensagem clara.

## 📝 Exemplos de Uso

### Cadastrar Cliente

```
Nome: João Silva
Telefone: 11987654321
Email: joao@email.com
Data de nascimento (YYYY-MM-DD): 1995-04-10
✅ Cliente cadastrado com sucesso! ID: 1
```

### Cadastrar Produto

```
Nome do produto: Arroz Branco
Preço (use . ou ,): 25,90
Quantidade em estoque: 50
✅ Produto cadastrado com sucesso! ID: 1
```

### Atualizar Estoque


ID do produto: 1
Produto encontrado: Arroz Branco
Estoque atual: 50
Novo estoque: 45
✅ Estoque atualizado com sucesso! Novo estoque: 45
