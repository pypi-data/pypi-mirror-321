from .service import RDMServiceComponent
from .record import RDMRecordModelComponent
from .ext_resource import RDMExtResourceModelComponent
from .draft_record import RDMDraftParentComponent
from .marshmallow import RDMMarshmallowModelComponent
from .published_service import RDMPublishedServiceComponent

RDM_COMPONENTS = [
    RDMServiceComponent,
    RDMRecordModelComponent,
    RDMExtResourceModelComponent,
    RDMDraftParentComponent,
    RDMMarshmallowModelComponent,
    RDMPublishedServiceComponent
]
