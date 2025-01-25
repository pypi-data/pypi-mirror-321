from rdfcrate import AttachedCrate, uris
from rdflib import Literal, URIRef

AttachedCrate(".").add_entity(URIRef("#instructions"), [uris.HowTo], [
    (uris.step, Literal("Put bread on plate")),
    (uris.step, Literal("Add vegemite"))
])
