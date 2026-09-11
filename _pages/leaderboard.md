---
title: "Leaderboard"
permalink: /leaderboard/
layout: single
author_profile: false
---

<iframe
  id="leaderboard-plot"
  title="SAPS runtime performance profile"
  src="{{ '/assets/leaderboard/index.html' | relative_url }}"
  width="100%"
  height="800"
  style="display: block; border: 0;"
></iframe>

<script>
  const plot = document.getElementById("leaderboard-plot");
  plot.addEventListener("load", () => {
    const body = plot.contentDocument.body;
    const resize = () => { plot.style.height = `${body.scrollHeight + 32}px`; };
    new ResizeObserver(resize).observe(body);
    resize();
  });
</script>
