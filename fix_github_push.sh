#!/bin/bash
set -e

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"

echo "📁 Repositório: $REPO_DIR"
echo ""

# 0. Remover lock files
echo "🔓 Removendo lock files..."
rm -f .git/HEAD.lock .git/index.lock .git/refs/heads/main.lock .git/packed-refs.lock
echo "✅ Locks removidos"
echo ""

# 1. Explicitamente remover o arquivo grande do cache se existir
echo "🗑️  Removendo arquivo grande do cache..."
git rm --cached -f "03 Licenciados/zitnOrke" 2>/dev/null && echo "   zitnOrke removido do cache" || echo "   zitnOrke não estava no cache"
echo ""

# 2. Limpa o restante do índice
echo "🧹 Limpando índice git..."
git rm -r --cached -f . --quiet 2>/dev/null || true
echo "✅ Índice limpo"

# 3. Re-adiciona respeitando .gitignore
echo "📂 Re-adicionando arquivos..."
git add .

# 4. Verificar que zitnOrke NÃO está como "A" (added) — "D" (deleted) é ok
if git status --short | grep "^A.*zitnOrke"; then
  echo "❌ ERRO: zitnOrke está sendo adicionado! Abortando."
  exit 1
else
  echo "✅ zitnOrke não está sendo adicionado (ok)"
fi

echo "Total de mudanças: $(git status --short | wc -l) arquivos"
echo ""

# 5. Amenda o commit
echo "💾 Atualizando commit..."
git commit --amend -m "feat: repositório inicial Grupo Comsteel — documentação estratégica, context, Design System e Hub de Arquitetos"
echo ""

# 6. Force push
echo "🚀 Enviando para GitHub..."
git push -f origin main
echo ""
echo "✅ CONCLUÍDO!"
echo "🔗 https://github.com/joaobureauia-cmd/grupo-comsteel"
