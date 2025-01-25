from pathlib import Path
import re

import eccodes as ecc


class StandardComplianceChecker:

    CHECKER_CODE = 2

    STD_KEYS = {
        "editionNumber": 2,
        "centre": "ecmf",
#         "tablesVersion": 31,
        "productionStatusOfProcessedData": 12,
        "destineLocalVersion": 1
    }

    def __init__(self, msgid, logger, param_definitions=None):
        self.status = 0
        self.msgid = msgid
        self.logger = logger
        self.param_definitions = param_definitions
        self.err_msg = ""

    @staticmethod
    def read_definition_file(filename):
        PARAM_PATTERN = "'(\d+)'"
        DEF_PATTERN = "([a-zA-Z]+)\s\=\s(-?\d+)\s\;"

        with open(filename, 'r') as f:
            params = {}

            for line in f:
                # Identify paramId definition
                match = re.match(PARAM_PATTERN, line)
                if match:
                    current_param = match.group(1)

                    if current_param in params:  # pragma: no cover
                        raise Exception(  # TODO: Exception not checked. Can this even happen?
                            f"Duplicated paramId: {current_param} "
                            f"in definitions file {filename}"
                        )
                    params[current_param] = {}

                # Identify attribute
                match = re.search(DEF_PATTERN, line)
                if match:
                    key, value = match.group(1), match.group(2)
                    params[current_param][key] = value

        return params

    @classmethod
    def get_grib_param_definitions(cls):
        DEF_PATH = Path(ecc.codes_definition_path().split(":")[0])
        DEF_WMO = DEF_PATH / "grib2/paramId.def"
        DEF_ECMWF = DEF_PATH / "grib2/localConcepts/ecmf/paramId.def"

        params = cls.read_definition_file(DEF_WMO)
        params.update(cls.read_definition_file(DEF_ECMWF))

        return params

    def run(self):

        # Check standard common keys
        for key, ref_value in self.STD_KEYS.items():
            grib_value = ecc.codes_get(self.msgid, key)

            if grib_value != ref_value:
                self.err_msg += (
                    f"Standard Compliance: Missmatch between obtained "
                    f"and expected {key} value: {grib_value} was obtanied, "
                    f"but {ref_value} was expected."
                )
                self.status = 1

        # Check param defining GRIB codes from definitions
        if self.param_definitions is None:
            self.param_definitions = self.get_grib_param_definitions()
        param_id = ecc.codes_get(self.msgid, "paramId")

        for key, ref_value in self.param_definitions[str(param_id)].items():
            grib_value = ecc.codes_get(self.msgid, key, ktype=int)

            if grib_value != int(ref_value):
                self.err_msg += (
                    f"Standard Compliance: Missmatch between obtained "
                    f"and expected {key} value: {grib_value} was obtanied, "
                    f"but {ref_value} was expected."
                )
                self.status = 1

