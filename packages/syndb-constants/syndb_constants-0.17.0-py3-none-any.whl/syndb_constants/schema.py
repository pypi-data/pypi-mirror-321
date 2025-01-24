from typing import Final

from syndb_constants.table import SyndbTable

DATASET_ID_COLUMN_NAME: Final[str] = "dataset_id"
PARENT_ID_COLUMN_NAME: Final[str] = "parent_id"
PARENT_ENUM_COLUMN_NAME: Final[str] = "parent_enum"

SINGLE_ID_COLUMN_NAME: Final[str] = "cid"
MULTI_ID_TABLE_TO_ID_COLUMNS: Final[dict[SyndbTable, list[str]]] = {
    SyndbTable.NEURON_RELATION: ["pre_synapse_id", "post_synapse_id"],
}
