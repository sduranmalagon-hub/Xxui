# Día del Arquitecto — v2 (dirección de arte refinada, A en el centro)

- Modelo: `gemini-3.1-flash-image-preview` · 4:5 · 2K · thinking high

## Prompt

A vertical editorial poster illustration in refined architectural line drawing style, like a precise pen-plotted construction drawing on pure flat white paper, art-directed for the cover of an architecture society's anniversary publication in the spirit of Wallpaper* and Monocle editorial graphics. STRICT THREE-COLOR PALETTE: flat pure white, black linework, and ONE intense vivid red (#E10600). Everything is flat, crisp and vector-clean, with perfectly even strokes.

LINE HIERARCHY: the puzzle outline uses a confident medium black stroke; all architectural drawings inside the pieces use one consistent fine hairline stroke at the same drawing scale, all standing on a shared ground line at the same height within each row, so the nine pieces read as one coherent set of elevations. Generous white space inside each piece around each drawing.

SUBJECT: a perfectly square 3×3 jigsaw puzzle seen straight on, with neat, symmetrical, evenly sized interlocking tabs. Pieces, drawn ONLY in black line:
- Top-left: Bogotá — brick apartment towers with brick coursing drawn in fine BLACK lines, the Monserrate hill silhouette behind.
- Top-center: Cartagena — colonial facades with wooden balconies and a church bell tower.
- Top-right: EMPTY SLOT filled with fine evenly spaced 45° hatching.
- Middle-left: Pacific — a stilt house on wooden posts over calm horizontal water lines.
- CENTER: a fine orthogonal street grid of small city blocks across the whole piece. Within the grid, a set of streets turns intense RED and thickens slightly, and those red streets construct a large, perfectly symmetrical, geometric capital letter A: two straight diagonal legs meeting at a sharp apex like a gable roof, and a clear horizontal crossbar, centered in the piece and filling about 70% of its height. The A is built ONLY from red street lines of the grid, with no outline around it; the rest of the grid stays fine black hairlines. This red A is the single focal point of the whole poster.
- Middle-right: Llanos — a round thatched maloca beside one moriche palm.
- Bottom-left: Santander — a stone church with ashlar coursing.
- Bottom-center: Medellín — houses stepped up a steep hillside, a cable-car line with one gondola crossing above.
- Bottom-right: San Andrés — a wooden clapboard house with a porch between two coconut palms.

ACTION: above the empty top-right slot, the missing piece floats tilted about 12°, showing a coffee-region bahareque house with clay-tile roof and wooden balcony. A simple elegant hand drawn in clean single-weight black outline enters from the top-right edge, seen from above, pinching the piece between thumb and index finger. A smooth dotted black arc arrow leads from the floating piece into the hatched slot.

In the upper-left margin, a triangular architect's scale ruler drawn in clean black line with fine unlabeled tick marks lies at about 30°, balancing the hand diagonally across the top.

COMPOSITION: the puzzle is centered horizontally with equal generous white margins left and right, and sits in the upper part of the frame; the ruler and hand occupy the top margin as a balanced diagonal pair. The bottom 22% of the canvas MUST be completely empty plain white, reserved for typography. Red appears ONLY in the letter A of the center piece; everything else is black on white. The A MUST be the only letter in the image — NEVER include any other letters, numbers, words, logos, signatures or watermarks.

## Post-producción aplicada

1. Flecha punteada redibujada a mano (PIL): ahora sale junto a la pieza flotante y entra en el hueco rayado.
2. Lienzo ampliado para que la franja blanca inferior ocupe el 22 % del alto, manteniendo 4:5 (1856×2304).
3. Outpainting con Gemini para prolongar el escalímetro y el antebrazo hasta los bordes.
4. Fondo normalizado a blanco puro (#FFFFFF).
