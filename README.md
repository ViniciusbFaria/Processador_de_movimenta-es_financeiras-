# Processador_de_movimenta-es_financeiras-
Processador de Movimentações Financeiras 

Projeto desenvolvido para a simulação de processamento de movimentações financeiras semelhante a módulos de sistemas ERP.


Processar lançamentos financeiros a partir de um arquivo CSV, realizando:

- Cálculo de saldo por conta
- Validações de consistência
- Geração de relatórios consolidados
- Fechamento diário por conta
- Detecção de lançamentos duplicados
- Rollback lógico de lançamentos inválidos

## Formato do Arquivo de Entrada

O sistema utiliza um arquivo CSV com separador `;`


### Exemplo de arquivo válido:
-2026-01-01;CAIXA;C;1000.00;Saldo inicial
-2026-01-02;CAIXA;D;200.00;Compra insumos
-2026-01-02;BANCO;C;500.00;Recebimento cliente
-2026-01-03;CAIXA;D;900.00;Pagamento fornecedor
-2026-01-03;BANCO;D;100.00;Tarifa bancaria


### Regras:
- `C` (Crédito): soma ao saldo da conta
- `D` (Débito): subtrai do saldo da conta
- Cada conta possui saldo independente (ex.: CAIXA, BANCO)

---

## Etapas Implementadas

### Cálculo de Saldo Final
- Leitura do arquivo CSV
- Cálculo do saldo final por conta
- Exibição do resultado em ordem alfabética

---

### Consolidação e Validações
- Cálculo do total de créditos
- Cálculo do total de débitos
- Contagem da quantidade de lançamentos processados
- Processamento dos registros na ordem do arquivo
- Registro de inconsistências quando o saldo ficaria negativo

---

### Funcionalidades Opcionais
- Fechamento diário por conta, registrando o saldo final de todas as contas para cada data
- Detecção de lançamentos duplicados quando todos os campos do registro são idênticos

---

### Bônus Técnico (Rollback Lógico)
- Implementação de rollback lógico
- Lançamentos de débito que resultariam em saldo negativo são automaticamente desconsiderados
- O saldo da conta permanece inalterado
- A tentativa de lançamento é registrada na saída para auditoria

---

## Processos Internos

- Os registros são processados sequencialmente, respeitando a ordem do arquivo CSV
- As validações são realizadas no momento do processamento
- O sistema mantém estruturas internas para controle de saldos, duplicidades, inconsistências, rollbacks e fechamento diário

---

## Saídas Geradas

O sistema exibe no terminal:

- Saldo final por conta
- Resumo das movimentações (créditos, débitos e quantidade)
- Fechamento diário por conta
- Lista de inconsistências encontradas
- Lançamentos duplicados detectados
- Rollbacks lógicos realizados

---

## Requisitos para Execução

- Python 3.8 ou superior


