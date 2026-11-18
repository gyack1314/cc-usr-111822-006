from .evidence import at
def definitions(db, known_at):
    return {row['id']:{**row['payload'],'source':row['digest']} for row in at(db,'scenario',known_at)}
