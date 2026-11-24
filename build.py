"""Builds index.html (a single self-contained file) from src/ and vault/."""
import json, pathlib
root = pathlib.Path(__file__).parent
vault = {}
for p in sorted((root / 'vault').rglob('*.md')):
    vault[p.relative_to(root / 'vault').as_posix()] = p.read_text(encoding='utf-8')
data = json.dumps(vault, ensure_ascii=False).replace('</', '<\\/')
html = (root / 'src/template.html').read_text(encoding='utf-8')
html = html.replace('/*__CSS__*/', (root / 'src/app.css').read_text(encoding='utf-8'))
html = html.replace('/*__VAULT__*/', data)
html = html.replace('/*__JS__*/', (root / 'src/app.js').read_text(encoding='utf-8').replace('</script', '<\\/script'))
(root / 'index.html').write_text(html, encoding='utf-8')
print(f'index.html built: {len(vault)} notes, {len(html)//1024} KB')
