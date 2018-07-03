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

def prettyPrintAllCompDefs(doc_obj): #Takes SBOL document object
    cds = getAllCompDefObjs(doc_obj)
    cdPro = getAllCompDefProperties(cds)
    for i in cdPro:
        print("dcterms:Title:\t", i[0], "\ndisplayId:\t", i[1], "\npersistentIdentity:\t", i[2], "\nType:\t", i[3], "\nRole:\t", i[4],"\nSequences:\t", i[5], "\nComponents:\t", i[6], "\n\n")

def getAllModDefObjs(doc_obj):
    return(doc_obj.module_definitions)

def getModDefsDisplayId(md_obj):
    cdDisps = []
    for i in md_obj:
        cdDisps.append(i.display_id)
    return(cdDisps)

def getModDefsName(md_obj):
    cdNames = []
    for i in md_obj:
        cdNames.append(i.display_name)
    return(cdNames)

def getModDefsPersisentIdentities(md_obj):
    cdPersistId = []
    for i in md_obj:
        cdPersistId.append(i.persistent_identity)
    return(cdPersistId)

def getModDefsRoles(md_obj):
    cdRoles = []
    for i in md_obj:
        cdRoles.append(i.roles)
    return(cdRoles)

def getModDefsModules(md_obj):
    cdMod = []
    cdModObjs = []
    for i in md_obj:
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

def getModDefsFuncComps(md_obj):
    cdFuncComps = []
    cdFuncCompsObjs = []
    for i in md_obj:
        cdFuncCompsObjs.append(i.functional_components)
    n = 0
    for j in cdFuncCompsObjs:
        if len(j) > 0:
            cdFuncComps.append([])
            for k in j:
                cdFuncComps[n].append([k.display_id,k.display_name,k.persistent_identity,k.definition.uri])
        else:
            cdFuncComps.append("No FunctionalComponents")
        n += 1
    return(cdFuncComps)

def getAllModDefProperties(md_obj):
    compDefProps = []
    for i in md_obj:
        compDefProps.append([
        getModDefsName([i]),
        getModDefsDisplayId([i]),
        getModDefsPersisentIdentities([i]),
        getModDefsRoles([i]),
        getModDefsModules([i]),
        getModDefsFuncComps([i])
        ])
    return(compDefProps)

def prettyPrintAllModDefs(doc_obj): #Takes SBOL document object
    mds = getAllModDefObjs(doc_obj)
    mdPro = getAllModDefProperties(mds)
    for i in mdPro:
        print("dcterms:Title:\t", i[0], "\ndisplayId:\t", i[1], "\npersistentIdentity:\t", i[2], "\nRole:\t", i[3], "\nModules:\t", i[4], "\nFunctionalComponents:\t", i[5], "\n\n")
