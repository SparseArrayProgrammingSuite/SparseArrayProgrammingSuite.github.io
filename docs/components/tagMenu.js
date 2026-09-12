// A collapsible checkbox group that behaves as an Observable Framework
// custom input: it exposes a `value` property (the checked tags) and
// dispatches an "input" event whenever that value changes, so it can be
// used directly with `view(tagMenu(...))`.
export function tagMenu(tags, {
  label = "",
  value = [],
  groupOf = () => "",
  groupOrder = [""]
} = {}) {
  const selected = new Set(value);

  const details = document.createElement("details");
  details.className = "saps-tag-menu";

  const summary = document.createElement("summary");
  summary.textContent = label;
  details.append(summary);

  const panel = document.createElement("div");
  panel.className = "saps-tag-menu__panel";
  details.append(panel);

  const groups = new Map(groupOrder.map((name) => [name, []]));
  for (const tag of tags) {
    const name = groupOf(tag);
    if (!groups.has(name)) groups.set(name, []);
    groups.get(name).push(tag);
  }

  const inputs = [];
  for (const [name, groupTags] of groups) {
    if (!groupTags.length) continue;
    const section = document.createElement("div");
    section.className = "saps-tag-menu__section";
    if (name) {
      const heading = document.createElement("div");
      heading.className = "saps-tag-menu__section-label";
      heading.textContent = name;
      section.append(heading);
    }
    for (const tag of groupTags) {
      const item = document.createElement("label");
      const input = document.createElement("input");
      input.type = "checkbox";
      input.value = tag;
      input.checked = selected.has(tag);
      input.addEventListener("change", () => details.dispatchEvent(new Event("input", {bubbles: true})));
      item.append(input, document.createTextNode(tag));
      section.append(item);
      inputs.push(input);
    }
    panel.append(section);
  }

  Object.defineProperty(details, "value", {
    get() {
      return inputs.filter((input) => input.checked).map((input) => input.value);
    },
    set(newValue) {
      const set = new Set(newValue);
      for (const input of inputs) input.checked = set.has(input.value);
    }
  });

  return details;
}
