---
date: 2026-07-31
slug: hello-world
---

# GPT 5.6-sol 276k is equivalent or worse when using None reasoning as compared to medium

I don't have the stomach to run this experiment for $100 worth of trials, I'm fine just catching it once in the wild. I'm sure there are cases where medium reasoning, or even maxed out reasoning results in better outputs, but this is a case that shows the opposite.

I wanted to microblog somewhere that I finally have a session where gpt-5.6-sol did better in VS Code (local) with None thinking.  The session is NWU1MzM0Y2ItMTIyMy00NmU5LWJjOWItY2NkMmJmMGFmOTA5

Prompt:

> When I "Inspect editor tokens and scopes for this erb symbol, I get this output which indicates a foreground color of `#5F594F`.  But the actual color is much brighter.  What could be happening?
>
>## <%=3 chars
>
>---
>languageerbstandard token typeOtherforeground#5F594F
>background#121314
>contrast ratio2.68
>---
>textmate scopespunctuation.section.embedded.begin.erb
>meta.embedded.line.erb
>text.html.erbforeground`punctuation.section.embedded.begin.erb{ "foreground": "#5F594F" }`
```

Results (paraphrased):

1) It's clear, try `complete.madeup.config`
or
2) try `"editor.semanticHighlighting.enabled": false` (bingo)
