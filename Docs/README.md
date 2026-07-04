# Documentação · Respira / Ventila

Hub central da documentação do projeto. Alguns arquivos permanecem na **raiz** por serem lidos automaticamente por ferramentas (GitHub, agentes) — este índice cataloga todos, morem eles onde morarem.

## Referência do projeto (nesta pasta)

| Documento | O que é |
|---|---|
| [`NORMALIZACAO.md`](NORMALIZACAO.md) | Nomenclatura pública, mapa canônico (Respira, Ponte Funcional, Ocupacional, Ventila) e política de compatibilidade de rotas. |
| [`atlas-laminas-plano.md`](atlas-laminas-plano.md) | Plano de expansão do Atlas de pranchas — lâminas 06–10, Ponte Funcional (RF1–4) e Ocupacional (RO1), com convenção de arquivos e critério de pronto. |
| [`atlas-auditoria.md`](atlas-auditoria.md) | Auditoria do Atlas, módulos, figuras e navegação (antes `filter.md`): sincronia índice × Atlas × mapa canônico e a fragilidade da cadeia de wrappers. |

## Governança e operação (na raiz — lidos por ferramentas)

| Documento | O que é | Por que fica na raiz |
|---|---|---|
| [`../README.md`](../README.md) | Landing do repositório: visão geral, séries e publicação. | GitHub renderiza o README da raiz. |
| [`../CLAUDE.md`](../CLAUDE.md) | Manual operacional para instâncias Claude/agentes: tese, invariantes, política de build/DRY, Definition of Done. | Carregado automaticamente por agentes no diretório do projeto. |
| [`../AGENTS.md`](../AGENTS.md) | Orientação para agentes, Codex e colaboradores automatizados. | Convenção `AGENTS.md` lida na raiz. |

## Atribuição e mídia (junto dos assets)

Documentos que descrevem mídia de terceiros vivem ao lado dos próprios arquivos, para preservar contexto e licença:

| Documento | O que é |
|---|---|
| [`../assets/respira-ventila-atlas/ATLAS.md`](../assets/respira-ventila-atlas/ATLAS.md) | Manifesto do atlas de mídia aberta Respira/Ventila. |
| [`../assets/respira-ventila-atlas/media/ATTRIBUTION.md`](../assets/respira-ventila-atlas/media/ATTRIBUTION.md) | Créditos e licenças das mídias do atlas aberto. |
| [`../assets/ventila17-26/OPEN_SOURCE_MEDIA.md`](../assets/ventila17-26/OPEN_SOURCE_MEDIA.md) | Mídia aberta usada em Ventila 17–26. |
| [`../assets/ventila17-26/media/ATTRIBUTION.md`](../assets/ventila17-26/media/ATTRIBUTION.md) | Créditos e licenças das mídias de Ventila 17–26. |

## Regra de ouro

Toda a documentação segue o mesmo princípio do código (ver `../AGENTS.md`): **atualizar para refletir o estado real, nunca reduzir**. Ao mudar arquitetura ou nomenclatura, atualize o `NORMALIZACAO.md` e este índice.
