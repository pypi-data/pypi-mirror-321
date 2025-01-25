from ton_message_body_decoder import get_decoded_message_body

incoming_aiotx_transfer_notification2 = "te6cckEBAgEAXgABZnNi0JwAAAAAAAAAAF6NSlEACAAe8cPwhRe9LKRcDkQZV7LlT/o2vDUOqGuNTx0s5z+gewEATAAAAAB0ZXN0bmV0IEFJT1RYIHlydCBhbm90aGVyIHRyYW5zZmVy0VckhA=="
incoming_aiotx_transfer_notification = "te6cckEBAgEAUQABZHNi0JwAAAAAAAAAAEO5rKAIAB7xw/CFF70spFwORBlXsuVP+ja8NQ6oa41PHSznP6B7AQA0AAAAAHRlc3RuZXQgQUlPVFggdHJhbnNmZXI96LjF"
incoming_aiotx_transfer_notification3 = "te6cckEBAgEAXQABYnNi0JwAAAAAAAAAADgTQdgAHvHD8IUXvSykXA5EGVey5U/6Nrw1DqhrjU8dLOc/oHsBAE4AAAAAdGVzdG5ldCBXJFJZcmVnNHd0wqMlJF4pXyMgdHJhbnNmZXKEkLo7"


def test_notifications_decoding():
    assert get_decoded_message_body(incoming_aiotx_transfer_notification) == {
        "op_code": "0x7362d09c",
        "op": "jetton_notify",
        "query_id": 0,
        "amount": 1000000000,
        "sender": "UQAPeOH4QovellIuByIMq9lyp_0bXhqHVDXGp46Wc5_QPYZ-",
        "comment": "testnet AIOTX transfer",
    }
    assert get_decoded_message_body(incoming_aiotx_transfer_notification2) == {
        "op_code": "0x7362d09c",
        "op": "jetton_notify",
        "query_id": 0,
        "amount": 1000000000000,
        "sender": "UQAPeOH4QovellIuByIMq9lyp_0bXhqHVDXGp46Wc5_QPYZ-",
        "comment": "testnet AIOTX yrt another transfer",
    }
    assert get_decoded_message_body(incoming_aiotx_transfer_notification3) == {
        "op_code": "0x7362d09c",
        "op": "jetton_notify",
        "query_id": 0,
        "amount": 8467485,
        "sender": "UQAPeOH4QovellIuByIMq9lyp_0bXhqHVDXGp46Wc5_QPYZ-",
        "comment": "testnet W$RYreg4wt£%$^)_# transfer",
    }
