# 🛒 SISTEMA DE MERCADO

## ✅ O que foi construído

Um sistema completo de gerenciamento de mercado em **Python puro** sem dependências externas, com:

- ✅ Gerenciamento de **Clientes** (cadastro, listagem, busca, remoção)
- ✅ Gerenciamento de **Produtos** (cadastro, listagem, atualização de estoque, remoção, relatório)
- ✅ Persistência em arquivos `.txt`
- ✅ Menu organizado e intuitivo
- ✅ Validações robustas de dados
- ✅ Cálculo automático de idade
- ✅ Geração automática de IDs únicos
- ✅ Separação clara de responsabilidades

## 📁 Estrutura de Arquivos

```
Sistema de mercado/
├── main.py           # Menu principal (inicie por aqui!)
├── clientes.py       # Lógica de clientes
├── produtos.py       # Lógica de produtos
├── utils.py          # Funções utilitárias compartilhadas
├── clientes.txt      # Dados de clientes (criado automaticamente)
└── produtos.txt      # Dados de produtos (criado automaticamente)
```

## 🚀 Como executar

Abra um terminal na pasta `Sistema de mercado` e execute:

```bash
python main.py
```

## 📊 Formatos de Dados

### clientes.txt
```
id;nome;telefone;email;data_nascimento
1;João Silva;11999999999;joao@email.com;1995-04-10
2;Maria Santos;21988888888;maria@email.com;1998-07-15
```

### produtos.txt
```
id;nome;preco;estoque
1;Arroz;25.90;50
2;Feijão;12.50;30
3;Açúcar;8.00;5
```

## 🎯 Funcionalidades Detalhadas

### CLIENTES
- **Cadastrar**: Email único, validação de telefone (10+ dígitos), data no formato AAAA-MM-DD
- **Listar**: Mostra todos com idade calculada automaticamente
- **Buscar**: Por nome (parcial) ou telefone
- **Remover**: Com confirmação antes de deletar

### PRODUTOS
- **Cadastrar**: Preço em float (use . para decimal), estoque em inteiro > 0
- **Listar**: Mostra todos com formatação de moeda
- **Atualizar Estoque**: Modifica quantidade sem perder dados do produto
- **Remover**: Com confirmação antes de deletar
- **Relatório**: Mostra produtos com estoque < 10 unidades

## 🔧 Pontos Críticos Implementados

### 1️⃣ ID Automático
✅ Lê todos os registros → Pega maior ID → Soma +1
- Evita duplicação de IDs
- Seguro mesmo com exclusões

### 2️⃣ Validação de Tipos
✅ Preço: convertido para `float`, validação de positivo
✅ Estoque: convertido para `int`, validação > 0
✅ Email: validação de formato básica (@, .)
✅ Telefone: apenas dígitos, mínimo 10
✅ Data: formato AAAA-MM-DD com cálculo de idade

### 3️⃣ Controle de Estoque
✅ Lê arquivo completo
✅ Altera apenas o registro necessário
✅ Reescreve arquivo inteiro
✅ Seguro e sem corrupção de dados

### 4️⃣ Separação de Responsabilidades
✅ `main.py`: Menu apenas (sem lógica)
✅ `clientes.py`: Toda lógica de clientes
✅ `produtos.py`: Toda lógica de produtos
✅ `utils.py`: Funções compartilhadas (arquivo, ID, validação)
✅ Sem código repetido
✅ Sem variáveis globais desnecessárias

## 📝 Dados de Teste

Para testar o sistema, você pode criar dados iniciais:

**clientes.txt**
```
1;João Silva;11999999999;joao@email.com;1995-04-10
2;Maria Santos;21988888888;maria@email.com;1998-07-15
3;Pedro Oliveira;85987654321;pedro@email.com;1990-12-25
```

**produtos.txt**
```
1;Arroz 5kg;25.90;50
2;Feijão Carioca;12.50;30
3;Açúcar 1kg;8.00;5
4;Sal Refinado;3.50;100
5;Óleo de Soja;7.80;8
```

## 💡 Exemplos de Uso

### Cadastrar Cliente
```
Nome: João da Silva
Telefone: 11999999999
Email: joao@email.com
Data: 1995-04-10
✅ Cliente cadastrado com sucesso (ID: 1)
```

### Cadastrar Produto
```
Nome: Arroz
Preço: 25.90
Estoque: 50
✅ Produto cadastrado com sucesso (ID: 1)
```

### Relatório de Estoque Baixo
Mostra automaticamente:
- Produtos com menos de 10 unidades
- ID, Nome, Preço e Quantidade

## ✨ Características Extras

- ✅ Formatação de tabelas clara e alinhada
- ✅ Mensagens de erro e sucesso com emoji
- ✅ Pausas para visualizar mensagens
- ✅ Confirmação antes de deletar dados
- ✅ Busca parcial por nome
- ✅ Tratamento de erros de entrada
- ✅ Arquivos UTF-8 para acentuação
- ✅ Suporte a Windows e Linux

## 🔒 Integridade de Dados

- ✅ Email nunca duplicado
- ✅ ID nunca duplicado
- ✅ Tipos sempre validados
- ✅ Arquivo sempre consistente
- ✅ Sem dados corrompidos

## 📌 Resumo Técnico

| Aspecto | Implementação |
|---------|---------------|
| Linguagem | Python 3.x |
| Banco de Dados | Arquivos .txt |
| Persistência | Leitura/Escrita sempre completa |
| Validação | Completa em todos os campos |
| IDs | Geração automática única |
| Idade | Cálculo automático |
| Menus | Hierárquicos e intuitivos |
| Tratamento de Erros | Try/except em todas as conversões |

---

**Criado respeitando as 4 regras críticas de desenvolvimento profissional!** 🚀
