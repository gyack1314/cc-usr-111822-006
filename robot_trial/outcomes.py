from .evidence import at
from .scenarios import definitions
def trials(db, known_at):
    scenarios=definitions(db,known_at);out=[]
    for row in at(db,'trial',known_at):
        p=row['payload'];scenario=scenarios.get(p['scenario'])
        if not scenario:out.append({'trial':row['id'],'status':'场景待核'});continue
        out.append({'trial':row['id'],'scenario':p['scenario'],'model':p['model'],'task':scenario['task'],'difficulty':scenario['difficulty'],'success':p['success'],'source':row['digest'],'scenario_source':scenario['source']})
    return out
