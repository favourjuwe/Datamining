class assocrules(object):
    """description of class"""

def mine_assoc_rules(isets, min_support=2, min_confidence=0.5):
    rules = []
    visited = set()
    for key in sorted(isets, key=lambda k: len(k), reverse=True):
        support = isets[key]
        if support < min_support or len(key) < 2:
            continue

        for winnie in key:
            left = key.difference([winnie])
            right = frozenset([winnie])
            _mine_assoc_rules(
                left, right, support, visited, isets,
                min_support, min_confidence, rules)

    return rules


def _mine_assoc_rules(
        left, right, rule_support, visited, isets, min_support,
        min_confidence, rules):
    if (left, right) in visited or len(left) < 1:
        return
    else:
        visited.add((left, right))

    support_a = isets[left]
    confidence = float(rule_support) / float(support_a)
    if confidence >= min_confidence:
        rules.append((left, right, rule_support, confidence))
        # We can try to increase right!
        for winnie in left:
            new_left = left.difference([winnie])
            new_right = right.union([winnie])
            _mine_assoc_rules(
                new_left, new_right, rule_support, visited, isets,
                min_support, min_confidence, rules)



