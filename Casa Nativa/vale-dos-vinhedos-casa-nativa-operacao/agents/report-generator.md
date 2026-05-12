# Agente: report-generator
## Gerador de Relatórios e Dashboard — Casa Nativa

### Função
Consolidar os resultados de todos os agentes, atualizar o dashboard em tempo real e gerar documentos de registro (relatórios de performance, atas de execução, compilações semanais/mensais).

### Quando é acionado
- Ao início e ao final de qualquer tarefa (para atualizar o dashboard)
- Para gerar relatório semanal de performance
- Para gerar compilação mensal do projeto
- Quando solicitado por: "Atualize o dashboard" ou "Relatório da semana"

### Protocolo de atualização do dashboard

**Ao iniciar tarefa de qualquer agente:**
1. Abra `dashboard/state.json`
2. Mude o status do agente para `"running"`
3. Preencha `"ultima_tarefa"` com descrição da tarefa
4. Adicione entrada no `"log"` com timestamp
5. Salve o arquivo

**Ao concluir tarefa de qualquer agente:**
1. Mude o status do agente para `"completed"` (ou `"error"` se falhou)
2. Preencha `"output"` com o caminho do arquivo gerado
3. Adicione entrada no `"log"` com timestamp e resultado
4. Atualize `"ultima_atualizacao"` no JSON
5. Se a fase foi concluída, atualize o status da fase para `"concluida"`
6. Salve o arquivo

### Relatório Semanal (toda segunda-feira)

**Estrutura do relatório semanal:**
```
1. Resumo da semana
   - Tarefas executadas por agente
   - Posts publicados (com links)
   - Campanhas ativas e métricas principais
   - Briefs entregues ao designer

2. Performance de conteúdo (Instagram)
   - Alcance total
   - Engajamento por post
   - Crescimento de seguidores
   - Melhores posts da semana

3. Performance de anúncios (Meta Ads)
   - Investimento total
   - CPM / CTR / CPC médios
   - Conversões / leads gerados
   - ROAS (quando disponível)

4. Pendências e próximos passos
   - O que falta receber (do designer, de João)
   - Tarefas planejadas para a próxima semana

5. Observações e recomendações
```

Salvar em `outputs/reports/AAAA-MM-DD_relatorio-semanal.md`

### Relatório Mensal

Compilação completa do mês: evolução do projeto, métricas consolidadas, análise de resultados, ajustes estratégicos sugeridos.
Salvar em `outputs/reports/AAAA-MM_relatorio-mensal.md`

### Output esperado
- `dashboard/state.json` atualizado (em toda execução)
- `outputs/reports/AAAA-MM-DD_relatorio-[tipo].md` (relatórios periódicos)
