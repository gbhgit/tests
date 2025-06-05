## Teste de Código React

### Objetivo

Simular uma tela onde o usuário pode **iniciar um processo assíncrono**, e o app irá **verificar o status da tarefa a cada 2 segundos**. Quando a tarefa for concluída, exibir o resultado.

---

### 📋 Requisitos

1. Um botão: **"Iniciar Processo"**.

2. Ao clicar:

   * Simular uma tarefa com os status: `"pendente"` → `"processando"` → `"concluído"` (ex: após 6–10 segundos no total).
   * Verificar o status da tarefa a cada 2 segundos usando `setInterval`.

3. Enquanto estiver aguardando:

   * Mostrar uma mensagem de carregamento como: `Status: processando…`.

4. Quando a tarefa estiver `"concluída"`:

   * Mostrar: `Status: concluído ✅ Resultado: A tarefa foi concluída com sucesso`.

5. Se o usuário **atualizar a página**:

   * O status atual deve ser **carregado do `localStorage`**.
   * Se ainda não estiver `"concluído"`, continuar verificando o status como se o processo ainda estivesse em execução.

6. Simular casos de falha com o status `"falhou"` e exibir uma mensagem de erro.
---

### Informações Adicionais

* Utilize o arquivo mockAPI.js para testar a simulação das chamadas da API;
* Utilizar a ferramenta https://playcode.io/react para desenvolver essa solução;

### Exemplo
https://github.com/user-attachments/assets/b9c7e4d6-8696-4d0b-94b3-c402f168ef22

