import os
from enum import Enum


from pih.consts.ad import AD
from pih.consts.facade import *
from pih.consts.file import FILE
from ipih import ROOT_MODULE_NAME
from pih.consts.hosts import Hosts
from pih.consts.python import PYTHON
from pih.tools import j, n, PathTool, nn
from pih.consts.document import DocumentTypes


from setuptools.dist import Distribution

PATH_SPLITTER: str = "/"
PATH_DOUBLE_SPLITTER: str = "//"


class PATH_SHARE:
    NAME: str = "shares"
    PATH: str = os.path.join(AD.PATH_ROOT, NAME)


class PATH_FACADE:
    LINUX_MOUNT_POINT: str = j((PATH_SPLITTER, "mnt"))
    SHARED_POINT_PATH: str = os.path.join("S$", FACADE.NAME)
    LINUX_MOUNT_POINT_PATH: str = j((LINUX_MOUNT_POINT, FACADE.NAME), PATH_SPLITTER)
    FILES_NAME: str = ".files"
    TOOLS_NAME: str = ".tools"

    VALUE: str = j(
        (
            PATH_DOUBLE_SPLITTER,
            AD.DOMAIN_MAIN,
            PATH_SPLITTER,
            FACADE.NAME,
            PATH_SPLITTER,
        )
    )

    @staticmethod
    def SERVICE(service_name: str) -> str:
        return os.path.join(
            PATH_FACADE.VALUE,
            FACADE.SERVICE_NAME(service_name),
        )

    @staticmethod
    def SERVICE_FILES(standalone_name: str) -> str:
        return os.path.join(PATH_FACADE.FILES(), standalone_name)

    @staticmethod
    def SERVICE_TOOLS(standalone_name: str) -> str:
        return os.path.join(PATH_FACADE.TOOLS(), standalone_name)

    @staticmethod
    def FILES() -> str:
        return os.path.join(PATH_FACADE.VALUE, PATH_FACADE.FILES_NAME)

    @staticmethod
    def TOOLS() -> str:
        return os.path.join(PATH_FACADE.VALUE, PATH_FACADE.TOOLS_NAME)

    @staticmethod
    def STORAGE() -> str:
        return os.path.join(r"\\", Hosts.DC1.NAME, PATH_FACADE.SHARED_POINT_PATH)

    class DITRIBUTIVE:

        SPLITTER: str = "-"
        FOLDER_NAME: str = ".distr"
        PACKAGE_FOLDER_NAME: str = "all"
        DEFAULT_PACKAGE_TAG: str = "py3-none-any"

        @staticmethod
        def NAME(value: str, version: str | None = None) -> str:
            return j(
                (ROOT_MODULE_NAME, value, None if n(version) else j(("==", version))),
                PATH_FACADE.DITRIBUTIVE.SPLITTER,
            )

        @staticmethod
        def VALUE() -> str:
            return os.path.join(PATH_FACADE.VALUE, PATH_FACADE.DITRIBUTIVE.FOLDER_NAME)

        @staticmethod
        def PACKAGE_FOLDER(name: str, version: str | None = None) -> str:
            path_list: list[str] = [PATH_FACADE.DITRIBUTIVE.VALUE(), name]
            if nn(version):
                path_list.insert(1, PATH_FACADE.DITRIBUTIVE.PACKAGE_FOLDER_NAME)
            return os.path.join(*path_list)

        @staticmethod
        def PACKAGE(name: str, version: str | None) -> str:
            def wheel_name(name: str, version: str | None) -> str:
                tag: str = ""
                dist_name: str = ""
                try:
                    dist: Distribution = Distribution(
                        attrs={"name": name, "version": version}
                    )
                    bdist_wheel_cmd = dist.get_command_obj("bdist_wheel")
                    bdist_wheel_cmd.ensure_finalized()
                    dist_name = bdist_wheel_cmd.wheel_dist_name
                    tag = PATH_FACADE.DITRIBUTIVE.SPLITTER.join(
                        bdist_wheel_cmd.get_tag()
                    )
                except BaseException as _:
                    dist_name = PATH_FACADE.DITRIBUTIVE.SPLITTER.join((name, version))
                    tag = PATH_FACADE.DITRIBUTIVE.DEFAULT_PACKAGE_TAG
                return PathTool.add_extension(
                    j((dist_name, PATH_FACADE.DITRIBUTIVE.SPLITTER, tag)),
                    PYTHON.PACKAGE_EXTENSION,
                )

            return os.path.join(
                *[
                    PATH_FACADE.DITRIBUTIVE.PACKAGE_FOLDER(name, version),
                    wheel_name(
                        j((ROOT_MODULE_NAME, name), "_"),
                        version,
                    ),
                ]
            )

    class VIRTUAL_ENVIRONMENT:

        NAME_PREFIX: str = ".venv"


class PATH_DATA_STORAGE:
    NAME: str = ".data"
    VALUE: str = os.path.join(PATH_FACADE.VALUE, NAME)


class PATH_BUILD:
    NAME: str = ".build"
    VALUE: str = os.path.join(PATH_FACADE.VALUE, NAME)


