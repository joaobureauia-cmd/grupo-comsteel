#!/bin/bash
# Setup Git — Grupo Comsteel
# Execute este script uma vez para conectar a pasta ao repositório GitHub

set -e

REPO_DIR="/Users/joaogabriel/Downloads/Grupo Comsteel "
REMOTE_URL="https://github.com/joaobureauia-cmd/grupo-comsteel.git"

echo "🚀 Iniciando setup do repositório Grupo Comsteel..."
cd "$REPO_DIR"

# Inicializar git se ainda não foi feito
if [ ! -d ".git" ]; then
  git init
  echo "✅ Repositório git inicializado"
else
  echo "ℹ️  Repositório git já existe"
fi

# Criar .gitignore
cat > .gitignore << 'GITIGNORE'
.DS_Store
**/.DS_Store
*.tmp
*.log
Thumbs.db
GITIGNORE

echo "✅ .gitignore criado"

# Configurar remote
if git remote | grep -q origin; then
  git remote set-url origin "$REMOTE_URL"
  echo "✅ Remote origin atualizado"
else
  git remote add origin "$REMOTE_URL"
  echo "✅ Remote origin adicionado"
fi

# Adicionar arquivos (excluindo arquivos muito grandes como vídeos)
echo "📦 Adicionando arquivos... (pode demorar alguns segundos)"
git add --all

# Commit inicial
git commit -m "feat: Design System inicial — logos, renders, portfólio e documentação

- 01_Logos: logos Construção & Mobilidade + Tiny House
- 02_Renders_Tiny_House: 199 imagens (13 modelos)
- 03_Portfolio_Construcao: 669 fotos (14 projetos)
- 04_Documentacao: identidade visual, tom de voz, mensagens-chave, guia de assets
- README.md: índice completo do Design System"

# Push para GitHub
echo "🚀 Enviando para GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ Concluído! Repositório disponível em:"
echo "   https://github.com/joaobureauia-cmd/grupo-comsteel"
