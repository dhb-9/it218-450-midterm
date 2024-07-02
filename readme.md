# MIDTERM

Doc:
https://docs.google.com/document/d/1ECQhG-yQekiTYdhKPdLDrf3vudMABSiCOHcI2E8NLuE/edit?usp=sharing

Video:
https://drive.google.com/file/d/1tYp76a4MXXE8Wj0Jb85tR_vsLRSqXjuV/view?usp=sharing

Certainly! Here's a comprehensive README documentation outline for your project. This documentation includes setup and usage instructions to ensure clarity and ease of use.

---

# Advanced Calculator Application

This is an advanced calculator application designed for a software engineering graduate course midterm project. It incorporates various design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL).

## Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage Instructions](#usage-instructions)
  - [Starting the Application](#starting-the-application)
  - [Commands](#commands)
- [Design Patterns](#design-patterns)

## Features

- **Command-Line Interface (REPL)**: Supports arithmetic operations, history management, and dynamic plugins.
- **Plugin System**: Dynamically loads new commands without modifying core code.
- **Calculation History Management**: Utilizes Pandas for robust history management.
- **Professional Logging**: Detailed logging of operations, errors, and informational messages.
- **Design Patterns**: Incorporates Command, Facade, Factory Method, Singleton, and Strategy patterns for scalable architecture.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/dhb-9/it218-450-midterm.git
   cd it218-450-midterm
   ```

2. **Create and activate a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage Instructions

### Starting the Application

Run the following command to start the calculator application:

```sh
python -m app
```

### Commands

The application supports the following commands:

- **add**: Perform addition
- **subtract**: Perform subtraction
- **multiply**: Perform multiplication
- **divide**: Perform division
- **history**: Display calculation history
- **clear**: Clear calculation history
- **delete**: Delete calculation history file
- **exit**: Exit the application

### Example Usage

1. **Adding two numbers**:
   ```
   Enter command (add/subtract/multiply/divide/history/clear/delete) or 'exit' to quit: add
   Enter first number: 10
   Enter second number: 5
   Result: 15
   ```

2. **Viewing history**:
   ```
   Enter command (add/subtract/multiply/divide/history/clear/delete) or 'exit' to quit: history
      command  operand1  operand2  result
   0      add      10.0       5.0    15.0
   ```

## Design Patterns

- **Command Pattern**:
- **Facade Pattern**:
- **Factory Method Pattern**:
- **Singleton Pattern**:
- **Strategy Pattern**:


This README covers the setup, usage, and highlights key aspects of your calculator application, including how to run it, the commands it supports, and the design patterns it employs.