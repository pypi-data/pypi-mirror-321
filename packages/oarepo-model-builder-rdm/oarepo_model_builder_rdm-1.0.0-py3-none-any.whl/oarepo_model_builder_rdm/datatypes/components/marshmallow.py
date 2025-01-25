from oarepo_model_builder.datatypes import ModelDataType
from oarepo_model_builder.datatypes.components import MarshmallowModelComponent
from oarepo_model_builder.datatypes import DataTypeComponent


class RDMMarshmallowModelComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [MarshmallowModelComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        if datatype.root.profile == "record":
            datatype.definition["marshmallow"]["base-classes"].append("oarepo_runtime.services.schema.rdm.RDMRecordMixin")