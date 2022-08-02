# Copyright 2018-2021 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st

options = ("male", "female")
i1 = st.multiselect("multiselect 1", options)
st.text(f"value 1: {i1}")

i2 = st.multiselect("multiselect 2", options, format_func=lambda x: x.capitalize())
st.text(f"value 2: {i2}")

i3 = st.multiselect("multiselect 3", [])
st.text(f"value 3: {i3}")

i4 = st.multiselect("multiselect 4", ["coffee", "tea", "water"], ["tea", "water"])
st.text(f"value 4: {i4}")

i5 = st.multiselect(
    "multiselect 5",
    list(
        map(
            lambda x: f"{x} I am a ridiculously long string to have in a multiselect, so perhaps I should just not wrap and go to the next line.",
            range(5),
        )
    ),
)
st.text(f"value 5: {i5}")

if st._is_running_with_streamlit:

    def on_change():
        st.session_state.multiselect_changed = True

    st.multiselect("multiselect 6", options, key="multiselect6", on_change=on_change)
    st.text("value 6: %s" % st.session_state.multiselect6)
    st.text(f"multiselect changed: {'multiselect_changed' in st.session_state}")
