from enum import Enum
from typing import Any, Dict

import streamlit as st


class StateKey(str, Enum):
    INPUT = 'input'
    SERIALIZED_INPUT = 'serialized_input'


def get_initial_session_state() -> Dict[StateKey, Any]:
    return {StateKey.INPUT: '', StateKey.SERIALIZED_INPUT: {
        'serialization': {},
        'description': '',
    }
    }


def set_initial_session_state():
    init = get_initial_session_state()
    for key, value in init.items():
        if key.value not in st.session_state:
            set_app_state(key, value)


def set_app_state(state_key: StateKey, value):
    st.session_state[state_key.value] = value


def get_app_state(state_key: StateKey):
    return st.session_state[state_key.value]
