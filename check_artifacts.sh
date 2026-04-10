#!/bin/bash
TOKEN="ghu_HbyW2MmVcMzFJtspEm7Fkb4VMtMul23RMmyc"
echo "Checking artifacts usage for all repos..."
total_size=0

while read repo; do
  size=$(curl -s -H "Authorization: Bearer $TOKEN" "https://api.github.com/repos/$repo/actions/artifacts" | jq '[.artifacts[].size_in_bytes] | add // 0')
  if [ "$size" -gt 0 ]; then
    size_mb=$(echo "scale=2; $size/1024/1024" | bc)
    echo "$repo: ${size_mb} MB ($size bytes)"
    total_size=$((total_size + size))
  fi
done < repos.txt

total_mb=$(echo "scale=2; $total_size/1024/1024" | bc)
echo "Total Artifacts Size: ${total_mb} MB"
