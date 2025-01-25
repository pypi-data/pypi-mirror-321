from ton_message_body_decoder import get_decoded_message_body

jetton_transfer = "te6cckEBAgEAbAABqA+KfqUAAAAAAAAAABAYAC/NRlgHRzROUNpKFDghRcU6l8mrqcE7KKOIP2lEyfyxAD7EmELlibbgmLLQ0japUp0eP3nEmAhTnITYg55gQnVGxzEtAQEAJgAAAABweXRlc3QgdHJhbnNmZXLpA50E"
jetton_transfer2 = "te6cckEBAgEAggABrA+KfqUAAAAAAAAAADgTQdgB++pdVNAMpa4HfQzQEjBLHKrbGgzxTUNn4fpHUfdhI9cAA944fhCi96WUi4HIgyr2XKn/RteGodUNcanjpZzn9A9HMS0BAQBOAAAAAHRlc3RuZXQgVyRSWXJlZzR3dMKjJSReKV8jIHRyYW5zZmVyl+m69A=="


def test_notifications_decoding():
    print(get_decoded_message_body(jetton_transfer2))
    assert get_decoded_message_body(jetton_transfer) == {
        "op": "jetton_transfer",
        "query_id": 0,
        "amount": 1,
        "destination": "UQAX5qMsA6OaJyhtJQocEKLinUvk1dTgnZRRxB-0omT-WHAv",
        "response_address": "UQD7EmELlibbgmLLQ0japUp0eP3nEmAhTnITYg55gQnVG7ZS",
        "forward_amount": 10000000,
        "comment": "pytest transfer",
        "has_custom_payload": False,
        "custom_payload": None,
        "has_forward_payload": True,
    }
    assert get_decoded_message_body(jetton_transfer2) == {
        "op": "jetton_transfer",
        "query_id": 0,
        "amount": 8467485,
        "destination": "UQD99S6qaAZS1wO-hmgJGCWOVW2NBnimobPw_SOo-7CR638T",
        "response_address": "UQAPeOH4QovellIuByIMq9lyp_0bXhqHVDXGp46Wc5_QPYZ-",
        "forward_amount": 10000000,
        "comment": "testnet W$RYreg4wt£%$^)_# transfer",
        "has_custom_payload": False,
        "custom_payload": None,
        "has_forward_payload": True,
    }
