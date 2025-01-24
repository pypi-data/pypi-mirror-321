# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import collections
import datetime
import json
from typing import Optional, List, Any, Dict, Union

from azure.functions import EventGridEvent, EventGridOutputEvent

from . import meta
from .meta import Datum


class EventGridEventInConverter(meta.InConverter, binding='eventGridTrigger',
                                trigger=True):

    @classmethod
    def check_input_type_annotation(cls, pytype: type) -> bool:
        """
        Event Grid always sends an array and may send more than one event in
        the array. The runtime invokes function once for each array element,
        thus no need to parse List[EventGridEvent]
        """
        return type(pytype) is type(EventGridEvent)

    @classmethod
    def decode(cls, data: meta.Datum, *,
               trigger_metadata) -> EventGridEvent:
        data_type = data.type

        if data_type == 'json':
            body = json.loads(data.value)
        else:
            raise NotImplementedError(
                f'unsupported event grid payload type: {data_type}')

        return EventGridEvent(
            id=body.get('id'),
            topic=body.get('topic'),
            subject=body.get('subject'),
            event_type=body.get('eventType'),
            event_time=cls._parse_datetime(body.get('eventTime')),
            data=body.get('data'),
            data_version=body.get('dataVersion'),
        )


class EventGridEventOutConverter(meta.OutConverter, binding="eventGrid"):
    @classmethod
    def check_output_type_annotation(cls, pytype: type) -> bool:
        valid_types = (str, bytes, EventGridOutputEvent,
                       List[EventGridOutputEvent])
        return (meta.is_iterable_type_annotation(pytype, str) or meta.
                is_iterable_type_annotation(pytype,
                                            EventGridOutputEvent)
                or (isinstance(pytype, type)
                and issubclass(pytype, valid_types))
                or (type(pytype) is type(EventGridOutputEvent))
                or (type(pytype) is type(List[EventGridOutputEvent])))

    @classmethod
    def encode(cls, obj: Any, *, expected_type:
               Optional[type]) -> Optional[Datum]:
        if isinstance(obj, str):
            return meta.Datum(type='string', value=obj)

        elif isinstance(obj, bytes):
            return meta.Datum(type='bytes', value=obj)

        elif type(obj.__class__) is type(EventGridOutputEvent):
            return meta.Datum(
                type='json',
                value=json.dumps({
                    'id': obj.id,
                    'subject': obj.subject,
                    'dataVersion': obj.data_version,
                    'eventType': obj.event_type,
                    'data': obj.get_json(),
                    'eventTime': cls._format_datetime(obj.event_time)
                })
            )

        elif isinstance(obj, collections.abc.Iterable):
            msgs: List[Union[str, Dict[str, Any]]] = []
            for item in obj:
                if isinstance(item, str):
                    msgs.append(item)
                elif type(obj.__class__) is type(EventGridOutputEvent):
                    msgs.append({'id': item.id,
                                 'subject': item.subject,
                                 'dataVersion': item.data_version,
                                 'eventType': item.event_type,
                                 'data': item.get_json(),
                                 'eventTime': cls._format_datetime(
                                     item.event_time)
                                 })
                else:
                    raise NotImplementedError(
                        'invalid data type in output '
                        'queue message list: {}'.format(type(item)))

            return meta.Datum(
                type='json',
                value=json.dumps(msgs)
            )

        raise NotImplementedError

    @classmethod
    def _format_datetime(cls, dt: Optional[datetime.datetime]):
        if dt is None:
            return None
        else:
            return dt.isoformat()
