import ranges
from check_cards import helper_check

labels = ranges.parse_range('22+')
labels_2 = ranges.parse_range("22+, ATs+, KQo")

if __name__ == "__main__":
    
    check_1 = len(ranges.COMBO_MAP)
    check_2 = sum(len(v) for v in ranges.COMBO_MAP.values())
    check_3 = len(ranges.parse_range('22+'))
    check_4 = len(ranges.labels_to_combos(labels))
    check_5 = len(ranges.parse_range("ATs+"))
    check_6 = len(ranges.parse_range("AKs+"))
    check_7 = len(ranges.parse_range("22+, ATs+, KQo"))
    check_8 = len(ranges.labels_to_combos(labels_2))
    check_9 = ranges.get_chart('UTG','vs_rfi')
    check_10 = ranges.get_chart('BB','rfi')

    summary = []

    summary.append(helper_check(169,check_1,"Combo Map Key check"))
    summary.append(helper_check(1326,check_2,"Combo Map Value check"))
    summary.append(helper_check(13,check_3,"Parse Range Check"))
    summary.append(helper_check(78,check_4,"Label to combo check"))
    summary.append(helper_check(4,check_5,"Parse Range Check 1"))
    summary.append(helper_check(1,check_6,"Parse Range Check 2"))
    summary.append(helper_check(18,check_7,"Parse Range Check 3"))
    summary.append(helper_check(106,check_8,"Label Combo Check 2"))
    summary.append(helper_check('No UTG chart for this action.',check_9,"Get Range Check 1"))
    summary.append(helper_check('No BB chart for this action.',check_10,"Get Range Check 2"))

    print(f'Equity Test: {sum(summary)} of {len(summary)} passed!')