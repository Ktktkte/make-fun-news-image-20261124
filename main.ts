// news-image-20261124 — copies the front page image to the output directory.
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { mkdirSync, copyFileSync, existsSync, readFileSync } from "node:fs";

const here = dirname(fileURLToPath(import.meta.url));
const imagePath = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

if (!existsSync(imagePath)) {
  console.error("entry.png not found next to main.ts");
  process.exit(1);
}

// Sanity check: the file must really be a PNG before we hand it to the grader.
const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!readFileSync(imagePath).subarray(0, 8).equals(PNG_SIGNATURE)) {
  console.error("entry.png is not a valid PNG");
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(imagePath, join(outDir, "entry.png"));
