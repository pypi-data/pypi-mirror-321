from pathlib import Path
from copy import deepcopy
from rich.console import Console
from typing import Union, List, Dict, Tuple, Any, TypeVar 

from kudaflib.config.settings import settings
from kudaflib.schemas.dcat import (
    CatalogMetadataInput,
    DatasetMetadataInput,
    ContactAPIInput,
    OrganizationAPIInput,
    PublisherAPIInput,
    CatalogAPIInput,
    DatasetAPIInput,
    OrganizationDCATOutput,
    CatalogDCATOutput,
    DatasetDCATOutput,
)
from kudaflib.schemas.variable import (
    VariableMetadata,
    VariableMetadataInput,
    VariableMetadataAPIInput,
    VariablesAPIInput,
    VarToUnitTypeLinkAPIInput,
    MeasureVariableAPIInput,
    UnitTypeMetadataInput,
    UnitTypeAPIInput,
)
from kudaflib.logic.utils import (
    validate_metadata_model,
    write_json,
    load_yaml,
    convert_to_multilingual_dict,
    get_multilingual_value_string,
    replace_enums,
    unittype_to_multilingual,
)
from kudaflib.logic.dcat_process import dcat_process
from kudaflib.logic.variable_process import variable_process
from kudaflib.logic.unit_type_process import unit_type_process


console = Console()

ModelType = TypeVar("ModelType")

global all_unit_types


