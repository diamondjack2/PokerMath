# Module 4: Ranges. 🃏

**Status**: Completed ✅

### Range Notation
Poker ranges are written in shorthand: `"22+, ATs+, KQo"`. `parse_range()` expands that
into the set of hand labels it describes — here 18 of them, from `22` through `AA`,
plus `ATs` through `AKs`, plus `KQo`.

The `+` means two different things. On a pair it walks up: `22+` is every pocket pair
from 22 to AA. On an unpaired hand the high card stays fixed and the kicker climbs:
`ATs+` is `ATs, AJs, AQs, AKs`.

`labels_to_combos()` turns those labels into actual card combinations using `COMBO_MAP`,
an index built once at import that maps each of the 169 labels to its 4, 6, or 12 combos.

### Charts
`charts.py` holds the preflop charts — 6-max, 100bb, three actions: raise first in,
facing a raise, and facing a 3-bet. Each chart has a `raise` string of pure actions and
a `mixed` dict of hands played more than one way, with their frequencies.

`get_chart(position, action)` returns the right one. Two combinations don't exist:
UTG can't face a raise (it acts first), and BB can't raise first in (the hand is over).

### Verification
`check_ranges.py` checks 10 values — the combo index totals 169 labels and 1326 combos,
and the parser expands each notation form to the right label and combo counts.

### How to run
Simply run `python check_ranges.py` to verify that each of the 10 values passes.

