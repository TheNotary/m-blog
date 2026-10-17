---
date: 2026-07-31
slug: hello-world
---

# GPT 5.6-sol 276k is equivalent or worse when using None reasoning as compared to medium

I don't have the stomach to run this experiment for $100 worth of trials, I'm fine just catching it once in the wild. I'm sure there are cases where medium reasoning, or even maxed out reasoning results in better outputs (especially in benchmark settings, obviously) but this is a case that shows the opposite.

I wanted to microblog somewhere that I finally have a session where gpt-5.6-sol did better in VS Code (local) with None thinking.  The session is NWU1MzM0Y2ItMTIyMy00NmU5LWJjOWItY2NkMmJmMGFmOTA5

Prompt:

> When I "Inspect editor tokens and scopes for this erb symbol, I get this output which indicates a foreground color of `#5F594F`.  But the actual color is much brighter.  What could be happening?
>
> (editor tokens copy/ paste)
<pre>
## <%=3 chars

---
languageerbstandard token typeOtherforeground#5F594F
background#121314
contrast ratio2.68
---
textmate scopespunctuation.section.embedded.begin.erb
meta.embedded.line.erb
text.html.erbforeground`punctuation.section.embedded.begin.erb{ "foreground": "#5F594F" }`
</pre>

## Results (paraphrased):

### With Reasoning

It's clear, try `complete.madeup.config`

### Without Reasoning

try `"editor.semanticHighlighting.enabled": false` (bingo)


## Takeaways

- If I tell the model exactly what to do, I set reasoning to None, I don't need it second guessing me, and I want to see it finish it's work fast.  

- Telling models exactly what to do is often an anti-pattern and implies I ran a Plan mode that failed. It's probably better to revert the plan session's commits, revise the plan, or ignore whatever problem I have with the code.  If that doesn't apply, then I should just be familiar enough with the code base to make the change manually anyway.  
