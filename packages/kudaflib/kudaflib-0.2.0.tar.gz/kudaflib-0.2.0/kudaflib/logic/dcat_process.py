from rich.console import Console
from typing import Union, List, Dict, Tuple, Any, TypeVar 

from kudaflib.config.settings import settings
from kudaflib.schemas.variable import (
    UnitTypeShort,
    UnitTypeMetadata,
    UnitTypeMetadataInput,
)   
from kudaflib.logic.utils import (
    validate_metadata_model,
    convert_to_multilingual_dict,
    convert_list_to_multilingual,
)
from kudaflib.logic.connect import kudaf_metadata_connect


console = Console()

ModelType = TypeVar("ModelType")


class DCATProcess:
    """
    This class contains logic for processing DCAT Metadata (Catalog, Dataset)
    """
    def query_existing_catalogs(
        self,
        target_environment: str,
        catalog_id: int = None,
        include_datasets: bool = False,
        include_variables: bool = False,
    ) -> Dict[str, Any]:
        cats_url = f"{settings.KUDAF_METADATA_BACKEND_URLS.get('catalog')}"

        if catalog_id:
            cats_url += f"{catalog_id}"

        if include_datasets:
            cats_url += "?include_datasets=true"
        elif include_variables:
            cats_url += "?include_variables=true"

        retries = 5
        while retries > 0:
            errors, response_json = kudaf_metadata_connect.get(
                target_environment=target_environment,
                url_path=cats_url,
                api_key_required=False,
            )
            if errors:
                console.print(f"[yellow]:disappointed: Error trying to fetch existing Kudaf-Metadata Catalogs: {response_json.get('errors')} -> Retrying... :crossed_fingers:[/yellow]")
                retries -= 1
            else:
                break

        return response_json

    def query_existing_datasets(
        self,
        target_environment: str,
        dataset_id: int = None,
        include_variables: bool = False,
    ) -> List[Dict[str, Any]]:
        ds_url = f"{settings.KUDAF_METADATA_BACKEND_URLS.get('dataset')}"

        if dataset_id:
            ds_url += f"{dataset_id}"
            
        if include_variables:
            ds_url += "?include_variables=true"

        retries = 5
        while retries > 0:
            errors, response_json = kudaf_metadata_connect.get(
                target_environment=target_environment,
                url_path=ds_url,
                api_key_required=False,
            )
            if errors:
                console.print(f"[yellow]:disappointed: Error trying to fetch existing Kudaf-Metadata Datasets: {response_json.get('errors')} -> Retrying... :crossed_fingers:[/yellow]")
                retries -= 1
            else:
                break

        return response_json
    
    def create_catalog(
        self,
        input_json: Dict[str, Any],
        target_environment: str,
        api_key: str,
    ):
        errors, response_json = kudaf_metadata_connect.post(
            target_environment=target_environment,
            resource="catalog",
            input_json=input_json,
            api_key_required=True,
            api_key=api_key,
        )

        if errors:
            return {"errors": response_json.get("error", "An error occurred")}
        elif response_json.get("sync_results", {}).get('successful', {}).get('num', 0) != 1:
            return {"errors": response_json.get("sync_results", {}).get('errors', {}).get('detail', "")}
        else:
            catalog_id = response_json.get("catalog", {}).get('id', 0)
            catalog_name = response_json.get("catalog", {}).get('name', "")
            return {"catalog_id": catalog_id, "catalog_name": catalog_name}
        
    def create_dataset(
        self,
        input_json: Dict[str, Any],
        target_environment: str,
        api_key: str,
    ):
        errors, response_json = kudaf_metadata_connect.post(
            target_environment=target_environment,
            resource="dataset",
            input_json=input_json,
            api_key_required=True,
            api_key=api_key,
        )
 
        if errors:
            return {"errors": response_json.get("error", "An error occurred")}
        elif response_json.get("sync_results", {}).get('successful', {}).get('num', 0) != 1:
            return {"errors": response_json.get("sync_results", {}).get('errors', {}).get('detail', "")}
        else:
            dataset_id = response_json.get("dataset", {}).get('id', 0)
            dataset_title = response_json.get("dataset", {}).get('title', "")
            return {"dataset_id": dataset_id, "dataset_name": dataset_title}
    
    @staticmethod
    def convert_fields_to_multilingual(
        metadata_input_model: Any, 
        default_lang: str = "no"
    ) -> Dict[str, Any]:
        """
        Converts string fields in a DCAT Metadata Input Model to Norwegian multilingual strings
        of the form {"no": "string"}
        """
        multi_dict = {}
        multilingual_fields = ["title", "name", "description", "keywords", "subjectFields"]
        nested_list_fields = ["subjectFields"]

        # Convert string fields to Norwegian multilungual strings if needed
        for field in multilingual_fields:
            field_contents = getattr(metadata_input_model, field, None)
            if isinstance(field_contents, list):
                if field in nested_list_fields:
                    multi_dict[field] = convert_list_to_multilingual(
                        input_list=field_contents, 
                        default_lang=default_lang,
                        nested_list=True)
                else:
                    multi_dict[field] = convert_list_to_multilingual(input_list=field_contents, default_lang=default_lang)
            elif isinstance(field, str):
                multi_dict[field] = [convert_to_multilingual_dict(input_str=field_contents, default_lang=default_lang)]
            else:
                continue

        return multi_dict
    

dcat_process = DCATProcess()
