import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

def main():
    st.title("Excel Data Plotter")

    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Data Preview:")
        st.write(df)

        if 'Column9' in df.columns:
            # Handle missing or incompatible data in 'Column9'
            try:
                # Convert 'Column9' to numeric and handle non-numeric values
                df['Column9'] = pd.to_numeric(df['Column9'], errors='coerce')
                df['Column9_Derivative'] = df['Column9'].diff()
            except Exception as e:
                st.error(f"Error calculating the derivative of 'Column9': {str(e)}")
        else:
            st.error("Column 'Column9' does not exist in the DataFrame.")

        # Create a dictionary with custom names for columns
        custom_column_names = {
            'Column1': 'Timestamp',  # Add more columns as needed
            'Column2': 'Converter_UL1',
            'Column3': 'Converter_UL2',
            'Column4': 'Converter_UL3',
            'Column5': 'Converter_I1',
            'Column6': 'Converter_I2',
            'Column7': 'Converter_I3',
            'Column8': 'Converter_rectifier_U',
            'Column9_Derivative': 'Derivative of grid_frequency',  # New column name
            'Column9': 'Converter_grid_frequency',
            'Column10': 'Converter_active_power',
            'Column11': 'Converter_reactive_power',  
            'Column12': 'Converter_U_DC_positive',
            'Column13': 'Converter_U_DC_negative',
            'Column14': 'Converter_I_DC',
            'Column15': 'Converter_chopper_I',
            'Column16': 'Converter_DC_current_setpoint',
            'Column17': 'Converter_reactive_power_setpoint',
            'Column18': 'Acceleration_nacelle_x',
            'Column19': 'Acceleration_nacelle_y',
            'Column20': 'Acceleration_nacelle_effective_value',
            'Column21': 'Generator_speed_momentary',  
            'Column22': 'Overspeed_modul_generator_speed_1',
            'Column23': 'Overspeed_modul_generator_speed_2',
            'Column24': 'Yaw_position',
            'Column25': 'Wind_speed',
            'Column26': 'Pitch_capacitor_voltage_hi_1',
            'Column27': 'Pitch_capacitor_voltage_hi_2',
            'Column28': 'Pitch_capacitor_voltage_hi_3',
            'Column29': 'Pitch_capacitor_voltage_lo_1',
            'Column30': 'Pitch_capacitor_voltage_lo_2',
            'Column31': 'Pitch_capacitor_voltage_lo_3',  
            'Column32': 'Pitch_position_blade_1',
            'Column33': 'Pitch_position_blade_2',
            'Column34': 'Pitch_position_blade_3',
            'Column35': 'Pitch_error_code_1_1',
            'Column36': 'Pitch_error_code_1_2',
            'Column37': 'Pitch_error_code_2_1',
            'Column38': 'Pitch_error_code_2_2',
            'Column39': 'Pitch_error_code_3_1',
            'Column40': 'Pitch_error_code_3_2',
            'Column41': 'Pitch_supply_24V_DC_1',  
            'Column42': 'Pitch_supply_24V_DC_2',
            'Column43': 'Pitch_supply_24V_DC_3',
            'Column44': 'Pitch_rate_demand_1',
            'Column45': 'Pitch_rate_demand_2',
            'Column46': 'Pitch_rate_demand_3',
            'Column47': 'Gh_torque_demand',
            'Column48': 'Converter_state_err',
            'Column49': 'Pitch_error_code_1_3',
            'Column50': 'Pitch_error_code_2_3',
            'Column51': 'Pitch_error_code_3_3',  
            'Column52': 'Rated_blade_pos'
            # Add more columns as needed
        }

        st.sidebar.subheader("Select Columns for Plotting")

        selected_column_1 = st.sidebar.selectbox("Select the first column for plotting", list(custom_column_names.values()))
        st.write(f"You selected: {selected_column_1}")
        selected_column_1 = next(key for key, value in custom_column_names.items() if value == selected_column_1)

        # Modify the y-axis label
        y_axis_label_1 = custom_column_names[selected_column_1]

        fig1 = px.line(df, x='Column1', y=selected_column_1, title="Data Plot")
        fig1.update_yaxes(title_text=y_axis_label_1)  # Set the y-axis label
        fig1.update_xaxes(title_text="Time")  # Set the x-axis label

        st.plotly_chart(fig1)

        st.sidebar.subheader("Compare Two Columns")

        selected_column_2 = st.sidebar.selectbox("Select the second column for comparison", list(custom_column_names.values()))
        st.write(f"You selected: {selected_column_2}")
        selected_column_2 = next(key for key, value in custom_column_names.items() if value == selected_column_2)

        # Modify the y-axis labels
        y_axis_label_2 = custom_column_names[selected_column_2]

        # Create a plot for comparing the two selected columns
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df['Column1'], y=df[selected_column_1], mode='lines', name=y_axis_label_1))
        fig2.add_trace(go.Scatter(x=df['Column1'], y=df[selected_column_2], mode='lines', name=y_axis_label_2))

        fig2.update_layout(title="Comparison Plot", xaxis_title="Time", yaxis_title="Values")
        st.plotly_chart(fig2)
        st.markdown("SA21", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
