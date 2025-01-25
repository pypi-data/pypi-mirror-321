"""Script for the definition of the class N2PNeuber."""

# Copyright (c) Idaero Solutions.
# Distributed under the terms of the LICENSE file located in NaxToPy-<version>.dist-info.


import scipy
from NaxToPy.Core.N2PModelContent import N2PModelContent
from NaxToPy.Modules.common.aux_functions import *
from NaxToPy.Core.Classes.N2PMaterial import N2PMaterial
from NaxToPy.Core.Classes.N2PElement import *
from NaxToPy.Core.Classes.N2PLoadCase import *
from NaxToPy.Modules.common.material import *
from NaxToPy import N2PLog
from typing import Literal
from collections import defaultdict
from NaxToPy.Modules.common.data_input_hdf5 import DataEntry


class N2PNeuber:

    """
    Class used to obtain stresses using the Neuber method.

    Attributes:
        _model: N2PModelContent -> model to be analyzed. It is a compulsory input and an error will occur if it is not 
        present.
        _element_list: list[N2PElement] -> list of N2PElement obtained from model.get_elements(). It is a compulsory input 
        and an error will occur if it is not present.
        _load_cases_list: list[N2PLoadCase] -> list of N2PLoadCase obtained from model.get_load_case(). It is a compulsory 
        input and an error will occur if it is not present.
        _elem_to_n2pmat: dict -> Dictionary which assigns an N2PMaterial to an individual element.
        _n2pmaterials: list[N2PMaterial] -> list of N2PMaterials.
        _materials: list[Materials] -> list of materials created by each of the N2PMaterial instances.
        _elem_to_mat: dict -> Dictionary which assigns an Material to an individual material.
        _results: np.array -> Array with all the results.
        _neuber_results: np.array -> Array with the neuber results calculated by _results.
        _transformed_data: np.array -> Array with the transformed data which store the valid information for the HDF5 document.
        _component_map: dict -> Dictionary with the component mapping index.
        _element_map: dict -> Dictionary with the element index.
        _section_map: dict -> Dictionary with the section mapping.
        _load_case_number: int = 100 -> Integer which defines the number of load cases to be analyzed per iteration.

    Calling example:
        >>> import NaxToPy as n2p
        >>> from NaxToPy.Modules.N2PNeuber.N2PNeuber import N2PNeuber
        >>> model = n2p.load_model(r"file path")
        >>> element_list = [(24581218, '0')]
        >>> n2pelem = model.get_elements(element_list)
        >>> n2plc = model._load_case(68195)
        >>> neuber = N2PNeuber() 
        >>> neuber.Model = model # compulsory input
        >>> neuber.Element_list = n2pelem # compulsory input
        >>> neuber.LoadCases = n2plc # compulsory input
        >>> neuber.calculate() # neuber stress are calculated
        >>> neuber.get_neuber_result(68195,'VON_MISES', 24581218, '0', 'z1') # neuber result

    """
    def __init__(self) -> None:
        # Mandatory attributes -----------------------------------------------------------------------------------------
        self._model: N2PModelContent = None
        self._element_list: list[N2PElement] = []
        self._load_cases_list: list[N2PLoadCase] = None

        # Materials attributes -----------------------------------------------------------------------------------------
        self._elem_to_n2pmat: dict = None
        self._n2pmaterials: list[N2PMaterial] = None
        self._materials: list[Material] = None
        self._elem_to_mat: dict = None

        # Results attributes -------------------------------------------------------------------------------------------
        self.results = []
        self._neuber_results = []
        self._transformed_data: list[DataEntry] = []
        
        # Mapping attributes -------------------------------------------------------------------------------------------
        self._component_map: dict = {}
        self._element_map:dict = {}
        self._section_map: dict = {}

        # Memory control -----------------------------------------------------------------------------------------------
        self._load_case_number: int = 100
    # ------------------------------------------------------------------------------------------------------------------


    # Getters ----------------------------------------------------------------------------------------------------------
    # Method to obtain the model ---------------------------------------------------------------------------------------
    @property 
    def Model(self) -> N2PModelContent: 
        """
        Property that returns the model attribute, that is, the N2PModelContent to be analyzed. 
        """
        
        return self._model 
    # ------------------------------------------------------------------------------------------------------------------

    # Method to obtain the List of elements which is going to be analyzed ----------------------------------------------
    @property
    def Element_list(self) -> list[N2PElement]:
        """
        Property that returns the list of elements, that is, the list of elements to be analyzed.
        """
        
        return self._element_list
    # ------------------------------------------------------------------------------------------------------------------

    # Method to obtain the load cases ---------------------------------------------------------------------------------
    @property
    def LoadCases(self) -> list[N2PLoadCase]:
        """
        Property that returns the load_cases list, that is, the list of the IDs of the load cases to be analyzed. 
        """

        return self._load_cases_list
    # ------------------------------------------------------------------------------------------------------------------

    # Method to obtain de dictionary of elements to N2PMaterial --------------------------------------------------------
    @property
    def Elem_to_N2PMaterial(self) -> dict:
        """
        Property that returns a dictionary that relates the elements to the N2PMaterial.
        """

        return self._elem_to_n2pmat
    # ------------------------------------------------------------------------------------------------------------------

    # Method to obtain the dictonary of results ------------------------------------------------------------------------
    @property
    def Results(self) -> np.array:
        """
        Property that returns an array that shows all the results.
        """

        return self.results
    # ------------------------------------------------------------------------------------------------------------------

    #Method to obtain the materials asigned to the elements ------------------------------------------------------------
    @property
    def Materials(self) -> list[Material]:
        """
        Property that returns a list of the materials created.
        """

        return self._materials
    # ------------------------------------------------------------------------------------------------------------------

    # Method to obtain de dictionary of elements to Material -----------------------------------------------------------
    @property
    def Elem_to_Material(self) -> dict:
        """
        Property that returns a dictionary that relates the elements to the Material.
        """
        return self._elem_to_mat
    # ------------------------------------------------------------------------------------------------------------------

    # Method to obtain the list od N2PMaterials ------------------------------------------------------------------------
    @property
    def List_N2PMaterials(self) -> list[N2PMaterial]:
        """
        Property that returns the list of N2PMaterials.
        """

        return self._n2pmaterials
    # ------------------------------------------------------------------------------------------------------------------

    # Method to obtain Neuber Results ----------------------------------------------------------------------------------
    @property
    def Neuber_Results(self) -> np.array:
        """
        Property that returns an array of Neuber results.
        """

        return self._neuber_results
    # ------------------------------------------------------------------------------------------------------------------

    # Method to obtain the number of LoadCases to be analyzed in each iteration ----------------------------------------
    @property
    def LoadCase_Number(self) -> int:
        """
        Property that returns the number of LoadCases to be analyzed in each iteration
        """

        return self._load_case_number
    # ------------------------------------------------------------------------------------------------------------------



    # Setters ----------------------------------------------------------------------------------------------------------
    @Model.setter 
    def Model(self, value: N2PModelContent) -> None: 
        self._model = value 
    # ------------------------------------------------------------------------------------------------------------------

    @Element_list.setter
    def Element_list(self, value: list[N2PElement]) -> None:
        if all(isinstance(element, N2PElement) for element in value):
            self._element_list = value
            self._reset_attributes()
            self._elem_to_mat, self._elem_to_n2pmat, self._materials, self._n2pmaterials = elem_to_material(self._model,self._element_list,True)
        else:
            N2PLog.Error.E663()
    # ------------------------------------------------------------------------------------------------------------------

    @LoadCases.setter
    def LoadCases(self, value: list[N2PLoadCase]) -> None:
        if isinstance(value, list):
            self._load_cases_list = value if all(isinstance(lc, N2PLoadCase) for lc in value) else N2PLog.Error.E664()     
        else:
            N2PLog.Error.E664()
    # ------------------------------------------------------------------------------------------------------------------

    @LoadCase_Number.setter
    def LoadCase_Number(self, value:int) -> None:
        self._load_case_number = value
    # ------------------------------------------------------------------------------------------------------------------




    def _reset_attributes(self) -> None:
        """Reset the attributes to their initial values"""
        # Materials attributes -----------------------------------------------------------------------------------------
        self._elem_to_n2pmat: dict = None
        self._n2pmaterials: list[N2PMaterial] = None
        self._materials: list[Material] = None
        self._elem_to_mat: dict = None

        # Results attributes -------------------------------------------------------------------------------------------
        self.results = []
        self._neuber_results = []
        self._transformed_data = []
        
        # Mapping attributes -------------------------------------------------------------------------------------------
        self._component_map: dict = {}
        self._element_map:dict = {}
        self._section_map: dict = {}
    # ------------------------------------------------------------------------------------------------------------------


    def _get_stress_by_elem(self) -> None:
        """
        Retrieves the stress results associated with the elements and stores them in a NumPy array.

        The structure of the resulting array is as follows:
            Results[*Number of the solution*][*Load Case Identifier*, *Increment ID*, *Element Identifier mapped*, 
            *Components*, *Section*]

        Returns:
            self._results: np.array
        """
        # Get the elements ID given by the user which are going to be analyzed -----------------------------------------
        elems = list(self._elem_to_mat.keys())

        # Get the n2pelements associated to the elements ID -------------------------------------------------------------
        n2pelems = self._model.get_elements(elems)

        # Create the input strings necessary to the new_report method----------------------------------------------------
        formatted_parts = [f"<LC{load_case.ID}:FR{load_case.ActiveN2PIncrement.ID}>" for load_case in self._load_cases_list]
        input_string_lc_inc = ",".join(formatted_parts)

        results_type = ['STRESSES', 'S']
        unnecesary_component = set(
            'LAYER,ANGLE_PRINCIPAL,PRINCIPAL_MAJOR,PRINCIPAL_MINOR,MARGIN_SAFETY,'
            'MARGIN_OF_SAFETY_IN_TENSION,MARGIN_OF_SAFETY_IN_COMPRESSION,FIRST_PPAL_STRESS,'
            'FIRST_PPAL_X-COS,SECOND_PPAL_X-COS,THIRD_PPAL_X-COS,MEAN_PRESS,'
            'OCTAHEDRAL_SHEAR_STRESS,SECOND_PPAL_STRESS,FIRST_PPAL_Y-COS,SECOND_PPAL_Y-COS,'
            'THIRD_PPAL_Y-COS,THIRD_PPAL_STRESS,FIRST_PPAL_Z-COS,SECOND_PPAL_Z-COS,'
            'THIRD_PPAL_Z-COS,VON_MISES,FIRST_INVARIANT,SECOND_INVARIANT,THIRD_INVARIANT,'
            'FIBER_DISTANCE,MAXIMUM_PRINCIPAL,MINIMUM_PRINCIPAL,TRESCA_2D,'
            'AXIAL_SAFETY_MARGIN,TORSIONAL_SAFETY_MARGIN'.split(',')
        )

        for result in results_type:
            if result in self._load_cases_list[0].Results.keys():
                input_string_result = result

        # Unique mapping of components by section ----------------------------------------------------------------------
        section_to_components = defaultdict(set)  # Use a set to avoid duplicates.

        for component in self._load_cases_list[0].get_result(input_string_result).Components.keys():
            if component not in unnecesary_component:
                for section in self._load_cases_list[0].get_result(input_string_result).get_component(component).Sections:
                    # Group the component under the section name
                    section_to_components[section.Name].add(component)

        # Create the array of strings where each position corresponds to a section -------------------------------------
        input_component_section_array = []
        mapped_components_array = []  # This will be the array of dictionaries with mappings per section.

        for i, (section_name, components) in enumerate(section_to_components.items()):
            self._section_map[section_name] = i

            # Build the string for this section
            section_string = ",".join([f"<{component}:{section_name}#>" for component in components])
            input_component_section_array.append(section_string)

            # Create the component mapping for this section with reset indexing
            section_component_map = {component: idx for idx, component in enumerate(components)}

            # Add the mapping to the array
            mapped_components_array.append(section_component_map)

        # Assign the mapping to the attribute self._component_map ------------------------------------------------------
        self._component_map = mapped_components_array

        # Initialize a list to accumulate all results ------------------------------------------------------------------
        all_results = []

        # Loop through each section and process results ----------------------------------------------------------------
        for i in range(len(input_component_section_array)):
            result = self._model.new_report(input_string_lc_inc, False, input_string_result, input_component_section_array[i],
                                            False, n2pelems, 'LC')
            result.calculate()

            # Convert result to NumPy array and add section index
            result = get_np_array_from_result(self._model, result,self._element_map, self._component_map[i])
            result_with_section = np.column_stack([result, np.full(result.shape[0], i)])

            # Append the result to the list
            all_results.append(result_with_section)

        # Get the maximum number of columns across all sections --------------------------------------------------------
        max_columns = max(result.shape[1] for result in all_results) - 1  # Temporarily exclude the section column
        max_columns += 1  # Include the section column

        # Create a list of aligned results -----------------------------------------------------------------------------
        all_results_aligned = []

        for i, result in enumerate(all_results):
            num_columns = result.shape[1]

            if num_columns < max_columns:
                # Separate the last column as section
                section_column = result[:, -1].reshape(-1, 1)  # Last column
                main_columns = result[:, :-1]  # All columns except the last

                # Calculate how many columns are missing
                padding = np.full((main_columns.shape[0], max_columns - main_columns.shape[1] - 1), np.nan)

                # Combine main columns, padding, and the section column
                result_aligned = np.hstack([main_columns, padding, section_column])
            elif num_columns == max_columns:
                result_aligned = result

            all_results_aligned.append(result_aligned)

        # Combine all aligned matrices ---------------------------------------------------------------------------------
        new_result = np.vstack(all_results_aligned)
        self.results.append(new_result)
        self.results = np.array(self.results)
        self.results = np.squeeze(self.results)

        
        return None
    # ------------------------------------------------------------------------------------------------------------------




    def get_neuber_result(self, lc: int, component: str, section: str, element_id: int, part_id: str = '0') -> float:
        """
        Retrieves the Neuber method result for a specific load case, stress component, element-part, 
        and section.

        Args:
            lc (int): Identifier of the load case.
            component (str): The stress component to retrieve.
            element_id (int): Identifier of the element.
            part_id (str, optional): Identifier of the part containing the element. Defaults to '0'.
            section (str): Section identifier for filtering results.

        Returns:
            float: The Neuber stress result for the specified parameters.
        """
        # Obtain indices from the maps
        section_index = self._section_map[section]
        component_index = self._component_map[section_index][component]
        element_index = self._element_map[(element_id, part_id)]


        # Filter results in the combined array -------------------------------------------------------------------------
        filtered = self._neuber_results[
            (self._neuber_results[:, 0] == lc) &  # Filter by Load Case
            (self._neuber_results[:, 2] == element_index) &    # Filter by element
            (self._neuber_results[:, -1] == section_index)     # Filter by section (added column)
        ]
        return filtered[0, 3 + component_index]




    def _neuber_method_hsb(self, elastic_stress: float, modulus_e: float, yield_stress: float, exponent_n: float, element: Union[tuple,int]):
        """Solves the Neuber method equation using initial guesses and fsolve.
        
        Args:
            elastic_stress (float): Elastic stress value.
            modulus_e (float): Modulus of elasticity.
            yield_stress (float): Yield stress value.
            exponent_n (float): Strain hardening exponent.
            element (tuple, int): Element identificator
            
        Returns:
            float: Calculated stress value, or None if no solution is found.
        """
        # Define the Ramberg-Osgood equation to solve ------------------------------------------------------------------
        def equation(x):
            return (elastic_stress**2 / modulus_e) - x * ((x / modulus_e) + 0.002 * (x / yield_stress) ** exponent_n)

        # Attempt to solve with different initial guesses --------------------------------------------------------------
        initial_guesses = [0.1, 1, 10, 100, 1000]
        for x0 in initial_guesses:
            try:
                stress_val, = scipy.optimize.fsolve(equation, x0)
                if abs(equation(stress_val)) < 1e-5:  # Ensure solution is close to zero
                    return stress_val
            except ValueError:
                continue
        N2PLog.Error.E665(element)
        return None
    # ------------------------------------------------------------------------------------------------------------------





    def _process_results_as_flat_array(self):
        """
        Processes an array of results and computes corrected values for each stress component.
        Returns a flat NumPy array where each row contains:
            - Load Case
            - Element ID mapped
            - Corrected stress value (All components)
            - Section mapped

        Returns:
            np.ndarray: Processed results array.
        """

        # Iterate through each row in the results array
        for row in self.results:
            # Extract LoadCase, Element_ID, Increment_ID, and Section
            load_case = int(row[0])
            increment_id = int(row[1])
            element_id = int(row[2])
            section = int(row[-1])  # Last column

            # Find the corresponding element and its material properties
            element = next(key for key, value in self._element_map.items() if value == element_id)
            material = self._elem_to_mat[element]
            modulus_e = material.Young
            yield_stress = material.Allowables.Yield_stress
            exponent_n = material.Allowables.RO_exponent

            # Initialize the processed data row
            processed_data = [load_case, increment_id, element_id]

            # Process each stress component
            for i in range(3, len(row) - 1):  # Components are after the first 3 indices and before the section
                component_value = row[i]

                if not np.isnan(component_value):  # Skip NaN values
                    corrected_value = self._neuber_method_hsb(
                        component_value, modulus_e, yield_stress, exponent_n, element
                    )
                else:
                    corrected_value = component_value  # Keep NaN if present

                # Add the corrected value to the row
                processed_data.append(corrected_value)

            # Add the section ID to the row
            processed_data.append(section)

            # Append the processed row to the results
            self._neuber_results.append(processed_data)
        
        self._neuber_results = np.array(self._neuber_results)
        
        return None
    # ------------------------------------------------------------------------------------------------------------------

    def _transform_data(self) -> None:
        """
        Transform the data into DataEntry instances, grouped by section and split by parts.
        """
        
        grouped_data = defaultdict(list)

        # Agrupar datos por LoadCase ID, Increment ID y Section
        for row in self._neuber_results:
            loadcase_id, increment_id, element_id, *components, section = row
            key = (loadcase_id, increment_id, section)
            grouped_data[key].append([element_id, *components])

        # Crear una lista de instancias de DataEntry
        for (loadcase_id, increment_id, section), rows in grouped_data.items():
            # Determinar los nombres de los componentes
            components_list = list(self._component_map[int(section)].keys())
            
            # Crear el dtype para el array estructurado
            components_dtype = np.dtype(
                [('ID_ENTITY', 'i4')] + [(nombre, 'f4') for nombre in components_list]
            )

            # Dividir datos por parte
            part_groups = defaultdict(list)
            for row in rows:
                # Desmapear el elemento
                element_id_mapped = row[0]
                element_key = next(
                    (key for key, value in self._element_map.items() if value == element_id_mapped), 
                    None
                )
                if element_key:
                    part = element_key[1]  # Obtener la parte ('0', '1', etc.)
                    part_groups[part].append(row)
            
            # Crear una instancia de DataEntry para cada parte
            for part, part_rows in part_groups.items():
                entry = DataEntry()
                entry.LoadCase = int(loadcase_id)
                entry.Increment = int(increment_id)
                entry.Section = next((key for key, value in self._section_map.items() if value == section), None)
                
                # Convertir los datos ajustados a un array estructurado
                part_rows = np.array(part_rows)
                num_fields = len(components_dtype)
                data_adjusted = part_rows[:, :num_fields]
                data_adjusted[:, 0] = data_adjusted[:, 0].astype('i4')
                
                entry.Data = np.array([tuple(row) for row in data_adjusted], dtype=components_dtype)
                entry.ResultsName = 'RESULTS_NEUBER'
                entry.PartName = part

                self._transformed_data.append(entry)

        return self._transformed_data

            



    def calculate(self) -> None:
        """
        Executes all necessary calculations as the final step in the workflow.

        Returns:
            None
        """
        # Check if all the inputs are given by the user ----------------------------------------------------------------
        for pos, material in enumerate(self._materials):
            if material.Allowables.Yield_stress == None:
                return N2PLog.Error.E661(material.ID)
            if material.Allowables.RO_exponent == None:
                return N2PLog.Error.E662(material.ID)

        # Calculate the final result -----------------------------------------------------------------------------------
        num_total_load_cases = len(self._load_cases_list)
        num_lc_per_it = self.LoadCase_Number
        self._get_stress_by_elem()
        init_val = self._load_cases_list
        for i in range(num_total_load_cases//num_lc_per_it):
            loadcases_it = self._load_cases_list[i*num_lc_per_it: (i+1)*num_lc_per_it]
            self._load_cases_list = loadcases_it
            self._process_results_as_flat_array()
            self._transform_data()
        if (num_total_load_cases//num_lc_per_it)*num_lc_per_it != num_total_load_cases:
            loadcases_it = self._load_cases_list[num_lc_per_it*(num_total_load_cases//num_lc_per_it):num_total_load_cases]
            self._load_cases_list = loadcases_it
            self._process_results_as_flat_array()
            self._transform_data()
        self._load_cases_list = init_val
    # ------------------------------------------------------------------------------------------------------------------


    # def reserve_factor_calculation_stress_strain_law(elastic_stress,e_modulus, neuber_allowable_strain, proof_stress, index):
    #     """Calculates the reserve factor usign elastic-perfectly plastic stress-strain law

    #     Args:
    #         elastic_stress (float): Elastic stress value.
    #         e_ modulus (float): Modulus of elasticity.
    #         neuber_allowable_strain (float): Neuber allowable strain value.
    #         proof_stress (float): Proof stress value.

    #     Returns:
    #         float: Calculated reserve factor.
    #     """

    #     reserve_factor = ((neuber_allowable_strain*proof_stress*e_modulus+proof_stress**2)**0.5)/(elastic_stress)

    #     print(f"Calculated Neuber Reserve Factor for the problem {index + 1} usig elastic-perfectly plastic stress-strain law is: {round(reserve_factor, 2)}")
    #     if reserve_factor < 1:
    #         print("Warning: The Neuber Reserve Factor is less than 1")
        
    #     return reserve_factor
