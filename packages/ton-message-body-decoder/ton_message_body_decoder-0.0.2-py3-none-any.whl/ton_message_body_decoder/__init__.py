from pytoniq_core.boc.deserialize import Boc
from typing import Any
from pytoniq_core import Slice
import base64
# Jetton op codes:
# https://github.com/ton-blockchain/token-contract/blob/main/ft/op-codes.fc


def decode_jetton_transfer(slice: Slice) -> dict[str, Any]:
    # Decode transfer details
    query_id = slice.load_uint(64)
    amount = slice.load_coins()
    destination = slice.load_address()
    response_address = slice.load_address()

    # Check if custom payload exists
    has_custom_payload = slice.load_bool()
    custom_payload = None
    if has_custom_payload:
        custom_payload = slice.load_ref()
    # Forward amount in nanotons
    forward_amount = slice.load_coins()

    # Forward payload
    has_forward_payload = slice.load_bool()
    forward_payload = None
    if has_forward_payload:
        forward_payload = slice.load_ref()

    # Decode comment if present in forward payload
    comment = None
    if forward_payload:
        fp_slice = forward_payload.begin_parse()
        if fp_slice.remaining_bits >= 32:
            comment_op = fp_slice.load_uint(32)
            if comment_op == 0:  # Text comment op code
                comment = fp_slice.load_snake_string()

    return {
        "op": "jetton_transfer",
        "query_id": query_id,
        "amount": amount,
        "destination": destination.to_str(is_bounceable=False) if destination else None,
        "response_address": response_address.to_str(is_bounceable=False)
        if response_address
        else None,
        "forward_amount": forward_amount,
        "comment": comment,
        "has_custom_payload": has_custom_payload,
        "custom_payload": custom_payload,
        "has_forward_payload": has_forward_payload,
        "op_code": hex(0xF8A7EA5),
    }


def decode_jetton_notification(slice: Slice) -> dict[str, Any]:
    query_id = slice.load_uint(64)
    amount = slice.load_coins()
    sender = slice.load_address()

    # Forward payload (contains comment)
    forward_payload = None
    comment = None
    if slice.remaining_refs > 0:
        forward_payload = slice.load_ref()
        if forward_payload:
            fp_slice = forward_payload.begin_parse()
            if fp_slice.remaining_bits >= 32:
                comment_op = fp_slice.load_uint(32)
                if comment_op == 0:  # Text comment op code
                    comment = fp_slice.load_snake_string()

    return {
        "op": "jetton_notify",
        "query_id": query_id,
        "amount": amount,
        "sender": sender.to_str(is_bounceable=False) if sender else None,
        "comment": comment,
        "op_code": hex(0x7362D09C),
    }


def get_decoded_message_body(boc_payload: str) -> dict:
    try:
        decoded_bytes = base64.b64decode(boc_payload)
        boc = Boc(decoded_bytes)
        cells = boc.deserialize()
        slice: Slice = cells[0].begin_parse()

        # Check operation code
        op = slice.load_uint(32)
        if op == 0xF8A7EA5:  # Jetton Transfer op code
            return decode_jetton_transfer(slice)
        elif op == 0x7362D09C:  # Jetton Notify op code
            return decode_jetton_notification(slice)
        else:
            return {"op_code": hex(op), "op": "unknown"}
    except Exception as e:
        print(f"Error decoding notification: {e}")
        return {}
