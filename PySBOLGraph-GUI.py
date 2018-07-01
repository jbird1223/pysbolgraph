from pysbolgraph.SBOL2Graph import SBOL2Graph as s2g
from pysbolgraph.terms import Biopax, SBOL2
import tkinter as tk



def loadSBOL(doc_name):
    doc_obj = s2g()
    s2g.load(doc_obj,doc_name)
    return(doc_obj)

def getAllCompDefObjs(doc_obj):
    return(doc_obj.component_definitions)

def getCompDefsDisplayId(cd_obj):
    cdDisps = []
    for i in cd_obj:
        cdDisps.append(i.display_id)
    return(cdDisps)

def getCompDefsName(cd_obj):
    cdNames = []
    for i in cd_obj:
        cdNames.append(i.name)
    return(cdNames)

def getCompDefsPersisentIdentities(cd_obj):
    cdPersistId = []
    for i in cd_obj:
        cdPersistId.append(i.persistent_identity)
    return(cdPersistId)

def getCompDefsRoles(cd_obj):
    cdRoles = []
    for i in cd_obj:
        cdRoles.append(i.roles)
    return(cdRoles)

def getCompDefsTypes(cd_obj):
    cdTypes = []
    for i in cd_obj:
        cdTypes.append(i.types)
    return(cdTypes)

def getCompDefsSequences(cd_obj):
    cdSeq = []
    cdSeqObjs = []
    for i in cd_obj:
        cdSeqObjs.append(i.sequences)
    n = 0
    for j in cdSeqObjs:
        if len(j) > 0:
            cdSeq.append([])
            for k in j:
                cdSeq[n].append(k.elements)
        else:
            cdSeq.append("No Sequence")
        n += 1
    return(cdSeq)

def getCompDefsComponents(cd_obj):
    cdComp = []
    cdCompObjs = []
    for i in cd_obj:
        cdCompObjs.append(i.components)
    n = 0
    for j in cdCompObjs:
        if len(j) > 0:
            cdComp.append([])
            for k in j:
                cdComp[n].append([k.display_id,k.display_name,k.persistent_identity,k.definition.uri])
        else:
            cdComp.append("No Components")
        n += 1
    return(cdComp)

def getAllCompDefProperties(cd_obj):
    compDefProps = []
    for i in cd_obj:
        compDefProps.append([
        getCompDefsName([i]),
        getCompDefsDisplayId([i]),
        getCompDefsPersisentIdentities([i]),
        getCompDefsTypes([i]),
        getCompDefsRoles([i]),
        getCompDefsSequences([i]),
        getCompDefsComponents([i])
        ])
    return(compDefProps)


def getAllModDefObjs(doc_obj):
    return(doc_obj.module_definitions)

def getModDefsDisplayId(cd_obj):
    cdDisps = []
    for i in cd_obj:
        cdDisps.append(i.display_id)
    return(cdDisps)

def getModDefsName(cd_obj):
    cdNames = []
    for i in cd_obj:
        cdNames.append(i.display_name)
    return(cdNames)

def getModDefsPersisentIdentities(cd_obj):
    cdPersistId = []
    for i in cd_obj:
        cdPersistId.append(i.persistent_identity)
    return(cdPersistId)

def getModDefsRoles(cd_obj):
    cdRoles = []
    for i in cd_obj:
        cdRoles.append(i.roles)
    return(cdRoles)

def getModDefsModules(cd_obj):
    cdMod = []
    cdModObjs = []
    for i in cd_obj:
        cdModObjs.append(i.modules)
    n = 0
    for j in cdModObjs:
        if len(j) > 0:
            cdMod.append([])
            for k in j:
                cdMod[n].append([k.display_id,k.display_name,k.persistent_identity,k.definition.uri])
        else:
            cdMod.append("No Modules")
        n += 1
    return(cdMod)

def getAllModDefProperties(cd_obj):
    compDefProps = []
    for i in cd_obj:
        compDefProps.append([
        getModDefsName([i]),
        getModDefsDisplayId([i]),
        getModDefsPersisentIdentities([i]),
        getModDefsModules([i])
        ])
    return(compDefProps)
