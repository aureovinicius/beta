#!/usr/bin/env bash
# Sintetiza o áudio (TTS) de cada roteiro de narração com a voz pt-BR do macOS.
# Os roteiros são gerados por gerar_canal.py em youtube/**/*.narracao.txt
#
# Uso:
#   ./gerar_audio.sh            # voz padrão (Luciana), formato m4a (AAC)
#   ./gerar_audio.sh Felipe     # outra voz pt-BR
#
# É idempotente: pula os áudios já existentes. Roda em lote (pode demorar:
# ~570 tópicos => possivelmente 1-3 h e algumas centenas de MB). Tudo local
# (a pasta youtube/ é ignorada pelo git).
set -euo pipefail
VOZ="${1:-Luciana}"
cd "$(dirname "$0")/youtube"
total=$(find . -name '*.narracao.txt' | wc -l | tr -d ' ')
i=0
find . -name '*.narracao.txt' | sort | while read -r f; do
  i=$((i + 1))
  out="${f%.narracao.txt}.m4a"
  if [ -f "$out" ]; then
    echo "[$i/$total] (já existe) $out"
    continue
  fi
  say -v "$VOZ" -o "$out" --data-format=aac -f "$f"
  echo "[$i/$total] $out"
done
echo "Concluído."
