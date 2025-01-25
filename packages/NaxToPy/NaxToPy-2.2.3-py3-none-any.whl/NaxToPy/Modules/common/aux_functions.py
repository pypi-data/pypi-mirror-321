from NaxToPy.Core.N2PModelContent import N2PModelContent
from NaxToPy import N2PLog
import numpy as np
from NaxToPy.Core.Classes.N2PElement import *
from NaxToPy.Modules.common.material import *

def get_n2pmaterials_iso(model: N2PModelContent, element_list: list[N2PElement]) -> dict:
    """
    Function which creates a dictionary that relates the element with the n2pmaterial
    and filters out elements that trigger warnings from the original element_list.
    """
    elem_material_dict = {}
    valid_elements = []  # List to store elements that don't trigger warnings

    for i in range(len(element_list)):
        id_prop = element_list[i].Prop
        prop = model.PropertyDict[id_prop]

        if prop.PropertyType == 'PSHELL':
            material_id = prop.MatMemID
            n2pmat = model.MaterialDict[material_id]

            if n2pmat.MatType in ['MAT1', 'ISOTROPIC']:
                elem_material_dict[(element_list[i].ID, element_list[i].PartID)] = n2pmat
                valid_elements.append(element_list[i])  # Add valid element to the list
            else:
                N2PLog.Warning.W651((element_list[i].ID, element_list[i].PartID))
        elif model.Solver == 'Abaqus':
            material_id = prop.MatID
            n2pmat = model.MaterialDict[material_id]

            if n2pmat.MatType in ['ISOTROPIC']:
                elem_material_dict[(element_list[i].ID, element_list[i].PartID)] = n2pmat
                valid_elements.append(element_list[i])  # Add valid element to the list
            else:
                N2PLog.Warning.W651((element_list[i].ID, element_list[i].PartID))

        else:
            N2PLog.Warning.W652((element_list[i].ID, element_list[i].PartID))
    
    # Replace the original element list with the filtered one
    element_list[:] = valid_elements

    return elem_material_dict

def get_np_array_from_result(model,result, element_map:dict, component_map: dict):
    """
    Processes the results array and returns the processed data and necessary mappings.   
    """

    # Create the aux variable which helps with the lecture of results
    aux = 0 if len(result.Body[0]) - len(component_map) == 4 else 1

    # Determine the order of indices based on component_map
    header_order = [list(result.Headers).index(header) for header in component_map.keys()]

    data = []

    # Process each row in the result.Body
    for row in result.Body:
        load_case = int(row[0])  # Load Case ID
        increment_id = int(row[1])
        element_id = int(row[3])  # Element ID
        part_id = str(row[4]) if aux == 1 else model.Parts[0]

        if (element_id, part_id) not in element_map:
            element_map[(element_id, part_id)] = len(element_map)

        # Create a row combining mapping values and component values
        row_data = [
            load_case,
            increment_id,
            element_map[(element_id, part_id)]
        ]

        # Add component values in the specified order
        for i in header_order:
            component_value = float(row[i])
            row_data.append(component_value)

        # Append the complete row to the data array
        data.append(row_data)

    # Convert the data list into a NumPy array
    data_array = np.array(data)
    return data_array


        

# Uso general para todos los módulos -----------------------------------------------------------------------------------
def get_n2pmaterials_general(model: N2PModelContent, element_list: list[N2PElement]) -> dict:
    """
    Function which creates a dictionary that relates the element with the n2pmaterial
    and filters out elements that trigger warnings from the original element_list.
    """
    elem_material_dict = {}
    for i in range(len(element_list)):
        id_prop = element_list[i].Prop
        prop = model.PropertyDict[id_prop]

        if prop.PropertyType == 'PSHELL':
            material_id = prop.MatMemID
            n2pmat = model.MaterialDict[material_id]
            elem_material_dict[(element_list[i].ID, element_list[i].PartID)] = n2pmat

        elif prop.PropertyType == 'PCOMP':
            material_id = prop.MatID
            n2pmat = model.MaterialDict[material_id]
            elem_material_dict[(element_list[i].ID, element_list[i].PartID)] = n2pmat
    
    return elem_material_dict

def elem_to_material(model: N2PModelContent, element_list: list[N2PElement], onlyisotropic: bool =  False) -> dict:
    elem_to_mat = {}
    materials = []
    n2pmaterials = []
    if onlyisotropic == False:
        elem_to_n2pmat = get_n2pmaterials_general(model,element_list)
    else:
        elem_to_n2pmat = get_n2pmaterials_iso(model,element_list)

    for elem_id, n2pmaterial in elem_to_n2pmat.items():
            if elem_id in elem_to_mat:
                continue 
            
            # Verify if the material exists ----------------------------------------------------------------------------
            material_instance = next(
                (material for material in materials if material.N2PMaterial_original.ID == n2pmaterial.ID),
                None
            )

            # If the material does not exist ---------------------------------------------------------------------------
            if material_instance is None:
                # Create a new material and add to the list
                if n2pmaterial.MatType in ['MAT1', 'ISOTROPIC']:
                    material_instance = Isotropic(n2pmaterial)
                    if not hasattr(material_instance, "Allowables"):
                        material_instance.Allowables = AllowablesISO()
                elif n2pmaterial.MatType in ['MAT2', 'ORTHOTROPIC']:
                    material_instance = Orthotropic(n2pmaterial)
                    if not hasattr(material_instance, "Allowables"):
                        material_instance.Allowables = AllowablesORTO()
                # Add the materials to each list
                n2pmaterials.append(n2pmaterial)
                materials.append(material_instance)
            
            # Asociate the element to the material even if is old or new
            elem_to_mat[elem_id] = material_instance
            
            # Update the dictionary of elements to n2pmaterial
            # self._elem_to_n2pmat[elem_id] = n2pmaterial
        
    return elem_to_mat, elem_to_n2pmat, materials, n2pmaterials
# ----------------------------------------------------------------------------------------------------------------------