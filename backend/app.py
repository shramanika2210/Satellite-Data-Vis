from flask import Flask, request
from flask_cors import CORS
import os
from ndmi import calculate_and_save_ndmi
from ndvi import calculate_and_save_ndvi
from savi import calculate_and_save_savi
from models import run_single_model
from final_test import *
from upload import upload_file

app = Flask(__name__)
CORS(app)


def suggest(ndvi_results, savi_results, ndmi_results):
    # Assuming ndvi_results, savi_results, and ndmi_results are lists of tuples
    for ndvi_result, savi_result, ndmi_result in zip(ndvi_results, savi_results, ndmi_results):
        # Extract the second element from each tuple
        ndvi_label, savi_label, ndmi_label = ndvi_result[1], savi_result[1], ndmi_result[1]

        # Map individual labels to simplified labels
        label_mapping = {
            'Healthy': 'H',
            'Non-vegetated': 'L',
            'Stressed': 'M'
        }

        # Convert individual labels to simplified labels
        simplified_labels = [label_mapping[label] for label in [ndvi_label, savi_label, ndmi_label]]

        # Combine simplified labels to form a combination string
        combination_string = ''.join(simplified_labels)

        # Map the combination to the corresponding overall health
        if combination_string == 'HHH':
            overall_health = 'High Vegetation, High Soil Health, and High Moisture. \nContinue with your current practices, and consider maintaining a balanced approach for long-term sustainability.\n\n'
        elif combination_string == 'HHM':
            overall_health = 'High Vegetation, High Soil Health, and Moderate Moisture. \nCauses: Water Stress\n\n'
        elif combination_string == 'HMH':
            overall_health = 'High Vegetation, Moderate Soil Health, and High Moisture. \nCauses: Soil Fertility, Nutrient Deficiencies\n\n'
        elif combination_string == 'HHL':
            overall_health = 'High Vegetation, High Soil Health, and Low Moisture. \nCauses: Water Stress, Unfavorable Weather Conditions\n\n'
        elif combination_string == 'HLH':
            overall_health = 'High Vegetation, Low Soil Health, and High Moisture. \nCauses: Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies\n\n'
        elif combination_string == 'HMM':
            overall_health = 'High Vegetation, Moderate Soil Health, and Moderate Moisture. \nCauses: Soil Fertility, Nutrient Deficiencies, Water Stress\n\n'
        elif combination_string == 'HLM':
            overall_health = 'High Vegetation, Low Soil Health, and Moderate Moisture. \nCauses: Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies, Water Stress\n\n'
        elif combination_string == 'HML':
            overall_health = 'High Vegetation, Moderate Soil Health, and Low Moisture. \nCauses: Soil Fertility, Nutrient Deficiencies, Water Stress, Unfavorable Weather Conditions\n\n'
        elif combination_string == 'HLL':
            overall_health = 'High Low Low\n\n'
        elif combination_string == 'MHH':
            overall_health = 'Moderate Vegetation, High Soil Health, and High Moisture. \nCauses: Poor Agriculture Practices, Pests, Weeds, and Diseases\n\n'
        elif combination_string == 'MMM':
            overall_health = 'Moderate Vegetation, Moderate Soil Health, and Moderate Moisture. \nCauses: Poor Agriculture Practices, Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies, Water Stress\n\n'
        elif combination_string == 'MMH':
            overall_health = 'Moderate Vegetation, Moderate Soil Health, and High Moisture. \nCauses: Poor Agriculture Practices, Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies\n\n'
        elif combination_string == 'MML':
            overall_health = 'Moderate Vegetation, Moderate Soil Health, and Low Moisture. \nCauses: Poor Agriculture Practices, Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies, Water Stress, Unfavorable Weather Conditions\n\n'
        elif combination_string == 'MHM':
            overall_health = 'Moderate Vegetation, High Soil Health, and Moderate Moisture. \nCauses: Poor Agriculture Practices, Pests, Weeds, and Diseases, Water Stress\n\n'
        elif combination_string == 'MLM':
            overall_health = 'Moderate Vegetation, Low Soil Health, and Moderate Moisture. \nCauses: Poor Agriculture Practices, Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies, Water Stress\n\n'
        elif combination_string == 'MHL':
            overall_health = 'Moderate Vegetation, High Soil Health, and Low Moisture. \nCauses: Poor Agriculture Practices, Pests, Weeds, and Diseases, Water Stress, Unfavorable Weather Conditions \n\n'
        elif combination_string == 'MLH':
            overall_health = 'Moderate Vegetation, Low Soil Health, and High Moisture. \nCauses: Poor Agriculture Practices, Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies\n\n'
        elif combination_string == 'MLL':
            overall_health = 'Moderate Low Low\n\n'
        elif combination_string == 'LHH': 
            overall_health = 'Low Vegetation, High Soil Health, and High Moisture. \nCauses: Poor Agriculture Practices, Seed Quality, Pests, Weeds, and Diseases\n\n'
        elif combination_string == 'LLL':
            overall_health = 'Low Vegetation, Low Soil Health, and Low Moisture. \nCauses: Poor Agriculture Practices, Seed Quality, Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies, Water Stress, Unfavorable Weather Conditions \n\n'
        elif combination_string == 'LLH':
            overall_health = 'Low Vegetation, Low Soil Health, and High Moisture. \nCauses: Poor Agriculture Practices, Seed Quality, Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies \n\n'
        elif combination_string == 'LLM':
            overall_health = 'Low Vegetation, Low Soil Health, and Moderate Moisture. \nCauses: Poor Agriculture Practices, Seed Quality, Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies, Water Stress \n\n'
        elif combination_string == 'LHL':
            overall_health = 'Low Vegetation, High Soil Health, and Low Moisture. \nCauses: Poor Agriculture Practices, Seed Quality, Pests, Weeds, and Diseases, Water Stress, Unfavorable Weather Conditions\n\n'
        elif combination_string == 'LML':
            overall_health = 'Low Vegetation, Moderate Soil Health, and Low Moisture. \nCauses: Poor Agriculture Practices, Seed Quality, Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies, Water Stress, Unfavorable Weather Conditions \n\n'
        elif combination_string == 'LMM':
            overall_health = 'Low Vegetation, Moderate Soil Health, and Moderate Moisture. \nCauses: Poor Agriculture Practices, Seed Quality, Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies, Water Stress \n\n'
        elif combination_string == 'LHM':
            overall_health = 'Low Vegetation, High Soil Health, and Moderate Moisture. \nCauses: Poor Agriculture Practices, Seed Quality, Pests, Weeds, and Diseases, Water Stress\n\n'
        elif combination_string == 'LMH':
            overall_health = 'Low Vegetation, Moderate Soil Health, and High Moisture. \nCauses: Poor Agriculture Practices, Seed Quality, Pests, Weeds, and Diseases, Soil Fertility, Nutrient Deficiencies\n\n'
        else:
            overall_health = 'Invalid combination of predictions'

        print(f"\n\nOverall health for {os.path.basename(ndvi_result[0])}, {os.path.basename(savi_result[0])} and {os.path.basename(ndmi_result[0])}: {overall_health}")

        return(f"\n\nOverall health: {overall_health}")

@app.route('/test',methods=['POST'])
def test():
    if  request.method == 'POST':
        upload_file(request)
        run_single_model("./test", "./test/ndmi-test", calculate_and_save_ndmi)
        run_single_model("./test", "./test/ndvi-test", calculate_and_save_ndvi)
        run_single_model("./test", "./test/savi-test", calculate_and_save_savi)
        # Define class names
        class_names = ['Healthy', 'Non-vegetated', 'Stressed']
        # Predict and display results for ndvi
        ndvi_results = predict_and_display_results('./test/ndvi-test', './model-ndvi-latest.keras', class_names)
        # Predict and display results for savi
        savi_results = predict_and_display_results('./test/savi-test', './model-savi-latest.keras', class_names)
        # Predict and display results for ndmi
        ndmi_results = predict_and_display_results('./test/ndmi-test', './model-ndmi-latest.keras', class_names)
        return suggest(ndvi_results, savi_results, ndmi_results)

if __name__ == "__name__":
    app.run(debug=True)