class PATH_SCAN:
    NAME: str = "scan"
    VALUE: str = os.path.join(AD.PATH_ROOT, NAME)


class PATH_MEDICAL_DATA:

    HOST: str = Hosts.DC1.NAME
    NAME: str = "medicalData"
    VALUE: str = PathTool.path(os.path.join(AD.PATH_ROOT, NAME))


class PATH_SCAN_TEST:
    NAME: str = "test"
    VALUE: str = os.path.join(PATH_SCAN.VALUE, NAME)


class PATH_SCAN_SOURCE:
    NAME: str = "Исходники"
    VALUE: str = os.path.join(PATH_SCAN.VALUE, NAME)


class PATH_SCAN_RESULT:
    NAME: str = "Результат"
    VALUE: str = os.path.join(PATH_SCAN.VALUE, NAME)

    @staticmethod
    def get_path(type: DocumentTypes) -> str | None:
        if type == DocumentTypes.MEDICAL_DIRECTION:
            return os.path.join(PATH_SCAN_RESULT.VALUE, "Направления")


class PATH_WS_816_SCAN:

    HOST: str = Hosts.WS816.NAME
    NAME: str = "Scans"
    VALUE: str = j((PATH_DOUBLE_SPLITTER, os.path.join(HOST, NAME)))


class PATH_OMS:
    NAME: str = "oms"
    VALUE: str = os.path.join(AD.PATH_ROOT, NAME)


class PATH_MARKS:
    NAME: str = "MarkServise"
    VALUE: str = os.path.join(AD.PATH_ROOT, NAME)


class PATH_IT:
    NAME: str = "5. IT"
    NEW_EMPLOYEES_NAME: str = "New employees"
    ROOT: str = os.path.join(PATH_SHARE.PATH, NAME)

    @staticmethod
    def get_new_employee_path(name: str) -> str:
        return os.path.join(
            os.path.join(PATH_IT.ROOT, PATH_IT.NEW_EMPLOYEES_NAME), name
        )


class PATH_APP:
    NAME: str = "apps"
    FOLDER: str = os.path.join(PATH_FACADE.VALUE, NAME)


class PATH_DOCS:
    NAME: str = f"Docs{FACADE.SERVICE_FOLDER_SUFFIX}"
    FOLDER: str = os.path.join(PATH_FACADE.VALUE, NAME)


class PATH_FONTS:
    NAME: str = "fonts"
    FOLDER: str = os.path.join(PATH_DOCS.FOLDER, NAME)

    @staticmethod
    def get(name: str) -> str:
        from pih.tools import PathTool

        return os.path.join(
            PATH_FONTS.FOLDER,
            PathTool.add_extension(name, FILE.EXTENSION.TRUE_TYPE_FONT),
        )


class PATH_APP_DATA:
    NAME: str = "data"
    FOLDER: str = os.path.join(PATH_APP.FOLDER, NAME)

    OCR_RESULT_NAME: str = "ocr result"
    OCR_RESULT_FOLDER: str = os.path.join(FOLDER, OCR_RESULT_NAME)

    @staticmethod
    def LOCATION_IMAGE_PATH(index: int) -> str:
        return PathTool.path(
            os.path.join(
                PATH_APP_DATA.FOLDER,
                "location",
                PathTool.add_extension(str(index), FILE.EXTENSION.JPG),
            )
        )


class PATH_STATISTICS:
    NAME: str = "statistics"
    CHART_FILE_NAME_PREFIX: str = "chart_"
    FOLDER: str = os.path.join(PATH_APP_DATA.FOLDER, NAME)

    @staticmethod
    def get_file_path(name: str | Enum) -> str:
        from pih.tools import EnumTool

        name = EnumTool.get(name)
        return PathTool.path(
            os.path.join(
                PATH_STATISTICS.FOLDER, PathTool.add_extension(name, FILE.EXTENSION.PNG)
            )
        )


class PATH_INDICATIONS:
    NAME: str = "indications"
    FOLDER: str = os.path.join(PATH_APP_DATA.FOLDER, NAME)

    CHILLER_DATA_NAME: str = "chiller"
    CHILLER_DATA_FOLDER: str = os.path.join(FOLDER, CHILLER_DATA_NAME)

    CHILLER_DATA_IMAGE_LAST: str = os.path.join(
        CHILLER_DATA_FOLDER, f"last.{FILE.EXTENSION.JPG}"
    )
    CHILLER_DATA_IMAGE_LAST_RESULT: str = os.path.join(
        CHILLER_DATA_FOLDER, f"last_result.{FILE.EXTENSION.JPG}"
    )

    @staticmethod
    def CHILLER_DATA_IMAGE_RESULT(
        datetime_string: str, temperature: float | None, indications: int
    ) -> str:
        name_list: list[str] = [str(indications)]
        if temperature is not None:
            name_list += [str(temperature)]
        name_list += [datetime_string]
        return os.path.join(
            PATH_INDICATIONS.CHILLER_DATA_FOLDER,
            f"{'_'.join(name_list)}.{FILE.EXTENSION.JPG}",
        )


