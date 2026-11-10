---
date: 2026-11-10
slug: the-rg-tool-a-better-grep
---

# The rg tool, a better grep

A few weeks while working with a client, I noticed an agent attempting to use the `rg` tool which consistently failed because...

<!-- more -->

What the heck is `rg` anyway?  

Neither of us had seen it before, and it's strange seeing a linux command that's shorter than 3 characters.  We shrugged, figuring it's just robots being weird again (and they are sooo weird sometimes).  We must have been on a GPT because today I noticed an attempted `rg` call on my machine with Sol 5.6. I figured reading up on this was now a mandate (what happened to AI freeing up developer time rather than consuming it?).  

Anyway, it turns out `rg` is a better grep that spares you from needing to memorize obscure command line arguments because it just does the actions you want be default.

Run `rg hello` with no arguments, and the string 'hello' is searched recursively from the current working directory.  

<img width="1493" height="807" alt="Image" src="https://github.com/user-attachments/assets/74364536-890d-4236-a0f1-69de12bfaaf7" />

You can pass in a glob and now you can filter your search and don't need to memorize a single switch! 

```sh
rg hello **/{*.py,devtool}
```

My former coding rig made observing commands/ errors difficult, so I get it's not always a simple recommendation to follow, but it's worth taking a look at what commands your agents are attempting --I can see missing utilities leading to slightly more expensive runs, and potentially degraded outcomes.  

