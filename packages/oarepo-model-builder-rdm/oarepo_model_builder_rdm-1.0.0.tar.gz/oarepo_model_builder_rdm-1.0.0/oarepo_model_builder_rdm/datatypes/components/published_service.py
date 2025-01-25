from oarepo_model_builder.datatypes import ModelDataType
from oarepo_model_builder_drafts.datatypes.components import PublishedServiceComponent
from oarepo_model_builder.datatypes import DataTypeComponent

class RDMPublishedServiceComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    depends_on = [PublishedServiceComponent]

    def before_model_prepare(self, datatype, *, context, **kwargs):
        # temporary solution before the new model builder
        components_to_remove = [
            '{{oarepo_runtime.services.files.FilesComponent}}',
            '{{invenio_drafts_resources.services.records.components.DraftFilesComponent}}'
        ]
        datatype.service_config["components"] = [
            component for component in datatype.service_config["components"]
            if component not in components_to_remove
        ]