class PATH_MOBILE_HELPER:
    NAME: str = "mobile helper"
    FOLDER: str = os.path.join(PATH_APP_DATA.FOLDER, NAME)

    QR_CODE_NAME: str = "qr code"
    QR_CODE_FOLDER: str = os.path.join(FOLDER, QR_CODE_NAME)

    INCOME_IMAGES_NAME: str = "income images"
    INCOME_IMAGES_FOLDER: str = os.path.join(FOLDER, INCOME_IMAGES_NAME)

    FILES_NAME: str = "files"
    FILES_FOLDER: str = os.path.join(FOLDER, FILES_NAME)

    TIME_TRACKING_REPORT: str = "time tracking report"
    TIME_TRACKING_REPORT_FOLDER: str = os.path.join(FOLDER, TIME_TRACKING_REPORT)


class PATH_POLIBASE_APP_DATA:
    NAME: str = "polibase"
    FOLDER: str = os.path.join(PATH_APP_DATA.FOLDER, NAME)
    PERSON_CARD_REGISTRY_FOLDER: str = os.path.join(FOLDER, "person card folder")

    SERVICE_FOLDER_PATH: str = os.path.join(
        PATH_FACADE.VALUE, f"{NAME}{FACADE.SERVICE_FOLDER_SUFFIX}"
    )

    class SETTINGS:
        MAIN: str = "polibase_main_settings.vbs"
        TEST: str = "polibase_test_settings.vbs"


class PATH_USER:
    NAME: str = "homes"
    HOME_FOLDER: str = os.path.join(AD.PATH_ROOT, NAME)
    HOME_FOLDER_FULL: str = os.path.join(AD.PATH_ROOT, NAME)

    @staticmethod
    def private_folder(login: str) -> str:
        return os.path.join(PATH_USER.HOME_FOLDER, login)

    @staticmethod
    def get_document_name(user_name: str, login: str | None = None) -> str:
        return (
            PATH_IT.get_new_employee_path(user_name)
            + (f" ({login})" if login else "")
            + ".docx"
        )


class PATH_POLIBASE:
    NAME: str = Hosts.POLIBASE.ALIAS
    DATA_FOLDER_NAME: str = "Data"
    PERSON_FOLDER_NAME: str = "PERSONS"
    TEST_SUFFIX: str = "_test"
    PERSON_CARD_REGISTRY_FOLDER: str = (
        PATH_POLIBASE_APP_DATA.PERSON_CARD_REGISTRY_FOLDER
    )

    @staticmethod
    def person_folder(pin: int | None = None, test: bool = False) -> str:
        root: str = PATH_POLIBASE.NAME
        if test:
            if root.find(".") != -1:
                root_parts: list[str] = root.split(".")
                root_parts[0] += PATH_POLIBASE.TEST_SUFFIX
                root = j(root_parts, ".")
            else:
                root += PATH_POLIBASE.TEST_SUFFIX
        return j(
            (
                r"\\",
                os.path.join(
                    root,
                    PATH_POLIBASE.DATA_FOLDER_NAME,
                    PATH_POLIBASE.PERSON_FOLDER_NAME,
                    "" if n(pin) else str(pin),
                ),
            )
        )


class PATH_WS:
    NAME: str = j(("WS", FACADE.SERVICE_FOLDER_SUFFIX))
    PATH: str = os.path.join(PATH_FACADE.VALUE, NAME)


class PATHS:
    SHARE: PATH_SHARE = PATH_SHARE()
    SCAN: PATH_SCAN = PATH_SCAN()
    MEDICAL_DATA: PATH_MEDICAL_DATA = PATH_MEDICAL_DATA()
    SCAN_TEST = PATH_SCAN_TEST()
    SCAN_SOURCE = PATH_SCAN_SOURCE()
    SCAN_RESULT = PATH_SCAN_RESULT()
    WS_816_SCAN: PATH_WS_816_SCAN = PATH_WS_816_SCAN()
    OMS: PATH_OMS = PATH_OMS()
    IT: PATH_IT = PATH_IT()
    USER: PATH_USER = PATH_USER()
    POLIBASE: PATH_POLIBASE = PATH_POLIBASE()
    POLIBASE_APP_DATA: PATH_POLIBASE_APP_DATA = PATH_POLIBASE_APP_DATA()
    WS: PATH_WS = PATH_WS()
    DOCS: PATH_DOCS = PATH_DOCS()
    FONTS: PATH_FONTS = PATH_FONTS()
    MOBILE_HELPER: PATH_MOBILE_HELPER = PATH_MOBILE_HELPER()
    APP_DATA: PATH_APP_DATA = PATH_APP_DATA()
    INDICATIONS: PATH_INDICATIONS = PATH_INDICATIONS()
    STATISTICS: PATH_STATISTICS = PATH_STATISTICS()
    FACADE: PATH_FACADE = PATH_FACADE()
    DATA_STORAGE: PATH_DATA_STORAGE = PATH_DATA_STORAGE()
    BUILD: PATH_BUILD = PATH_BUILD()
