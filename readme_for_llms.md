## Description
The GeoAI ground-level NO2 estimation challenge will ask participants to develop ML models to estimate surface NO2 concentrations using only public remote sensing data as predictor variables. Participants will be provided with ground truth data from air quality monitoring stations and remote sensing data processed by Google Earth Engine (GEE). The challenge encourages participants to explore innovative approaches to NO2 monitoring and modelling, while emphasising simplicity, reproducibility, and transparency in their methodologies. Participants will need to test their models not only in general terms, but also spatially over the study area and temporally over the year, and be able to interpret the given results.

### Key considerations for participants:
- Ensuring the transparency of their model development process, including data pre-processing, feature selection, model architecture and hyper-parameter tuning.
- Demonstrate reproducibility by providing clear documentation and code that allows others to replicate their results.
- Develop models capable of estimating NO2 levels in different weather conditions and seasons, demonstrating adaptability and robustness.

### Evaluation
The evaluation metric for this competition is Root Mean Squared Error.

For every row in the dataset, submission files should contain 2 columns: ID and Target.

Your submission file should look like this (numbers to show format only):

| ID_Zindi | GT_NO2 |
|----------|--------|
| ID_2MYNQS| 22.5   |
| ID_P4U5WU| 13.01  |

An evaluation jury will be set up to give score to each participant considering the four aspects listed below:

1. Performance assessment on in-situ data from selected ground stations not provided to participants, using Pearson correlation (r), Root Mean Square Error (RMSE) and Mean Absolute Error (MAE) as accuracy metrics.
2. Transparency, simplicity and reproducibility of the model methodology.
3. Ability to estimate ground-level NO2 concentrations with high accuracy, regardless of season and location in the study area.
4. Innovation and practicality in approach to NO2 monitoring and modelling.

*Note: The ground truth data used for evaluation are independent from the training data set.*

### The data is:
- Ground-truth data from air quality monitoring stations in the continental part of Lombardy and Veneto regions.
- Remote sensing data of NO2 from Sentinel-5P TROPOMI, precipitation from CHIRPS and land surface temperature from NOAA datasets, all from Google Earth Engine (GEE).
- Participants don't have to use all the parameters provided, but are encouraged to create new ones from the existing ones, which could help to improve the performance of the model.
- Note: Participants will be provided with two datasets. One for modelling which includes ground-truth and remote sensing data, and the second which includes only remote sensing data and will be used to evaluate the developed model.

### Winning solutions need to submit:
- A model file developed in the challenge that can be used to estimate surface NO2 levels.
- An evaluation dataset file with an added column of estimated surface values of NO2 concentrations by the developed model.
- A technical document describing the whole process of developing your model (from pre-processing to evaluation).
- The code used to process the data and train the model, together with the final modelling dataset you used.
 
*Note: we will evaluate the procedure using the technical document; the submission will not be accepted if the methodology is evaluated as unrepeatable. The submitted code is limited to R, Python and/or GEE JavaScript.*

## DESCRIPTION
### FILES
- **Test.csv**: Test resembles Train.csv but without the target-related columns. This is the dataset on which you will apply your model to.
- **Train.csv**: Train contains the target. This is the dataset that you will use to train your model.
- **SampleSubmission.csv**: Is an example of what your submission file should look like. The order of the rows does not matter, but the names of the "ID" must be correct.
- **DataDescription.pdf**: Descriptions of the variables.

| Parameter             | Description                                                           | Source    | Unit       | Temporal resolution | Spatial resolution | % of missing values in modelling dataset |
|-----------------------|-----------------------------------------------------------------------|-----------|------------|---------------------|--------------------|------------------------------------------|
| **ID_Zindi**          | Unique identifier for each row in the dataset                         | -         | -          | -                   | -                  | 0%                                       |
| **Date**              | Date of measurement in format `DD/MM/YY`                              | -         | -          | Daily               | -                  | 0%                                       |
| **ID**                | Identifier for the monitoring station or measurement point            | -         | -          | -                   | -                  | 0%                                       |
| **LAT**               | Latitude of the monitoring station                                    | -         | Degrees    | -                   | -                  | 0%                                       |
| **LON**               | Longitude of the monitoring station                                   | -         | Degrees    | -                   | -                  | 0%                                       |
| **Precipitation**     | Precipitation                                                        | CHIRPS    | mm/d       | Daily               | 5566m              | 0%                                       |
| **LST**               | Land Surface Temperature                                             | NOAA      | K          | Daily               | 1000m              | 46%                                      |
| **AAI**               | Aerosol index at wavelengths 354/388 nm                              | TROPOMI   | -          | Daily               | 1113.2m            | 15%                                      |
| **CloudFraction**     | Effective cloud fraction                                             | TROPOMI   | Fraction   | Daily               | 1113.2m            | 15%                                      |
| **NO2_strat**         | Stratospheric vertical column of NO2                                 | TROPOMI   | mol/m²     | Daily               | 1113.2m            | 15%                                      |
| **NO2_total**         | Total vertical column of NO2                                         | TROPOMI   | mol/m²     | Daily               | 1113.2m            | 15%                                      |
| **NO2_trop**          | Tropospheric vertical column of NO2                                  | TROPOMI   | mol/m²     | Daily               | 1113.2m            | 41%                                      |
| **TropopausePressure**| Tropopause Pressure                                                  | TROPOMI   | Pa         | Daily               | 1113.2m            | 15%                                      |
| **GT_NO2**            | Ground-level NO2 from the station   
