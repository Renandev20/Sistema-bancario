# **Este projeto foi desenvolvido para um desafio do BOOTCAMP DIO VIVO - Trilha Python - proposto pelo Professor Guilherme Carvalho**
### Foi desenvolvido com parceria da IA Generativa CHATGPT para debugar.

# Sistema Bancário

Este é um projeto simples de sistema bancário feito em Python. O sistema permite criar usuários, contas bancárias, realizar depósitos, saques e consultar extratos. Além disso, oferece funcionalidades para listar usuários, listar contas e modificar informações do usuário.

## Funcionalidades

- **Depósito**: Permite ao usuário depositar um valor em uma conta específica.
- **Saque**: Permite ao usuário sacar um valor de uma conta, respeitando limites e número máximo de saques.
- **Extrato**: Exibe o histórico de transações e o saldo atual de uma conta.
- **Novo Usuário**: Cria um novo usuário com informações como nome, CPF, data de nascimento e endereço.
- **Nova Conta**: Cria uma nova conta associada a um usuário existente.
- **Listar Usuários**: Exibe a lista de todos os usuários cadastrados.
- **Listar Contas**: Exibe a lista de todas as contas existentes.
- **Modificar Usuário**: Permite modificar as informações do usuário existente, como nome, data de nascimento e endereço.

## Requisitos

- **Python 3.7 ou superior**: Para executar este sistema, você precisará do Python instalado na sua máquina.

## Como Usar

1. Clone ou faça download do repositório do projeto.
2. Navegue até a pasta onde o arquivo do projeto está localizado.
3. Execute o arquivo Python para iniciar o sistema bancário:
   ```bash
   python <nome_do_arquivo.py>
# Estrutura do Projeto

O projeto é estruturado da seguinte forma:

## Funções Principais

- **menu()**: Exibe o menu de operações disponíveis no sistema bancário.
- **depositar()**: Realiza um depósito e retorna o saldo e o extrato atualizados.
- **sacar()**: Realiza um saque e retorna o saldo e o extrato atualizados.
- **exibir_extrato()**: Exibe o extrato de uma conta.
- **criar_usuario()**: Cria um novo usuário.
- **modificar_usuario()**: Permite modificar informações do usuário.
- **criar_conta()**: Cria uma nova conta para um usuário existente.
- **listar_usuarios()**: Lista todos os usuários cadastrados.
- **listar_contas()**: Lista todas as contas existentes.
- **filtrar_usuario()**: Filtra usuários pelo CPF.
- **filtrar_conta()**: Filtra contas pelo número.

## Função Principal

- **main()**: Controla o fluxo do menu e gerencia a interação com o usuário.

# Considerações Finais

Este projeto é uma versão simplificada de um sistema bancário. Ele foi projetado para fins educacionais e prática em Python. Aqui estão algumas considerações finais:

- **Escopo Limitado**: Este sistema não cobre todas as funcionalidades de um sistema bancário real. Por exemplo, não há autenticação de usuário, segurança, ou validação detalhada de dados.
- **Limitações**: O sistema assume um uso simplificado, sem conexão a um banco de dados real ou mecanismos de segurança complexos.
- **Oportunidades para Melhoria**: Há várias áreas para aprimoramento, incluindo:
  - Adicionar autenticação de usuário.
  - Implementar persistência de dados (armazenamento em um banco de dados ou arquivo).
  - Expandir para suportar transações entre contas.
- **Avisos para Usuários**: Este sistema não deve ser usado para propósitos de produção ou para gerenciar informações sensíveis, pois não possui recursos de segurança e validações adequadas.

Espero que este projeto seja útil para fins educacionais e prática em Python. 
Contribuições e melhorias são bem-vindas!
