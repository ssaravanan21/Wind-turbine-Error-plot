# Wind Turbine Error Analysis Tool

This tool facilitates the rapid visualization and comparison of plots related to wind turbine errors. When an error occurs in the wind turbine, a buffer file is generated. This buffer file contains 52 columns and nearly 6000 rows of data. The columns include information such as converter voltage, current, frequency, and wind speed. Each row is timestamped, capturing data 30 seconds before and after the error with a sampling time of 0.02 seconds.

Traditionally, error analysis involved manual inspection of Excel files, which is not the most efficient method. To streamline this process, we've developed a web application using Python's Pandas and Plotly libraries. This application enables users to visualize and analyze error data in a more effective manner.

While Excel can provide plots, it often takes time to process. By leveraging Pandas, we can handle the data more efficiently. Plotly enhances the experience by allowing users to zoom in and explore details within the plots.

As an additional feature, we've incorporated frequency derivation, a useful parameter for error analysis. This data column is not typically present in the buffer file but adds valuable insights.

Another notable feature is the comparison plot, which allows users to analyze two columns simultaneously. This tool is designed to make error analysis in wind power plants more accessible and efficient.

After testing with the technician, we have identified the need for an additional feature. This feature should allow us to upload files in either XLSX or TXT format.

Initially, we generate .txt files from SCADA. If we can directly upload these .txt files, it would greatly streamline our process, saving both time and effort. As a result, we have implemented this functionality
