# 🖥️ Python com Interface Gráfica

Este repositório contém os exemplos práticos e projetos desenvolvidos durante o curso **"Criando um projeto com interface gráfica utilizando a linguagem Python"** oferecido pela **Fundação Bradesco**.

## 📚 Sobre o Curso

Este é o **4º curso** da trilha de conhecimento em **Linguagem de Programação Python** da Fundação Bradesco, composta por 5 cursos progressivos. O curso aborda conceitos avançados de programação orientada a objetos e desenvolvimento de interfaces gráficas utilizando o framework Kivy.

### 🎯 Posição na Trilha de Conhecimento
- **1º Curso**: Introdução à Programação Orientada a Objetos - POO → 
- **2º Curso**: Linguagem de Programação Python - Básico → [Repositório Python](https://github.com/BrunoBelarmino007/Python.git)
- **3º Curso**: Desenvolvimento Orientado a Objeto Utilizando a Linguagem Python → [Repositório PythoncomPOO](https://github.com/BrunoBelarmino007/PythoncomPOO.git)
- **4º Curso**: **Criando um Projeto com Interface Gráfica Utilizando a Linguagem Python (Este repositório)** ⭐
- **5º Curso**: Desenvolvendo um Projeto Completo Python com Estruturas de Dados → [Repositório PythonProjeto](https://github.com/BrunoBelarmino007/PythonProjeto.git) 

## 🎯 Conteúdo Estudado

### 📁 Módulo 2 - Programação Orientada a Objetos
Consolidação e aplicação avançada dos conceitos de POO com exemplos práticos:

#### **Classes e Objetos Básicos**
- **`Pessoa.py`**: Conceitos fundamentais de classes, atributos e métodos
- **`Area.py`**: Classe para cálculos geométricos (retângulos)
- **`Esfera.py`**: Cálculos matemáticos com volume e área de esferas

#### **Aplicações Práticas**
- **`Funcionario.py`**: Sistema de gerenciamento de funcionários com cálculo de salários
- **`Funcionalidades.py`**: Simulação de TV e controle remoto (interação entre objetos)
- **`Cronometro.py`**: Cronômetro funcional com interface de terminal

#### **Testes e Validações**
- **`TesteArea.py`**: Calculadora de azulejos para pisos
- **`TesteFuncionario.py`**: Testes do sistema de funcionários
- **`Teste.py`**: Validação das funcionalidades da TV

### 📁 Módulo 3 - Interface Gráfica com Kivy
Desenvolvimento de aplicações com interface gráfica moderna:

#### **Conceitos Básicos do Kivy**
- **`exemploButton.py`**: Criação e manipulação de botões
- **`exemploLayout.py`**: Organização de elementos na tela com layouts
- **`testKivyProject.py`**: Exibição de imagens e labels

#### **Aplicações Completas**
- **`exemploCalculadora.py`**: Calculadora funcional com interface gráfica
- **`main.py`**: Sistema completo de login e cadastro de usuários
- **`database.py`**: Gerenciamento de banco de dados para usuários

#### **Arquivos de Interface**
- **`my.kv`**: Arquivo de layout do Kivy para separação da lógica visual
- **`users.txt`**: Persistência de dados dos usuários cadastrados

## 📊 Estrutura do Projeto

```
PythoncomInterfaceGrafica/
├── modulo_2/                   # Programação Orientada a Objetos
│   ├── Area.py                 # Classe para cálculos geométricos
│   ├── Cronometro.py           # Cronômetro funcional
│   ├── Esfera.py               # Cálculos com esferas
│   ├── Funcionalidades.py      # TV e controle remoto
│   ├── Funcionario.py          # Sistema de funcionários
│   ├── Pessoa.py               # Conceitos básicos de POO
│   ├── TesteArea.py            # Calculadora de azulejos
│   ├── TesteFuncionario.py     # Testes do sistema
│   └── Teste.py                # Validações gerais
├── modulo_3/                   # Interface Gráfica com Kivy
│   ├── kivy_project/           # Ambiente virtual do Kivy
│   ├── database.py             # Gerenciamento de dados
│   ├── exemploButton.py        # Exemplo com botões
│   ├── exemploCalculadora.py   # Calculadora gráfica
│   ├── exemploLayout.py        # Layouts do Kivy
│   ├── main.py                 # Sistema de login completo
│   ├── my.kv                   # Arquivo de interface Kivy
│   ├── testKivyProject.py      # Testes básicos do Kivy
│   └── users.txt               # Base de dados dos usuários
├── .gitignore                  # Arquivos ignorados pelo Git
└── README.md                   # Este arquivo
```


## 🚀 Como Executar os Projetos

### Pré-requisitos
```bash
# Python 3.x
python --version
- Ambiente virtual 
```
### Passos para Execução

1. **Clone o repositório:**
```bash
git clone https://github.com/BrunoBelarmino007/PythoncomInterfaceGrafica.git
cd PythoncomInterfaceGrafica
```

2. **Instale o ambiente virtual:**
```bash
# Dentro do módulo 3
cd modulo_3
python3 -m venv kivy_project
```

3. **Ative o ambiente virtual (opcional):**
```bash
# Windows
source kivy_project/Scripts/activate

# Linux/Mac
source kivy_project/bin/activate
```


4. **Depois Instale Kivy** 
```bash
 pip install kivy
```

### Executando Módulo 2 (POO)
```bash
cd modulo_2/

# Executar cronômetro
python Cronometro.py

# Testar calculadora de azulejos
python TesteArea.py

# Testar sistema de funcionários
python TesteFuncionario.py
```

### Executando Módulo 3 (Interface Gráfica)
```bash
cd modulo_3/

# Exemplos básicos
python exemploButton.py
python exemploLayout.py
python testKivyProject.py

# Calculadora gráfica
python exemploCalculadora.py

# Sistema completo de usuários
python main.py
```

## 🎯 Principais Aprendizados

### Programação Orientada a Objetos
- ✅ **Classes e Objetos**: Definição e instanciação
- ✅ **Encapsulamento**: Métodos públicos e privados
- ✅ **Interação entre Objetos**: Composição e agregação
- ✅ **Aplicações Práticas**: Sistemas reais com POO

### Interface Gráfica com Kivy
- ✅ **Widgets Básicos**: Button, Label, TextInput
- ✅ **Layouts**: BoxLayout, FloatLayout
- ✅ **Gerenciamento de Telas**: ScreenManager
- ✅ **Arquivos .kv**: Separação de lógica e interface
- ✅ **Eventos**: Binding e callbacks
- ✅ **Persistência**: Manipulação de arquivos para dados

## 🛠️ Projetos Desenvolvidos

### 1. **Cronômetro Digital** 
- Interface de terminal com atualização em tempo real
- Controle de horas, minutos e segundos
- Implementação de threading implícito

### 2. **Calculadora de Azulejos**
- Cálculo de materiais para construção
- Interface interativa por terminal
- Aplicação prática de geometria

### 3. **Sistema de Funcionários**
- Gerenciamento de dados de funcionários
- Cálculo automático de salários
- Estrutura de dados com dicionários

### 4. **Calculadora Gráfica**
- Interface moderna com Kivy
- Operações matemáticas básicas
- Tratamento de erros e validações

### 5. **Sistema de Login Completo**
- Cadastro e login de usuários
- Persistência em arquivo de texto
- Navegação entre telas
- Validação de formulários

## 🎨 Tecnologias Utilizadas

- **Python 3.x**: Linguagem base
- **Kivy**: Framework para interface gráfica
- **POO**: Paradigma de programação
- **File I/O**: Manipulação de arquivos
- **DateTime**: Manipulação de datas
- **Math**: Cálculos matemáticos

## 🏆 Competências Desenvolvidas

### Técnicas
- Programação orientada a objetos avançada
- Desenvolvimento de interfaces gráficas
- Gerenciamento de dados em arquivos
- Validação de formulários
- Organização de código em módulos

### Soft Skills
- Resolução de problemas complexos
- Pensamento estruturado
- Planejamento de projetos
- Documentação de código


## 🤝 Contribuições

Este repositório é para fins educacionais e faz parte de uma trilha de aprendizado. Sugestões de melhorias são bem-vindas!

---

Ofereça sua vida a Deus como um sacrifício vivo, santo e agradável, e permita que Ele transforme seu modo de pensar. Assim, você viverá para cumprir a boa, perfeita e agradável vontade do Senhor - Romanos 12:1 e 2.

---
