import ipih

from pih import A, PIHThread
from MessageQueueService.const import SD, ATTEMP_COUNT
from pih.collections import Message, nfloat, nbool, nstr
from pih.tools import ParameterList, while_not_do, ne, js, nn, j, nnt


SC = A.CT_SC

ISOLATED: bool = False

from collections import defaultdict
from time import sleep
import random


class DH:
    message_buffer_list: dict[str, list[Message]] = defaultdict(list)


def service_call_handler(sc: SC, pl: ParameterList) -> nbool:
    if sc == SC.add_message_to_queue:
        message: Message | None = pl.next(Message())
        if ne(message):
            message_buffer_list: list[Message] = DH.message_buffer_list[
                nnt(nnt(message).sender)
            ]
            if pl.next():
                message_buffer_list.insert(0, nnt(message))
            else:
                message_buffer_list.append(nnt(message))
            return True
    return None


def send_message(message: Message, delay: nfloat = None) -> None:
    message_value: str = message.message or ""
    if ne(message_value.strip()):
        recipient: str = A.S_P.test_recipient(message.sender) or nnt(message.recipient)

        def send() -> bool:
            if nn(message.location):
                return A.ME_WH_W.send_location(
                    recipient, nnt(message.location), message_value, message.sender
                )
            if nn(message.image_url):
                image_data: nstr = A.D_CO.file_to_base64(nnt(message.image_url))
                if nn(image_data):
                    return A.ME_WH_W.send_image(
                        recipient,
                        message_value,
                        nnt(image_data),
                        message.sender,
                    )
            return A.ME_WH_W.send(recipient, message_value, message.sender)

        while_not_do(
            send,
            attemp_count=ATTEMP_COUNT,
            success_handler=lambda: sleep(nnt(delay)) if nn(delay) else None,
        )


def complete_buffered_message_sending_action(message: Message) -> bool:
    A.L.polibase(js(("Сообщение было отправлено аббоненту:", message.recipient)))
    return True


def buffered_messages_sending_thread_action(sender: A.CT_ME_WH_W.Profiles) -> None:
    while True:
        message_buffer_list: list[Message] = DH.message_buffer_list[sender.value]
        if ne(message_buffer_list):
            message: Message
            try:
                if A.S.get(A.CT_S.WHATSAPP_SENDING_MESSAGES_VIA_WAPPI_IS_ON):
                    message = message_buffer_list.pop(0)
                    send_message(
                        message,
                        delay=random.randint(
                            A.S.get(
                                A.CT_S.WHATSAPP_BUFFERED_MESSAGE_MIN_DELAY_IN_MILLISECONDS
                            ),
                            A.S.get(
                                A.CT_S.WHATSAPP_BUFFERED_MESSAGE_MAX_DELAY_IN_MILLISECONDS
                            ),
                        )
                        / 1000,
                    )
            except Exception as error:
                A.L.polibase(
                    j(
                        (
                            "Ошибка при отправке сообщенияю аббоненту ",
                            message.recipient,
                            ". Ошибка: ",
                            error,
                        )
                    ),
                    A.CT_L_ME_F.ERROR,
                )
        else:
            sleep(1)


def service_starts_handler() -> None:
    for sender_profile in A.CT_ME_WH_W.Profiles:
        PIHThread(buffered_messages_sending_thread_action, args=(sender_profile,))


def start(as_standalone: bool = False) -> None:
    A.SRV_A.serve(
        SD,
        service_call_handler,
        service_starts_handler,
        isolate=ISOLATED,
        as_standalone=as_standalone,
    )


if __name__ == "__main__":
    start()
