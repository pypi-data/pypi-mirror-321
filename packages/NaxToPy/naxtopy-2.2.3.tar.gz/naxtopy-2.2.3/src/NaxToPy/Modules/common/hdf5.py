from NaxToPy.Core.Constants import Constants
from NaxToPy.Modules.common.data_input_hdf5 import DataEntry
from NaxToPy import N2PLog
import h5py 
import time 
import os 
from typing import Union
import io

class HDF5_NaxTo: 

    # H5F5 constructor ------------------------------------------------------------------------------------------------- 
    def __init__(self): 

        """
        Class that represents one .HDF5 file. 

        Attributes: 
            file: HDF5 file created, either in disk or in memory. 
            memory_file_boolean: bool = True -> boolean that shows if the file is created in disk or in memory. 
            file_path: str -> path in which the file will be created in disk. 
            file_description: str -> file description. 

        The file is structured in the following way: 
            File -> NaxTo -> Results -> Load Case -> Increment -> Results Name -> Section -> Data dataset (a different
        dataset is created for each part). 
        """
        self._file = None
        self._memory_file_boolean: bool = True
        self._file_path: str = None 
        self._file_description: str = None 
    # ------------------------------------------------------------------------------------------------------------------
    
    # Getters ----------------------------------------------------------------------------------------------------------
    @property
    def FilePath(self) -> str: 
        return self._file_path 
    # ------------------------------------------------------------------------------------------------------------------
    
    @property 
    def FileDescription(self) -> str: 
        return self._file_description
    # ------------------------------------------------------------------------------------------------------------------

    @property
    def File(self):
        return self._file
    # ------------------------------------------------------------------------------------------------------------------

    @property
    def MemoryFile(self) -> bool:
        return self._memory_file_boolean
    # ------------------------------------------------------------------------------------------------------------------


    
    # Setters ----------------------------------------------------------------------------------------------------------
    @FilePath.setter 
    def FilePath(self, value: str) -> None: 
        if type(value) == str: 
            self._file_path = value
            self._memory_file_boolean = False
        else: 
            N2PLog.Error.E535(value, str)
    # ------------------------------------------------------------------------------------------------------------------

    @FileDescription.setter 
    def FileDescription(self, value: str) -> None: 
        if type(value) == str: 
            self._file_description = value 
        else: 
            N2PLog.Warning.W527(value, str)
    # ------------------------------------------------------------------------------------------------------------------

    @MemoryFile.setter
    def MemoryFile (self, value: bool) -> None:
        self._memory_file_boolean = value
    # ------------------------------------------------------------------------------------------------------------------

    # Method used to create an HDF5 file -------------------------------------------------------------------------------
    def create_hdf5(self) -> None:

        """
        Method used to create an HDF5 file, either in disk (if the FilePath attribute has been filled in), or in memory 
        (if the FilePath boolean attribute has not been filled in). This file will have the following default 
        attributes: 
            - "SOFTWARE", which will always be "NAXTO". 
            - "DESCRIPTION", which will be the FileDescription attribute (if it has been set). 
            - "CREATION_DATE", which will be the exact date when this function is called. Its structure will be 
                HH:MM:SS, DD-MM-YYYY    <==>    hour:minutes:seconds, day-month-year 
        Then, a first group will be created, called "NAXTO", with the following attributes: 
            - "VERSION", which will be the NaxTo version used. 
            - "ASSEMBLY", which will be the NaxToPy version used. 
        Finally, a second group will be created inside the "NAXTO" group, called "RESULTS", which will be empty and 
        should be filled with data written in the "write_dataset()" function. 
        """

        if self._memory_file_boolean == True:
            self._file = io.BytesIO()
        else:
            self._file = self.FilePath
        with h5py.File(self._file, "w") as hdf:
            hdf.attrs["SOFTWARE"] = "NAXTO"
            if self.FileDescription:
                hdf.attrs["DESCRIPTION"] = self.FileDescription
            t = time.gmtime()
            hdf.attrs["CREATION_DATE"] = str(t[3]) + ":" + str(t[4]) + ":" + str(t[5]) + ", " + str(t[0]) + "-" + str(t[1]) + "-" + str(t[2])
    
            naxto = hdf.create_group("NAXTO")
            naxto.attrs["VERSION"] = Constants.NAXTO_VERSION
            naxto.attrs["ASSEMBLY"] = Constants.VERSION

            results = naxto.create_group("RESULTS") 
    # ------------------------------------------------------------------------------------------------------------------

    # Method used to write a dataset -----------------------------------------------------------------------------------
    def write_dataset(self, dataEntryList: list[DataEntry]) -> None: 

        """
        Method used to fill in the dataset(s) of the HDF5 file. 

        Args: 
            dataEntryList: list[DataEntry] -> list of DataEntry instances to write in the dataset(s). 

        The following groups are created (every group is created inside the previous one): 
            - Load Case group, whose name will be the LoadCase attribute of the DataEntry instance, corresponding to 
            the load case's ID. It will have the following attribute: 
                + "DESCRIPTION", which will be the LoadCaseDescription attribute of the DataEntry instance. 
            - Increment group, whose name will be the Increment attribute of the DataEntry instance, corresponding to 
            the increment's ID. It will have the following attribute: 
                + "DESCRIPTION", which will be the IncrementDescription attribute of the DataEntry instance. 
                + "VALUE", which will be the IncrementValue attribute of the DataEntry instance. 
            - Results name group, whose name will be the ResultsName attribute of the DataEntry instance, corresponding  
            to whatever results are being exported. It will have the 
            following attributes: 
                + "DESCRIPTION", which will be the ResultsNameDescription attribute of the DataEntry instance.
                + "TYPE", which will be the ResultsType attribute of the DataEntry instance, corresponding to the type 
                of results that are being exported ("ELEMENT", "CORNER" or "NODE"). 
            - Section group, whose name will be the Section attribute of the DataEntry instance, corresponding to the 
            section in which the results are being displayed. It will have the following attributes: 
                + "DESCRIPTION", which will be the SectionDescription attribute of the DataEntry instance. 
        Finally, the data dataset will be created, whose name will be the PartName attribute of the DataEntry instance, 
        corresponding to the part ID where the results are being displayed. It will have the following attributes: 
            - "DESCRIPTION", which will be the DataDescription attribute of the DataEntry instance. 
            - "PART NAME", which will be the PartName attribute of the DataEntry instance. 
        Inside the dataset, the Data attribute of the DataEntry instances will be written as a table. 
        """

        for dataEntry in dataEntryList: 
            if not dataEntry.ResultsName or dataEntry.LoadCase is None or dataEntry.Increment is None or not dataEntry.Section or not dataEntry.PartName or dataEntry.Data is None: 
                N2PLog.Warning.W700()
                continue 
            l = len(dataEntry.Data)
            with h5py.File(self._file, "a") as hdf:
                naxto = hdf["NAXTO"]
                results = naxto["RESULTS"]
                if str(dataEntry.LoadCase) in results: 
                    # caso de carga ya creado 
                    lc = results[str(dataEntry.LoadCase)]
                    if str(dataEntry.Increment) in lc: 
                        # incremento ya creado 
                        increment = lc[str(dataEntry.Increment)]
                        if dataEntry.ResultsName in increment: 
                            # resultados ya creados 
                            resultsName = increment[dataEntry.ResultsName]
                            if dataEntry.Section in resultsName: 
                                # sección ya creada 
                                section = resultsName[dataEntry.Section]
                                if dataEntry.PartName in section: 
                                    # dataset ya creado 
                                    data = section[dataEntry.PartName]
                                    if data == dataEntry.Data.dtype: 
                                        s = data.shape[0]
                                        data.resize(s + l, axis = 0)
                                        for i,j in enumerate(dataEntry.Data): 
                                            data[s + i] = j 
                                    else: 
                                        N2PLog.Error.E700()
                                        continue 
                                else: 
                                    # dataset sin crear, se crea ahora 
                                    data = section.create_dataset(dataEntry.PartName, shape = (l, 1), maxshape = (None, 1), compression = "gzip", compression_opts = 9, dtype = dataEntry.Data.dtype)
                                    data.attrs["DESCRIPTION"] = dataEntry.DataDescription 
                                    data.attrs["PART NAME"] = dataEntry.PartName
                                    for i,j in enumerate(dataEntry.Data): 
                                        data[i] = j
                            else: 
                                # sección sin crear, se crea ahora 
                                section = resultsName.create_group(dataEntry.Section)
                                section.attrs["DESCRIPTION"] = dataEntry.SectionDescription
                                data = section.create_dataset(dataEntry.PartName, shape = (l, 1), maxshape = (None, 1), compression = "gzip", compression_opts = 9, dtype = dataEntry.Data.dtype)
                                data.attrs["DESCRIPTION"] = dataEntry.DataDescription 
                                data.attrs["PART NAME"] = dataEntry.PartName
                                for i,j in enumerate(dataEntry.Data): 
                                    data[i] = j
                        else: 
                            # resultados sin crear, se crean ahora 
                            resultsName = increment.create_group(dataEntry.ResultsName)
                            resultsName.attrs["DESCRIPTION"] = dataEntry.ResultsNameDescription
                            resultsName.attrs["TYPE"] = dataEntry.ResultsNameType
                            section = resultsName.create_group(dataEntry.Section)
                            section.attrs["DESCRIPTION"] = dataEntry.SectionDescription
                            data = section.create_dataset(dataEntry.PartName, shape = (l, 1), maxshape = (None, 1), compression = "gzip", compression_opts = 9, dtype = dataEntry.Data.dtype)
                            data.attrs["DESCRIPTION"] = dataEntry.DataDescription 
                            data.attrs["PART NAME"] = dataEntry.PartName
                            for i,j in enumerate(dataEntry.Data): 
                                data[i] = j
                    else: 
                        # incremento sin crear, se crea ahora 
                        increment = lc.create_group(str(dataEntry.Increment))
                        increment.attrs["DESCRIPTION"] = dataEntry.IncrementDescription 
                        increment.attrs["VALUE"] = dataEntry.IncrementValue 
                        resultsName = increment.create_group(dataEntry.ResultsName)
                        resultsName.attrs["DESCRIPTION"] = dataEntry.ResultsNameDescription
                        resultsName.attrs["TYPE"] = dataEntry.ResultsNameType
                        section = resultsName.create_group(dataEntry.Section)
                        section.attrs["DESCRIPTION"] = dataEntry.SectionDescription 
                        data = section.create_dataset(dataEntry.PartName, shape = (l, 1), maxshape = (None, 1), compression = "gzip", compression_opts = 9, dtype = dataEntry.Data.dtype)
                        data.attrs["DESCRIPTION"] = dataEntry.DataDescription 
                        data.attrs["PART NAME"] = dataEntry.PartName
                        for i,j in enumerate(dataEntry.Data): 
                            data[i] = j
                else: 
                    # caso de carga sin crear, se crea ahora 
                    lc = results.create_group(str(dataEntry.LoadCase))
                    lc.attrs["DESCRIPTION"] = dataEntry.LoadCaseDescription 
                    increment = lc.create_group(str(dataEntry.Increment))
                    increment.attrs["DESCRIPTION"] = dataEntry.IncrementDescription 
                    increment.attrs["VALUE"] = dataEntry.IncrementValue 
                    resultsName = increment.create_group(dataEntry.ResultsName)
                    resultsName.attrs["DESCRIPTION"] = dataEntry.ResultsNameDescription
                    resultsName.attrs["TYPE"] = dataEntry.ResultsNameType
                    section = resultsName.create_group(dataEntry.Section)
                    section.attrs["DESCRIPTION"] = dataEntry.SectionDescription 
                    data = section.create_dataset(dataEntry.PartName, shape = (l, 1), maxshape = (None, 1), compression = "gzip", compression_opts = 9, dtype = dataEntry.Data.dtype)
                    data.attrs["DESCRIPTION"] = dataEntry.DataDescription 
                    data.attrs["PART NAME"] = dataEntry.PartName
                    for i,j in enumerate(dataEntry.Data): 
                        data[i] = j
    # ------------------------------------------------------------------------------------------------------------------

    # Method used to write an hdf5 file in memory instead of in a path -------------------------------------------------
    def write_local_file(self) -> None:

        """
        Method used to convert an HDF5 file that has been created in memory to an HDF5 file in disk, which will be 
        located in the FilePath attribute. 
        """

        if isinstance(self._file, io.BytesIO):
            # Regresa el puntero al inicio del archivo
            self._file.seek(0)
            
            # Escribe el contenido del archivo en memoria al disco
            with open(self._file_path, 'wb') as disk_file:
                disk_file.write(self._file.read())
            # print(f"Archivo HDF5 guardado en {self._file_path}")
        else:
            raise ValueError("No se está usando un archivo en memoria para este caso.")