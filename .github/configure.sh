#!/usr/bin/env bash
set -euo pipefail

repo="Winipedia/pyrig-private"

dependency_alerts() {
  gh api "repos/${repo}/vulnerability-alerts" --method=PUT
}

dependency_security_updates() {
  gh api "repos/${repo}/automated-security-fixes" --method=PUT
}

release_immutability() {
  gh api "repos/${repo}/immutable-releases" --method=PUT
}

repository() {
  jq '.repository' .github/settings.json | gh api "repos/${repo}" --method=PATCH --input=-
}

rulesets() {
  local endpoint="repos/${repo}/rulesets"
  jq --compact-output '.rulesets[]' .github/settings.json | while read -r ruleset; do
    id=$(gh api "${endpoint}" \
      | jq --raw-output --argjson r "${ruleset}" '.[] | select(.name==$r.name) | .id')
    if [[ -z ${id} ]]; then method="POST"; else method="PUT"; fi
    url="${endpoint}${id:+/${id}}"
    gh api "${url}" --method="${method}" --input=- <<<"${ruleset}"
  done
}

topics() {
  jq '{names: .topics}' .github/settings.json | gh api "repos/${repo}/topics" --method=PUT --input=-
}

for step in $(declare -F | awk '{print $3}'); do
  "${step}"
done
