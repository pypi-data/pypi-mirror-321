import uuid
import structlog
from structlog.typing import EventDict
from elastic_extension import ESStructLogExtension

_ES_MESSAGE_KEY = "message"
_ISO_FORMAT = "iso"


class ESStructLogProcessor:
    def __init__(self,
                 host: str = None,
                 basic_auth: tuple[str, str] = None,
                 index: str = None,
                 flush_frequency: int = 1,
                 raise_on_indexing_error: bool = False,
                 verify_certs: bool = True,
                 es_extension: ESStructLogExtension = None):
        """Elastic Processor for structlog. NOTICE, if you provide es_extension don't provide any other params.

        :param flush_frequency: Frequency of flushing log messages sent to Elastic.
        :param verify_certs: Should certificates be verified?
        :param index: Elasticsearch index name.
        :param basic_auth: Elastic user credentials.
        :param host: The Elastic host to connect to.
        :param raise_on_indexing_error: Should indexing errors be raised.
        :param es_extension: Configured ES extension for processor."""
        if es_extension is None:
            self._es_struct_log_extension = ESStructLogExtension(host=host,
                                                                 basic_auth=basic_auth,
                                                                 index=index,
                                                                 flush_frequency=flush_frequency,
                                                                 raise_on_indexing_error=raise_on_indexing_error,
                                                                 verify_certs=verify_certs)
        else:
            self._es_struct_log_extension = es_extension

    def __call__(self, _logger, _name, event_dict: EventDict):
        event_dict.update(request_id=str(uuid.uuid4()))
        self._es_struct_log_extension.emit(event_dict)
        return event_dict


def configure_es_structlog_logger(host: str,
                                  basic_auth: tuple[str, str],
                                  index: str,
                                  verify_certs: bool,
                                  flush_frequency: int):
    """Default configuration for structlog & ES processor.
    
    :param flush_frequency: Frequency of flushing log messages sent to Elastic.
    :param verify_certs: Should certificates be verified?
    :param index: Elasticsearch index name.
    :param basic_auth: Elastic user credentials.
    :param host: The Elastic host to connect to. 
    """""
    processors = [
        structlog.processors.CallsiteParameterAdder(parameters=[structlog.processors.CallsiteParameter.MODULE,
                                                                structlog.processors.CallsiteParameter.FUNC_NAME,
                                                                structlog.processors.CallsiteParameter.FILENAME]),
        structlog.contextvars.merge_contextvars,
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(fmt=_ISO_FORMAT),
        structlog.processors.EventRenamer(_ES_MESSAGE_KEY),
        ESStructLogProcessor(host=host,
                             basic_auth=basic_auth,
                             index=index,
                             flush_frequency=flush_frequency,
                             verify_certs=verify_certs),
        structlog.processors.KeyValueRenderer(key_order=["message", "request_id"])
    ]

    structlog.configure(
        processors=processors,
        context_class=dict
    )


def get_structlog_logger() -> structlog.stdlib.BoundLogger:
    """Function that return the structlog default logger. Use it for dependency injection."""
    if not structlog.is_configured():
        raise Exception("structlog logger is not configured.")

    return structlog.stdlib.get_logger()
