import time

from internal.infra.adb.adb_function import ADBClient
from internal.infra.bigquery.get_bigquery_db import BigQueryFunction
from internal.infra.pages.create_comment import CreateComment
from internal.infra.pages.system import System
from internal.infra.validators.validators import Validators


def go_to_create_comment():
    ADBClient.start_playsee_app().icon_create_click()
    return CreateComment()


def test_icon_close_click():
    event_name = "icon_close_click"
    go_to_create_comment().icon_close_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_btn_community_click():
    event_name = "btn_community_click"
    go_to_create_comment().btn_community_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_textfields_comment_click():
    event_name = "textfields_comment_click"
    go_to_create_comment()
    System().back_click()
    CreateComment().textfields_comment_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_first_event_name(result, event_name)


def test_textfields_comment_typing_and_btn_comment_click_and_publish_comment_success():
    event_name = "textfields_comment_typing"
    go_to_create_comment().textfields_comment_typing()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_event_name_in_count(result, event_name, 3)

    event_name = "btn_comment_click"
    content_type = "community"
    event_name_2 = "publish_comment_success"
    content_type_2 = "community_comment"

    CreateComment().btn_comment_click()
    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name, content_type)
    Validators().validate_event_name_content_type_in_count(result, event_name_2, content_type_2)


def test_icon_album_click():
    event_name = "icon_album_click"
    go_to_create_comment().icon_album_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


def test_icon_location_pin_click():
    event_name = "icon_location_pin_click"
    go_to_create_comment().icon_location_pin_click()

    result = BigQueryFunction().query_bigquery_dynamic_date()
    BigQueryFunction().display_query_result(result, 5)

    Validators().validate_change_page(result, event_name)


