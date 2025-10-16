# Projeto Chat Online - Programação Orientada a Objetos (POO)

Este projeto é um **chat online local com interface gráfica** desenvolvido com o paradigma de Programação Orientada a Objetos, utilizando a linguagem **Python** e o toolkit **Tkinter**. Ele permite múltiplos usuários se comunicarem em tempo real através de uma arquitetura cliente-servidor.

---

## 🧩 Estrutura do Projeto

```bash
Chat Room/
├── main.py                 # Inicia o cliente (janela de login/chat)
├── servidor.py             # Servidor central TCP
├── start_client.py         # Abre múltiplos clientes automaticamente
├── casos_de_uso.png        # Diagrama de casos de uso
├── diagrama_classes.png    # Diagrama de classes
├── README.md               # Este arquivo
└── src/
    ├── controlador.py      # Controlador principal do cliente
    ├── gui/
    │   ├── __init__.py
    │   ├── janela_base.py
    │   ├── janela_login.py
    │   ├── janela_chat.py
    │   └── redimensionavel_mixin.py
    └── models/
        ├── __init__.py
        ├── usuario.py
        ├── mensagem.py
        └── chat.py
```

---

## ▶️ Como Executar

### 1. Inicie o Servidor
```bash
python servidor.py
```

### 2. Inicie os Clientes
Você pode abrir vários manualmente:
```bash
python main.py
```
Ou abrir múltiplos automaticamente:
```bash
python start_client.py
```

---

## ✅ Funcionalidades
- Tela de login com nome do usuário
- Interface de chat redimensionável
- Envio e recebimento de mensagens em tempo real
- Conexão com servidor TCP local
- Broadcast de mensagens para todos os usuários
- Arquitetura modular com separação de camadas (GUI, lógica, modelo)

---

## 📦 Requisitos
- Python 3.x

Não há dependências externas. Apenas `tkinter` (vem com Python).

---

## 🎯 Paradigmas e POO Utilizados
- ✅ Herança (`JanelaBase` → `JanelaLogin`, `JanelaChat`)
- ✅ Polimorfismo (`exibir_mensagem`, `iniciar`, etc.)
- ✅ Mixin (`RedimensionavelMixin`)
- ✅ Composição forte (`Chat` contém `Mensagem`)
- ✅ Associação fraca (`Mensagem` referencia `Usuario`)

---

## 📋 Casos de Uso
### Caso 01 – Login
**Ator:** Usuário  
**Descrição:** O usuário informa um nome de usuário para entrar no sistema.

**Fluxo Principal:**
1. O sistema exibe uma tela de login com um campo de texto.
2. O usuário digita seu nome.
3. O sistema valida o nome (não vazio).
4. O sistema inicializa a interface de chat.

---

### Caso 02 – Entrar no Chat
**Ator:** Usuário  
**Descrição:** Após realizar o login, o usuário é direcionado à tela principal do chat.

**Fluxo Principal:**
1. O sistema cria uma conexão com o servidor de chat.
2. A janela de chat é exibida.
3. O histórico de mensagens é carregado em tempo real (se houver).

---

### Caso 03 – Enviar Mensagem
**Ator:** Usuário  
**Descrição:** O usuário envia uma mensagem textual no chat.

**Fluxo Principal:**
1. O usuário digita uma mensagem no campo de entrada.
2. Pressiona Enter.
3. O sistema exibe a mensagem imediatamente no chat.
4. O sistema envia a mensagem ao servidor.
5. O servidor redistribui a mensagem a todos os clientes conectados.

---

### Caso 04 – Receber Mensagens
**Ator:** Sistema  
**Descrição:** Mensagens enviadas por outros usuários são recebidas e exibidas no chat.

**Fluxo Principal:**
1. O sistema escuta mensagens no socket TCP.
2. Quando recebe, converte de JSON para mensagem.
3. Exibe no chat com remetente e horário.

---

### Caso 05 – Redimensionar Janela
**Ator:** Usuário  
**Descrição:** O usuário pode alterar o tamanho da janela do chat conforme desejar.

**Fluxo Principal:**
1. O usuário clica e arrasta a borda da janela.
2. A interface ajusta os elementos (campo de entrada, área de texto).

---

### Caso 06 – Sair do Chat
**Ator:** Usuário  
**Descrição:** O usuário fecha a janela do chat para encerrar sua participação.

**Fluxo Principal:**
1. O usuário fecha a janela.
2. A conexão com o servidor é encerrada.
3. O cliente é finalizado sem erro.

## 📋 Diagrama Casos de Uso
![Diagrama Casos de Uso](casos_de_uso.png)
---

## 🧱 Diagrama de Classes

![Diagrama de Classes](diagrama_classes.png)

## 🧱 Relacionamentos entre Classes
- `ControladorChat` **usa**: `Usuario`, `Mensagem`, `JanelaLogin`, `JanelaChat`
- `JanelaLogin` e `JanelaChat` **herdam** de: `JanelaBase`
- `JanelaChat` **usa** um **Mixin**: `RedimensionavelMixin`
- `Mensagem` **contém** um: `Usuario`
- `Chat` **gerencia listas de**: `Usuario` e `Mensagem`

---

## 👤 Autor
Projeto desenvolvido por **Gabriel Goldenberg Moita** para disciplina de Programação Orientada a Objetos.






