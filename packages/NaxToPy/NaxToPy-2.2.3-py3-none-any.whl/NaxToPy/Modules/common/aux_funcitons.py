from NaxToPy.Core.N2PModelContent import N2PModelContent
from NaxToPy import N2PLog
from typing import Union

def get_n2pmaterials (model: N2PModelContent, id_element: Union[tuple[int, str], list, int] = 0) -> dict:

    elem_material_dict = {}

    for i in range(len(id_element)):

        id = id_element[i]

        n2pelem = model.get_elements([id])

        id_prop = n2pelem[0].Prop

        prop = model.PropertyDict[id_prop]

        if prop.PropertyType == 'PSHELL':
            material_id = prop.MatMemID

            n2pmat = model.MaterialDict[material_id]

            if n2pmat.MatType in ['MAT1','ISOTROPIC']:
                elem_material_dict[id] = n2pmat
            else:
                N2PLog.Warning.W651(id)
        else:
            N2PLog.Warning.W652(id)

    return elem_material_dict