class MetadataProcess:
    def __init__(self):
        self.target_url = ""

    def create(
        self, 
        config_yaml_path: Path,
        target_environment: str,
        api_key: str,
        output_metadata_dir: Union[Path, None] = None,
    ) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Creates (POSTs) Kudaf Metadata (from a YAML configuration file) via the Kudaf-Metadata API 
        """
        self.target_url = settings.KUDAF_METADATA_BACKEND_BASE_URLS.get(target_environment, "")
        console.print(f"[bold blue] Uploading Metadata to KUDAF system @ :point_right: [italic]{self.target_url}[/italic][/bold blue]")

        catalogs = {}
        datasets = {}
        variables = {}
        unit_types = {}

        catalog_id, dataset_id = None, None

        config_dict = load_yaml(config_yaml_path)

        ################## PROCESS YAML CATALOGS ##################

        for cat in config_dict.get('catalogs'):
            # Validate Catalog Metadata
            _in_catmodel = validate_metadata_model(Model=CatalogMetadataInput, metadata_json=cat)

            # Check if Catalog already exists
            cat_title = cat.get('title')
            cat_api_response_get = dcat_process.query_existing_catalogs(
                target_environment=target_environment,
            )

            for _c in cat_api_response_get:
                if _c.get('id') is not None:
                    if cat_title == get_multilingual_value_string(_c.get('metadata', {}).get('title', {})):
                        console.print(f"[yellow]:locked_with_key: Catalog {cat_title} already exists --> skipping creation")
                        catalog_id = _c.get('id')
                        break

            if catalog_id is None:
                # Create a new Catalog
                # Convert to API input format
                contact_api_dict = ContactAPIInput(
                    **_in_catmodel.contact_point.model_dump(exclude_unset=True)  
                ).model_dump(exclude_unset=True)

                publisher_api_input_model = PublisherAPIInput(
                    name=_in_catmodel.publisher.name,
                    organization=OrganizationAPIInput(
                        name=_in_catmodel.publisher.name,
                        description=convert_to_multilingual_dict(_in_catmodel.publisher.description),
                    ),
                )
                publisher_api_dict = replace_enums(publisher_api_input_model.model_dump(exclude_unset=True))

                # Convert to API input format
                cat_api_input_model = CatalogAPIInput(
                    title=convert_to_multilingual_dict(_in_catmodel.title),
                    description=convert_to_multilingual_dict(_in_catmodel.description),
                    publisher=publisher_api_dict,  # Already in API create format
                    contactPoint=contact_api_dict,  # Already in API create format
                )
                cat_dict = replace_enums(cat_api_input_model.model_dump(exclude_unset=True))

                # Add the Catalog to the API
                cat_api_response = dcat_process.create_catalog(
                    input_json=cat_dict,
                    target_environment=target_environment,
                    api_key=api_key,
                )
                if cat_api_response.get('errors') is not None:
                    return {
                        "errors": cat_api_response.get('errors'),
                        "catalogs": catalogs,
                        "datasets": datasets,
                        "variables": variables,
                        "unit_types": unit_types,
                    }
                else:
                    console.print(f"[bold green]:star:- CATALOG: {cat_title} CREATED in Kudaf-Metadata @ {self.target_url}")
                    catalog_id = cat_api_response.get('catalog_id')
                    catalogs[_in_catmodel.title] = {
                        "id": catalog_id,
                        "metadata": cat_dict,
                    }

            ################## PROCESS YAML UNIT TYPES ##################

            # Query existing UnitTypes
            ut_api_response_get = unit_type_process.query_existing_unittypes(
                target_environment=target_environment,
                catalog_id=catalog_id
            )

            if "errors" in ut_api_response_get:
                return {
                        "errors": ut_api_response_get.get('errors'),
                        "catalogs": catalogs,
                        "datasets": datasets,
                        "variables": variables,
                        "unit_types": unit_types,
                    }
   
            global_utypes = {_ut.get('shortName'): _ut for _ut in ut_api_response_get.get('global_unit_types', [])}
            this_catalog_utypes = {_ut.get('shortName'): _ut for _ut in ut_api_response_get.get('catalog_unit_types')}
            globals()['all_unit_types'] = global_utypes | this_catalog_utypes
            
            # Process UnitTypes in YAML file
            for _ut in cat.get('unittypes'):
                _in_ut = deepcopy(_ut)

                # Validate Unit Type Metadata
                _in_utmodel = validate_metadata_model(Model=UnitTypeMetadataInput, metadata_json=_in_ut)

                if _in_utmodel.shortName in global_utypes or _in_utmodel.shortName in this_catalog_utypes:
                    console.print(f"[yellow]:locked_with_key: Unit Type {_in_utmodel.shortName} already exists in Catalog: {cat_title} --> skipping creation")
                    continue

                # Convert to API input format
                ut_api_input_model = UnitTypeAPIInput(
                    catalog_id=catalog_id,
                    unit_type=_in_utmodel,            
                )
                ut_dict = replace_enums(ut_api_input_model.model_dump(exclude_unset=True))

                # Add the Unit Type to the API
                ut_api_response = unit_type_process.create_unit_type(
                    input_json=ut_dict,
                    target_environment=target_environment,
                    api_key=api_key,
                )

                if ut_api_response.get('errors'):
                    return {
                        "errors": ut_api_response.get('errors'),
                        "catalogs": catalogs,
                        "datasets": datasets,
                        "variables": variables,
                        "unit_types": unit_types,
                    }

                console.print(f"[bold green]:star: -> UNIT TYPE: {_in_utmodel.shortName} from Catalog: {cat_title} CREATED in Kudaf-Metadata @ {self.target_url}")
           
                utmulti = unittype_to_multilingual(_in_utmodel)
                _out_utdict = unit_type_process.create_unittype_metadata(unittype_model_input=utmulti) #_in_utmodel)

                unit_types[_in_utmodel.shortName] = {
                    "id": ut_api_response.get('unittype_id'),
                    "metadata": replace_enums(_out_utdict)
                } 

            # Refresh list of existing Catalog UnitTypes with the ones just created
            ut_api_response_get = unit_type_process.query_existing_unittypes(
                catalog_id=catalog_id,
                target_environment=target_environment,
            )

            if "errors" in ut_api_response_get:
                return {
                        "errors": ut_api_response_get.get('errors'),
                        "catalogs": catalogs,
                        "datasets": datasets,
                        "variables": variables,
                        "unit_types": unit_types,
                    }
   
            global_utypes = {_ut.get('shortName'): _ut for _ut in ut_api_response_get.get('global_unit_types', [])}
            this_catalog_utypes = {_ut.get('shortName'): _ut for _ut in ut_api_response_get.get('catalog_unit_types')}
            globals()['all_unit_types'] = global_utypes | this_catalog_utypes

            ################## PROCESS YAML DATASETS ##################

            for ds in _in_catmodel.datasets:
                # Check if Dataset already exists
                ds_id = ds.get('identifier')
                ds_title = ds.get('title')
                ds_api_response_get = dcat_process.query_existing_datasets(
                    target_environment=target_environment,
                )

                ds_exists = False
                for _d in ds_api_response_get:
                    if (_d.get('id') is not None and _d.get('id') == ds_id) or \
                        _d.get('name') == ds_title:
                            ds_exists = True
                            dataset_id = _d.get('id')  # Use the ID from the API
                            break

                if not ds_exists:
                    # Validate Dataset Metadata
                    _in_dsmodel = validate_metadata_model(Model=DatasetMetadataInput, metadata_json=ds)
                    
                    # Convert to API input format
                    ds_api_input_model = DatasetAPIInput(
                        catalogId=catalog_id, 
                        dataset_id=_in_dsmodel.identifier,
                        title=convert_to_multilingual_dict(_in_dsmodel.title),
                        description=convert_to_multilingual_dict(_in_dsmodel.description),
                        publisher=_in_dsmodel.publisher,  # Already in API create format
                        contactPoint=[ContactAPIInput(**_in_dsmodel.contact_point[0].model_dump(exclude_unset=True))],  # Already in API create format
                    )
                    ds_dict = replace_enums(ds_api_input_model.model_dump(exclude_unset=True))

                    # Add the Dataset to the API
                    ds_api_response = dcat_process.create_dataset(
                        input_json=ds_dict,
                        target_environment=target_environment,
                        api_key=api_key,
                    )

                    if ds_api_response.get('errors') is not None:
                        return {
                            "errors": ds_api_response.get('errors'),
                            "catalogs": catalogs,
                            "datasets": datasets,
                            "variables": variables,
                            "unit_types": unit_types,
                        }
                    else:
                        console.print(f"[bold green]:star: -> DATASET: {ds_title} from Catalog: {cat_title} CREATED in Kudaf-Metadata @ {self.target_url}")
                        dataset_id = ds_api_response.get('dataset_id')
                        datasets[_in_dsmodel.title] = {
                            "id": dataset_id,
                            "metadata": ds_dict,
                        }

                    _multiling_vars = dcat_process.convert_fields_to_multilingual(
                        metadata_input_model=_in_dsmodel, 
                        default_lang='no'
                    )
                    ds.update(_multiling_vars) 

                    # Add the ContactPoint metadata
                    ds['contact_point'] = [_in_dsmodel.publisher.contact_point.model_dump(exclude_unset=True)]

                    # Validate completed DCAT Dataset Metadata model
                    _out_dsmodel = validate_metadata_model(Model=DatasetDCATOutput, metadata_json=ds)

                    datasets[_in_dsmodel.title] = {
                        "id": dataset_id,
                        "metadata": replace_enums(_out_dsmodel.model_dump(exclude_unset=True)),
                    }

                else:
                    console.print(f"[yellow]:locked_with_key: Dataset {ds_title} with ID: {dataset_id} already exists in Catalog: {cat_title} --> skipping creation")

                ################## PROCESS YAML VARIABLES ##################

                for _var in ds.get('variables'):  # config_dict.get('variables'):
                    # Get list of existing Variables for this Dataset
                    ds_api_response_get = dcat_process.query_existing_datasets(
                        target_environment=target_environment,
                        dataset_id=dataset_id, 
                        include_variables=True,
                    )

                    if ds_api_response_get:
                        ds_vars = ds_api_response_get.get('variables', [])

                    var_exists = False
                    for _v in ds_vars:
                        if _v.get('name') == _var.get('name'):
                            var_exists = True
                            break
                    
                    if var_exists:
                        console.print(f"[yellow]:locked_with_key: Variable {_var.get('name')} already exists in Dataset: {ds_title} --> skipping creation")
                        continue

                    # Construct the API input for the Identifier Variables
                    ivariables = []
                    idunit_exists = True
                    for iv in _var.get('identifierVariables'):
                        ivname = iv.get('unitType')
                        utid = globals()['all_unit_types'].get(ivname, {}).get('id', 0)
                        if not utid:
                            console.print(f"[red]:poop: Unit Type {ivname} for IdentifierVariable NOT FOUND in Kudaf-Metadata --> skipping creation of Variable: {_var.get('name')}")
                            idunit_exists = False
                            break

                        ivariables.append(VarToUnitTypeLinkAPIInput(unit_type_id=utid))

                    if not idunit_exists:
                        continue

                    mvariables = []
                    munit_exists = True
                    for mv in _var.get('measureVariables'):
                        mvariable = MeasureVariableAPIInput(
                            label=mv.get('label'),
                            description=mv.get('description'),
                            dataType=mv.get('dataType'),
                        )

                        if mv.get('unitType'):
                            utid = globals()['all_unit_types'].get(mv.get('unitType'), {}).get('id', 0)
                            if not utid:
                                console.print(f"[red]:poop: Unit Type {mv.get('unitType', 'MISSING UNIT TYPE')} for MeasureVariable NOT FOUND in Kudaf-Metadata --> skipping creation of Variable: {_var.get('name')}")
                                munit_exists = False
                                break
                            else:
                                mvariable.unitType = VarToUnitTypeLinkAPIInput(unit_type_id=utid)

                        mvariables.append(mvariable)

                    if not munit_exists:
                        continue

                    # Construct the API input for the Variable
                    var_api_input_model = VariablesAPIInput(
                        dataset_id=dataset_id,
                        variables=[VariableMetadataAPIInput(
                            name=_var.get('name'),
                            temporalityType=_var.get('temporalityType'),
                            sensitivityLevel=_var.get('sensitivityLevel'),
                            populationDescription=_var.get('populationDescription'),
                            spatialCoverageDescription=_var.get('spatialCoverageDescription'),
                            subjectFields=_var.get('subjectFields'),
                            identifierVariables=ivariables,
                            measureVariables=mvariables,
                        )],
                    )

                    var_dict = replace_enums(var_api_input_model.model_dump(exclude_unset=True))

                    # POST the Variable via the API
                    var_api_response = variable_process.create_variable(
                        input_json=var_dict,
                        target_environment=target_environment,
                        api_key=api_key,
                    )

                    if var_api_response.get('errors') is not None:
                        return {
                            "errors": var_api_response.get('errors'),
                            "catalogs": catalogs,
                            "datasets": datasets,
                            "variables": variables,
                            "unit_types": unit_types,
                        }
                    
                    console.print(f"[bold green]:star:   --> VARIABLE: {_var.get('name')} from Dataset: {ds_title} CREATED in Kudaf-Metadata @ {self.target_url}")

                    variables[_var.get('name')] = {
                        "id": var_api_response.get('variable_id'),
                        "metadata": var_dict,
                    }

        return {
            "catalogs": catalogs,
            "datasets": datasets,
            "variables": variables,
            "unit_types": unit_types,
        }

    def generate(
        self, 
        config_yaml_path: Path,
        output_metadata_dir: Union[Path, None] = None,
    ) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Generates Kudaf JSON Metadata files (for both Variables and Unit Types) from a YAML configuration file
        """
        variables = []
        unit_types = []

        config_dict = load_yaml(config_yaml_path)

        #### PROCESS YAML VARIABLES SECTION ####
        for _var in config_dict.get('variables'):
            # Validate Input Variable Metadata
            _in_varmodel = validate_metadata_model(Model=VariableMetadataInput, metadata_json=_var)

            # Add the Instance (Identifier, Measure, Attribute) Variables
            _ds_units, _inst_vars = variable_process.insert_instance_variables(metadata_input=_in_varmodel)
            _var.update(_inst_vars)
            _descript_vars = variable_process.convert_descriptions_to_multilingual(metadata_input=_in_varmodel, default_lang='no')
            _var.update(_descript_vars)     

            # Validate completed Output Variable Metadata model
            _metmodel = validate_metadata_model(Model=VariableMetadata, metadata_json=_var)

            variables.append(_metmodel.model_dump(exclude_unset=True))

            # Working list of UnitTypes so far
            ut_names = [_u.get('shortName') for _u in unit_types]
            # Add to UnitTypes if new
            unit_types += [_unit for _unit in _ds_units if _unit.get('shortName') not in ut_names]

        #### WRITE OUT METADATA FILES ####
        out_dir = str(output_metadata_dir) if output_metadata_dir else "./"

        write_json(
            filepath=Path(out_dir) / "variables_metadata.json", 
            content=variables
        )
        if unit_types:
            write_json(
                filepath=Path(out_dir) / "unit_types_metadata.json", 
                content=unit_types
            )

        return variables


metadata_process = MetadataProcess()
