import streamlit as st
import requests
import os

from settings import app_config
from basic_auth import authenticate_user


def run():
    if authenticate_user():
        st.set_page_config(layout="wide")
        st.title("Predicting the coupon recommendation :ticket:")
        st.markdown(
            "This app is a demo app for deploying to productinise ML model. \
                    The most important properties are presented at the top \
                    whilst the rest is included in the expandable section."
        )
        st.markdown("The prediction is between 0 - 1.")
        st.markdown("Select specific values for the characteristics below:")

        with st.container():
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                time = st.slider(
                    label="Time",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="time",
                )
                expiration = st.slider(
                    label="Expiration",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="expiration",
                )
                age = st.slider(
                    label="Age",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="age",
                )
            with col2:
                education = st.slider(
                    label="Education",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="Education",
                )
                income = st.slider(
                    label="Income",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="Educincomeation",
                )
                bar = st.slider(
                    label="Bar",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="bar",
                )
            with col3:
                coffee_house = st.slider(
                    label="Coffee House",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="coffee_house",
                )
                carry_away = st.slider(
                    label="Carry Away",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="carry_away",
                )
                restaurant_20_to_50 = st.slider(
                    label="Restaurant 20 to 50",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="restaurant_20_to_50",
                )
            with col4:
                coupon_geq_15min = st.slider(
                    label="Coupon GEQ 15min",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="coupon_geq_15min",
                )
                coupon_geq_25min = st.slider(
                    label="Coupon GEQ 25min",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="coupon_geq_25min",
                )
                direction_same = st.slider(
                    label="Same direction",
                    min_value=0,
                    max_value=10,
                    step=1,
                    value=5,
                    key="direction_same",
                )

        data = {
            "col_0": 0,
            "col_1": 0,
            "col_2": 0,
            "col_3": 1,
            "col_4": 0,
            "col_5": 0,
            "col_6": 0,
            "col_7": 0,
            "col_8": 0,
            "col_9": 0,
            "col_10": 0,
            "col_11": 0,
            "col_12": 2,
            "col_13": 0,
            "col_14": 0,
            "col_15": 0,
            "col_16": 0,
            "col_17": 0,
            "col_18": 0,
            "col_19": 0,
            "col_20": 0,
            "col_21": 1,
            "col_22": 0,
            "col_23": 1,
            "col_24": 0,
            "col_25": 0,
            "col_26": 0,
            "time": time,
            "expiration": expiration,
            "age": age,
            "education": education,
            "income": income,
            "Bar": bar,
            "CoffeeHouse": coffee_house,
            "CarryAway": carry_away,
            "Restaurant20To50": restaurant_20_to_50,
            "toCoupon_GEQ15min": coupon_geq_15min,
            "toCoupon_GEQ25min": coupon_geq_25min,
            "direction_same": direction_same,
        }
        inference_input = {
            "instances": [
                list(data.values())
            ]
        }

        if st.button("Predict"):
            response = requests.post(
                f"{app_config.KSERVE_ENDPOINT}/v1/models/{app_config.MODEL_NAME}:predict",
                json=inference_input,
            )
            response.raise_for_status()
            prediction = response.json()
            pred_result = prediction["predictions"][0]

            with st.container():
                if pred_result >= 0.5:
                    st.success(f"The prediction is: **{pred_result}**")
                else:
                    st.warning(f"The prediction is: **{pred_result}**")


if __name__ == "__main__":
    run()
