from collections import defaultdict
from .outcomes import trials
def summary(db, known_at):
    groups=defaultdict(list)
    for row in trials(db,known_at):
        if row.get('status'):continue
        groups[(row['model'],row['scenario'])].append(row)
    return [{'model':model,'scenario':scenario,'attempts':len(items),'successes':sum(bool(r['success']) for r in items)} for (model,scenario),items in sorted(groups.items())]
