#!/bin/bash
TOKEN="ghu_HbyW2MmVcMzFJtspEm7Fkb4VMtMul23RMmyc"
REPO="refreshcoder/ilisten"

echo "Fetching artifacts for $REPO..."
curl -s -H "Authorization: Bearer $TOKEN" "https://api.github.com/repos/$REPO/actions/artifacts?per_page=100" | jq -r '.artifacts[] | .id' > artifacts_to_delete.txt

count=$(wc -l < artifacts_to_delete.txt)
echo "Found $count artifacts to delete."

while read id; do
  echo "Deleting artifact $id..."
  curl -s -X DELETE -H "Authorization: Bearer $TOKEN" "https://api.github.com/repos/$REPO/actions/artifacts/$id"
done < artifacts_to_delete.txt
echo "Done."
