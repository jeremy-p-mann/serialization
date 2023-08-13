import streamlit as st
import yaml  # type: ignore

from serial import serialize
from serial.state import StateKey as SK
from serial.state import (get_app_state, set_app_state,
                          set_initial_session_state)

set_initial_session_state()


def serialize_callback():
    input = get_app_state(SK.INPUT)
    output = {
        'serialization': serialize(input),
        'description': input,
    }
    set_app_state(SK.SERIALIZED_INPUT, output)


st.title('Serialization')

input = st.text_area('Enter Workout Description', get_app_state(SK.INPUT))
set_app_state(SK.INPUT, input)
st.button('Serialize', on_click=serialize_callback)

output = get_app_state(SK.SERIALIZED_INPUT)
st.markdown(
    f'''
```yaml
{yaml.dump(output)}
```
'''
)
