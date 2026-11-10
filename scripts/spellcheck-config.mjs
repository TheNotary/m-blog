import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { parse, printParseErrorCode } from "jsonc-parser";

// Loaded explicitly by the CLI, not discovered by the VS Code extension.
// The extension must write overrides to its editable workspace settings.
const errors = [];
const settings = parse(
  readFileSync(new URL("../.vscode/settings.json", import.meta.url), "utf8"),
  errors,
  { allowTrailingComma: true },
);

if (errors.length) {
  throw new Error(
    `Invalid VS Code settings: ${errors.map(({ error }) => printParseErrorCode(error)).join(", ")}`,
  );
}

export default {
  version: "0.2",
  globRoot: fileURLToPath(new URL("../", import.meta.url)),
  ...Object.fromEntries(
    Object.entries(settings)
      .filter(([key]) => key.startsWith("cSpell."))
      .map(([key, value]) => [key.slice("cSpell.".length), value]),
  ),
};