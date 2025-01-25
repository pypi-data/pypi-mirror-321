from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_script


def clean_up(session: Session, dest_database: str) -> List[Row]:
    return run_script(session, "CleanUp", DestDatabase=dest_database).all()


def get_engines_for_model_and_model_year(session: Session, model: int) -> List[Row]:
    return run_script(session, "getEnginesForModelAndModelYear", model=model).all()


def get_valid_profiles_for_selected_builder(
    session: Session, selected_profiles: str
) -> List[Row]:
    return run_script(
        session, "getValidProfilesForSelectedBuilder", selectedProfiles=selected_profiles
    ).all()


def get_vin_components(session: Session, vin: str) -> List[Row]:
    return run_script(session, "getVINComponents", vin=vin).all()


def get_vin_components_by_partner_group_id(session: Session, vin: str) -> List[Row]:
    return run_script(session, "getVINComponentsByPartnerGroupId", vin=vin).all()


def get_vin_components_by_partner_group_id_swdl(session: Session, vin: str) -> List[Row]:
    return run_script(session, "getVINComponentsByPartnerGroupIdSwdl", vin=vin).all()


def sp__return_csv(session: Session, column_name: str) -> List[Row]:
    return run_script(session, "sp_ReturnCSV", ColumnName=column_name).all()
