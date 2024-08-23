WITH Total_Patients AS (
    SELECT
        COUNT(DISTINCT PATID) AS Total_Patients
    FROM
        PCORNET_CDM.CDM.PRIVATE_DEMOGRAPHIC
),

Gender_Breakdown AS (
    SELECT
        'Gender Breakdown' AS Category,
        SEX AS Subcategory,
        COUNT(*) AS Total_Count,
        ROUND((COUNT(*) * 100.0 / SUM(COUNT(*)) OVER ()), 2) AS Percentage_Distribution
    FROM
        PCORNET_CDM.CDM.PRIVATE_DEMOGRAPHIC
    GROUP BY
        SEX
),

Race_Breakdown AS (
    SELECT
        'Race Breakdown' AS Category,
        RACE AS Subcategory,
        COUNT(*) AS Total_Count,
        ROUND((COUNT(*) * 100.0 / SUM(COUNT(*)) OVER ()), 2) AS Percentage_Distribution
    FROM
        PCORNET_CDM.CDM.PRIVATE_DEMOGRAPHIC
    GROUP BY
        RACE
),

Hispanic_Breakdown AS (
    SELECT
        'Hispanic Breakdown' AS Category,
        HISPANIC AS Subcategory,
        COUNT(*) AS Total_Count,
        ROUND((COUNT(*) * 100.0 / SUM(COUNT(*)) OVER ()), 2) AS Percentage_Distribution
    FROM
        PCORNET_CDM.CDM.PRIVATE_DEMOGRAPHIC
    GROUP BY
        HISPANIC
),

Sexual_Orientation_Breakdown AS (
    SELECT
        'Sexual Orientation Breakdown' AS Category,
        SEXUAL_ORIENTATION AS Subcategory,
        COUNT(*) AS Total_Count,
        ROUND((COUNT(*) * 100.0 / SUM(COUNT(*)) OVER ()), 2) AS Percentage_Distribution
    FROM
        PCORNET_CDM.CDM.PRIVATE_DEMOGRAPHIC
    GROUP BY
        SEXUAL_ORIENTATION
)

-- Select statements to retrieve all the information together
SELECT
    'Total Patients' AS Category,
    NULL AS Subcategory,
    Total_Patients AS Total_Count,
    NULL AS Percentage_Distribution
FROM
    Total_Patients

UNION ALL

SELECT * FROM Gender_Breakdown

UNION ALL

SELECT * FROM Race_Breakdown

UNION ALL

SELECT * FROM Hispanic_Breakdown

UNION ALL

SELECT * FROM Sexual_Orientation_Breakdown
;
