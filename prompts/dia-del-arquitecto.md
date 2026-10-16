# Día del Arquitecto — ilustración editorial (rompecabezas de Colombia)

- Modelo: `gemini-3.1-flash-image-preview` (Nano Banana 2)
- Aspect ratio: `4:5` · imageSize: `2K` · thinking: `high`
- Modo: Editorial / ilustración de línea (plano arquitectónico)

## Comando

```bash
export GOOGLE_AI_API_KEY=...   # https://aistudio.google.com/apikey
python3 .claude/skills/banana/scripts/generate.py \
  --aspect-ratio 4:5 --resolution 2K --thinking high \
  --prompt "$(sed -n '/^## Prompt/,$p' prompts/dia-del-arquitecto.md | tail -n +3)"
```

## Prompt

A vertical editorial illustration in clean architectural line drawing style, like a precise technical blueprint plotted with a fine pen on pure flat white paper, for an architecture magazine feature in the spirit of Monocle and Wallpaper* editorial graphics. STRICT THREE-COLOR PALETTE: pure white background, thin uniform black lines, and ONE intense vivid red (#E10600). Every surface is flat white; all forms are defined only by crisp, even-weight black linework — flat, shadowless, gradient-free, texture-free, vector-clean.

SUBJECT: a 3×3 jigsaw puzzle seen straight on, front elevation, its interlocking tabs and blanks outlined with thin even black lines. Each piece holds a fragment of an architectural elevation or plan from a different region of Colombia, drawn only in black line like a construction drawing:
- Top-left: Bogotá — red-brick apartment towers drawn as brick coursing lines, with the outline of the Andean eastern hills (Monserrate) behind.
- Top-center: Cartagena — colonial facades with wooden balconies and a church bell tower.
- Top-right: EMPTY SLOT — the missing piece; the hole is filled with fine parallel diagonal hatching lines.
- Middle-left: Pacific coast — a stilt house (palafito) on wooden posts above rippling water lines.
- CENTER: a fine orthogonal street grid of tiny city blocks. Within this grid, the streets become dense and turn intense RED, and that red density forms the silhouette of a simplified anatomical human heart with the vena cava and aorta rising upward. The heart is recognizable ONLY through the color shift of the street lines from black to red — the heart silhouette has no outline stroke, and it MUST look like a real anatomical heart, never a symmetrical valentine heart. Around the red heart the grid continues as lighter, sparser black lines.
- Middle-right: Llanos — a round thatched maloca with a single palm tree.
- Bottom-left: Santander — a stone church with ashlar block lines.
- Bottom-center: Medellín — houses stepped up a steep hillside, with a cable-car gondola line crossing above.
- Bottom-right: Caribbean islands (San Andrés) — a wooden clapboard house with a porch and coconut palms.

ACTION: above the empty top-right slot, the missing piece floats slightly tilted, showing a bahareque coffee-region house (Eje Cafetero) with a clay-tile roof and wooden balcony. A simple line-drawn hand entering from the upper right, seen from above, pinches the piece between thumb and index finger, about to place it. A dotted black arrow curves from the floating piece down into the hatched hole.

In the upper-left margin, a triangular architect's scale ruler (escalímetro) drawn in black line with fine tick marks lies diagonally, as a symbol of the profession.

COMPOSITION: puzzle centered horizontally in the upper four-fifths of the frame with generous white margins on all sides; balanced and airy. The bottom fifth of the canvas MUST be completely empty plain white space reserved for later typography. Red appears ONLY in the center piece's heart. NEVER include any letters, numbers, labels, logos, signatures or watermarks anywhere — the scale ruler carries only unlabeled tick marks.
